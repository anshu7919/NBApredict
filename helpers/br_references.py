"""
Contains constants from basketballreference.com or for interaction with basketballreference based tables.

For example, it contains all team names and abbreviations as well as headers for different tables that are queried.
All of the classes come from the br_web_scraper repo available on github. I am not clear on why the classes use enums
which I've largely worked around in the package. Other lists and dictionaries were generated specifically for this
project.
"""

from enum import Enum
import os
from helpers import test


class Location(Enum):
    HOME = "HOME"
    AWAY = "AWAY"


class Outcome(Enum):
    WIN = "WIN"
    LOSS = "LOSS"


class Team(Enum):
    ATLANTA_HAWKS = "ATLANTA HAWKS"
    BOSTON_CELTICS = "BOSTON CELTICS"
    BROOKLYN_NETS = "BROOKLYN NETS"
    CHARLOTTE_HORNETS = "CHARLOTTE HORNETS"
    CHICAGO_BULLS = "CHICAGO BULLS"
    CLEVELAND_CAVALIERS = "CLEVELAND CAVALIERS"
    DALLAS_MAVERICKS = "DALLAS MAVERICKS"
    DENVER_NUGGETS = "DENVER NUGGETS"
    DETROIT_PISTONS = "DETROIT PISTONS"
    GOLDEN_STATE_WARRIORS = "GOLDEN STATE WARRIORS"
    HOUSTON_ROCKETS = "HOUSTON ROCKETS"
    INDIANA_PACERS = "INDIANA PACERS"
    LOS_ANGELES_CLIPPERS = "LOS ANGELES CLIPPERS"
    LOS_ANGELES_LAKERS = "LOS ANGELES LAKERS"
    MEMPHIS_GRIZZLIES = "MEMPHIS GRIZZLIES"
    MIAMI_HEAT = "MIAMI HEAT"
    MILWAUKEE_BUCKS = "MILWAUKEE BUCKS"
    MINNESOTA_TIMBERWOLVES = "MINNESOTA TIMBERWOLVES"
    NEW_ORLEANS_PELICANS = "NEW ORLEANS PELICANS"
    NEW_YORK_KNICKS = "NEW YORK KNICKS"
    OKLAHOMA_CITY_THUNDER = "OKLAHOMA CITY THUNDER"
    ORLANDO_MAGIC = "ORLANDO MAGIC"
    PHILADELPHIA_76ERS = "PHILADELPHIA 76ERS"
    PHOENIX_SUNS = "PHOENIX SUNS"
    PORTLAND_TRAIL_BLAZERS = "PORTLAND TRAIL BLAZERS"
    SACRAMENTO_KINGS = "SACRAMENTO KINGS"
    SAN_ANTONIO_SPURS = "SAN ANTONIO SPURS"
    TORONTO_RAPTORS = "TORONTO RAPTORS"
    UTAH_JAZZ = "UTAH JAZZ"
    WASHINGTON_WIZARDS = "WASHINGTON WIZARDS"

    # DEPRECATED TEAMS
    CHARLOTTE_BOBCATS = "CHARLOTTE BOBCATS"
    NEW_JERSEY_NETS = "NEW JERSEY NETS"
    NEW_ORLEANS_HORNETS = "NEW ORLEANS HORNETS"
    NEW_ORLEANS_OKLAHOMA_CITY_HORNETS = "NEW ORLEANS/OKLAHOMA CITY HORNETS"
    SEATTLE_SUPERSONICS = "SEATTLE SUPERSONICS"
    VANCOUVER_GRIZZLIES = "VANCOUVER GRIZZLIES"


class OutputType(Enum):
    JSON = "JSON"
    CSV = "CSV"


class OutputWriteOption(Enum):
    WRITE = "w"
    CREATE_AND_WRITE = "w+"
    APPEND = "a"
    APPEND_AND_WRITE = "a+"


class Position(Enum):
    POINT_GUARD = "POINT GUARD"
    SHOOTING_GUARD = "SHOOTING GUARD"
    SMALL_FORWARD = "SMALL FORWARD"
    POWER_FORWARD = "POWER FORWARD"
    CENTER = "CENTER"


class Tables(Enum):
    misc_stats = "misc_stats"


