import general
# from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy import MetaData


# Type conversion functions
def get_py_type(tbl_dict):
    """Given a table dictionary (formatted as key:[list]), returns a dictionary of tbl_key: py_type where py_type can
    be 'integer', 'float', or 'string' (at the moment)"""

    tbl_keys = list(tbl_dict.keys())
    py_types = [general.get_type(tbl_dict[key]) for key in list(tbl_dict.keys())]
    py_types_dict = dict(zip(tbl_keys, py_types))
    return py_types_dict


def get_sql_type(tbl_dict):
    """Given a table dictionary (formatted as key:[list]), returns a dictionary of tbl_key: sql_type
    where sql_type is a sqlalchemy sql_type class"""

    py_types = get_py_type(tbl_dict) #py_types is a dict
    sql_types = py_type_to_sql_type(py_types)
    return(sql_types)


def py_type_to_sql_type(py_types):
    """Converts a dictionary of python types to a dictionary of sql types where sql type is a sqlalchemy sql_type
    class"""

    sql_types = dict()
    for key in py_types:
        if py_types[key] == "integer":
            sql_types[key] = Integer
        elif py_types[key] == "float":
            sql_types[key] = Float
        elif py_types[key] == "string":
            sql_types[key] = String
        else:
            raise Exception("Error: py_type {} is not an integer, float, or string".format(py_types[key]))
    return sql_types


# Database interaction functions


def create_table(engine, name, cols, overwrite = False):
    """Creates a table(name) in the engine with the specified cols
    engine: sql_alchemy create_engine(url) output
    name: name for the created table
    cols: """

    Base = declarative_base()
    Base.metadata.reflect(engine)
    if name in Base.metadata.tables and not overwrite:
        print("Table exists and overwrite is False. Returning without making changes")
        return
    elif name in Base.metadata.tables and overwrite:
        print("Table exists and overwrite is True. Overwriting table")
        drop_table(engine, name)
    table = type(name, (Base, ), cols)
    table.__table__.create(bind=engine)


def create_col_definitions(tbl_name, id_type_dict):
    """Returns a dictionary that begins with __table__name and an integer id followed by columns as specified
    in the id_type_dict
    tbl_name: name of the desired table
    id_type_dict: dictionary of column id's and associated sql_alchemy sql types"""

    col_specs = {'__tablename__': '{}'.format(tbl_name),
                 'id': Column(Integer, primary_key=True)}
    for key in id_type_dict:
        col_specs[key] = Column(id_type_dict[key])

    return col_specs


def drop_table(engine, drop_tbl):
    """Function takes an engine, finds table in the engine, drops the drop_tbl from the engine"""

    metadata = MetaData(bind=engine)
    metadata.reflect(bind=engine)
    drop_tbl_class = metadata.tables[drop_tbl]
    drop_tbl_class.drop()