TEAM_ABBREVIATIONS_TO_TEAM = {
    'ATL': Team.ATLANTA_HAWKS,
    'BOS': Team.BOSTON_CELTICS,
    'BRK': Team.BROOKLYN_NETS,
    'CHI': Team.CHICAGO_BULLS,
    'CHO': Team.CHARLOTTE_HORNETS,
    'CLE': Team.CLEVELAND_CAVALIERS,
    'DAL': Team.DALLAS_MAVERICKS,
    'DEN': Team.DENVER_NUGGETS,
    'DET': Team.DETROIT_PISTONS,
    'GSW': Team.GOLDEN_STATE_WARRIORS,
    'HOU': Team.HOUSTON_ROCKETS,
    'IND': Team.INDIANA_PACERS,
    'LAC': Team.LOS_ANGELES_CLIPPERS,
    'LAL': Team.LOS_ANGELES_LAKERS,
    'MEM': Team.MEMPHIS_GRIZZLIES,
    'MIA': Team.MIAMI_HEAT,
    'MIL': Team.MILWAUKEE_BUCKS,
    'MIN': Team.MINNESOTA_TIMBERWOLVES,
    'NOP': Team.NEW_ORLEANS_PELICANS,
    'NYK': Team.NEW_YORK_KNICKS,
    'OKC': Team.OKLAHOMA_CITY_THUNDER,
    'ORL': Team.ORLANDO_MAGIC,
    'PHI': Team.PHILADELPHIA_76ERS,
    'PHO': Team.PHOENIX_SUNS,
    'POR': Team.PORTLAND_TRAIL_BLAZERS,
    'SAC': Team.SACRAMENTO_KINGS,
    'SAS': Team.SAN_ANTONIO_SPURS,
    'TOR': Team.TORONTO_RAPTORS,
    'UTA': Team.UTAH_JAZZ,
    'WAS': Team.WASHINGTON_WIZARDS,

    # DEPRECATED TEAMS
    'NJN': Team.NEW_JERSEY_NETS,
    'NOH': Team.NEW_ORLEANS_HORNETS,
    'NOK': Team.NEW_ORLEANS_OKLAHOMA_CITY_HORNETS,
    'CHA': Team.CHARLOTTE_BOBCATS,
    'CHH': Team.CHARLOTTE_HORNETS,
    'SEA': Team.SEATTLE_SUPERSONICS,
    'VAN': Team.VANCOUVER_GRIZZLIES,
}

team_to_team_abbreviation = {
    "ATLANTA HAWKS": "ATL",
    "BOSTON CELTICS": "BOS",
    "BROOKLYN NETS": "BRK",
    "CHARLOTTE HORNETS": "CHO",
    "CHICAGO BULLS": "CHI",
    "CLEVELAND CAVALIERS": "CLE",
    "DALLAS MAVERICKS": "DAL",
    "DENVER NUGGETS": "DEN",
    "DETROIT PISTONS": "DET",
    "GOLDEN STATE WARRIORS": "GSW",
    "HOUSTON ROCKETS": "HOU",
    "INDIANA PACERS": "IND",
    "LOS ANGELES CLIPPERS": "LAC",
    "LOS ANGELES LAKERS": "LAL",
    "MEMPHIS GRIZZLIES": "MEM",
    "MIAMI HEAT": "MIA",
    "MILWAUKEE BUCKS": "MIL",
    "MINNESOTA TIMBERWOLVES": "MIN",
    "NEW ORLEANS PELICANS": "NOP",
    "NEW YORK KNICKS": "NYK",
    "OKLAHOMA CITY THUNDER": "OKC",
    "ORLANDO MAGIC": "ORL",
    "PHILADELPHIA 76ERS": "PHI",
    "PHOENIX SUNS": "PHO",
    "PORTLAND TRAIL BLAZERS": "POR",
    "SACRAMENTO KINGS": "SAC",
    "SAN ANTONIO SPURS": "SAS",
    "TORONTO RAPTORS": "TOR",
    "UTAH JAZZ": "UTA",
    "WASHINGTON WIZARDS": "WAS",
    
    # DEPRECATED TEAMS
    "CHARLOTTE BOBCATS": "CHA",
    "NEW JERSEY NETS": "NJN",
    "NEW ORLEANS HORNETS": "NOH",
    "NEW ORLEANS/OKLAHOMA CITY HORNETS": "NOK",
    "SEATTLE SUPERSONICS": "SEA",
    "VANCOUVER GRIZZLIES": "VAN"
}

POSITION_ABBREVIATIONS_TO_POSITION = {
    "PG": Position.POINT_GUARD,
    "SG": Position.SHOOTING_GUARD,
    "SF": Position.SMALL_FORWARD,
    "PF": Position.POWER_FORWARD,
    "C": Position.CENTER,
}

bball_ref_tbl_names = {
    "misc_stats": Tables.misc_stats
}

data_stat_headers = [  # Column headers for the misc_stats table
    "team_name", "age", "wins",
    "losses", "wins_pyth", "losses_pyth",
    "mov", "sos", "srs", "off_rtg",
    "def_rtg", "pace", "fta_per_fga_pct",
    "fg3a_per_fga_pct", "ts_pct",
    "efg_pct", "tov_pct", "orb_pct",
    "ft_rate", "opp_efg_pct", "opp_tov_pct",
    "drb_pct", "opp_ft_rate", "arena_name",
    "attendance", "attendance_per_g"
]

four_factors = [  # The offensive and defensive four factors
    "efg_pct", "tov_pct", "orb_pct",
    "ft_rate", "opp_efg_pct", "opp_tov_pct",
    "drb_pct", "opp_ft_rate"
]

BASE_URL = 'https://www.basketball-reference.com'
# JSON_REFERENCE_PATH = os.path.join(test.project_directory(), "data", "references.json")
