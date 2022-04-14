"""SQL Statements for importing CSV data."""

import csv
from sqlite3 import Connection, ProgrammingError

import click

CIRCUITS_CREATE = """CREATE TABLE circuits (
    circuitId INTEGER PRIMARY KEY,
    circuitRef TEXT NOT NULL,
    name TEXT NOT NULL,
    location TEXT,
    country TEXT,
    lat REAL,
    lng REAL,
    alt INTEGER,
    url TEXT UNIQUE
)
"""

CIRCUITS_INSERT = """INSERT INTO circuits VALUES (
    :circuitId,
    :circuitRef,
    :name,
    :location,
    :country,
    :lat,
    :lng,
    :alt,
    :url
)
"""

CONSTRUCTOR_RESULTS_CREATE = """CREATE TABLE constructor_results (
    constructorResultsId INTEGER PRIMARY KEY,
    raceId INTEGER NOT NULL ,
    constructorId INTEGER NOT NULL ,
    points REAL,
    status TEXT
)
"""

CONSTRUCTOR_RESULTS_INSERT = """INSERT INTO constructor_results VALUES (
    :constructorResultsId,
    :raceId,
    :constructorId,
    :points,
    :status
)
"""

CONSTRUCTOR_STANDINGS_CREATE = """CREATE TABLE constructor_standings (
    constructorStandingsId INTEGER PRIMARY KEY,
    raceId INTEGER NOT NULL,
    constructorId INTEGER NOT NULL,
    points REAL NOT NULL,
    position INTEGER,
    positionText TEXT,
    wins INTEGER NOT NULL
)
"""

CONSTRUCTOR_STANDINGS_INSERT = """INSERT INTO constructor_standings VALUES (
    :constructorStandingsId,
    :raceId,
    :constructorId,
    :points,
    :position,
    :positionText,
    :wins
)
"""

CONSTRUCTORS_CREATE = """CREATE TABLE constructors (
    constructorId INTEGER PRIMARY KEY,
    constructorRef TEXT NOT NULL,
    name TEXT NOT NULL UNIQUE,
    nationality TEXT,
    url TEXT NOT NULL
)
"""

CONSTRUCTORS_INSERT = """INSERT INTO constructors VALUES (
    :constructorId,
    :constructorRef,
    :name,
    :nationality,
    :url
)
"""

DRIVER_STANDINGS_CREATE = """CREATE TABLE driver_standings (
    driverStandingsId INTEGER PRIMARY KEY,
    raceId INTEGER NOT NULL,
    driverId INTEGER NOT NULL,
    points REAL NOT NULL,
    position INTEGER,
    positionText TEXT,
    wins INTEGER
)
"""

DRIVER_STANDINGS_INSERT = """INSERT INTO driver_standings VALUES (
    :driverStandingsId,
    :raceId,
    :driverId,
    :points,
    :position,
    :positionText,
    :wins
)
"""

DRIVERS_CREATE = """CREATE TABLE drivers (
    driverId INTEGER PRIMARY KEY,
    driverRef TEXT NOT NULL,
    number INTEGER,
    code TEXT,
    forename TEXT NOT NULL,
    surname TEXT NOT NULL,
    dob TEXT,
    nationality TEXT,
    url TEXT NOT NULL
)
"""

DRIVERS_INSERT = """INSERT INTO drivers VALUES (
    :driverId,
    :driverRef,
    :number,
    :code,
    :forename,
    :surname,
    :dob,
    :nationality,
    :url
)
"""

LAP_TIMES_CREATE = """CREATE TABLE lap_times (
    raceId INTEGER,
    driverId INTEGER,
    lap INTEGER,
    position INTEGER,
    time TEXT,
    milliseconds INTEGER
)
"""

LAP_TIMES_INSERT = """INSERT INTO lap_times VALUES (
    :raceId,
    :driverId,
    :lap,
    :position,
    :time,
    :milliseconds
)
"""

PIT_STOPS_CREATE = """CREATE TABLE pit_stops (
    raceId INTEGER,
    driverId INTEGER,
    stop INTEGER,
    lap INTEGER NOT NULL,
    time TEXT NOT NULL,
    duration TEXT,
    milliseconds INTEGER
)
"""

PIT_STOPS_INSERT = """INSERT INTO pit_stops VALUES (
    :raceId,
    :driverId,
    :stop,
    :lap,
    :time,
    :duration,
    :milliseconds
)
"""

QUALIFYING_CREATE = """CREATE TABLE qualifying (
    qualifyId INTEGER PRIMARY KEY,
    raceId INTEGER NOT NULL,
    driverId INTEGER NOT NULL,
    constructorId INTEGER NOT NULL,
    number INTEGER NOT NULL,
    position INTEGER,
    q1 TEXT,
    q2 TEXT,
    q3 TEXT
)
"""

QUALIFYING_INSERT = """INSERT INTO qualifying VALUES (
    :qualifyId,
    :raceId,
    :driverId,
    :constructorId,
    :number,
    :position,
    :q1,
    :q2,
    :q3
)
"""

# NOTE: Ignoring fp1/fp2/fp3/quali/sprint dates & times fields
RACES_CREATE = """CREATE TABLE races (
    raceId INTEGER PRIMARY KEY,
    year INTEGER NOT NULL,
    round INTEGER NOT NULL,
    circuitId INTEGER NOT NULL,
    name TEXT NOT NULL,
    date TEXT NOT NULL,
    time TEXT,
    url TEXT UNIQUE
)
"""

RACES_INSERT = """INSERT INTO races VALUES (
    :raceId,
    :year,
    :round,
    :circuitId,
    :name,
    :date,
    :time,
    :url
)
"""

RESULTS_CREATE = """CREATE TABLE results (
    resultId INTEGER PRIMARY KEY,
    raceId INTEGER NOT NULL,
    driverId INTEGER NOT NULL,
    constructorId INTEGER NOT NULL,
    number INTEGER,
    grid INTEGER NOT NULL,
    position INTEGER,
    positionText TEXT NOT NULL,
    positionOrder INTEGER NOT NULL,
    points REAL NOT NULL,
    laps INTEGER NOT NULL,
    time TEXT,
    milliseconds INTEGER,
    fastestLap INTEGER,
    rank INTEGER,
    fastestLapTime TEXT,
    fastestLapSpeed TEXT,
    statusId INTEGER NOT NULL
)"""

RESULTS_INSERT = """INSERT INTO results VALUES (
    :resultId,
    :raceId,
    :driverId,
    :constructorId,
    :number,
    :grid,
    :position,
    :positionText,
    :positionOrder,
    :points,
    :laps,
    :time,
    :milliseconds,
    :fastestLap,
    :rank,
    :fastestLapTime,
    :fastestLapSpeed,
    :statusId
)
"""

SEASONS_CREATE = """CREATE TABLE seasons (
    year INTEGER PRIMARY KEY,
    url TEXT NOT NULL
)
"""

SEASONS_INSERT = """INSERT INTO seasons VALUES (
    :year,
    :url
)
"""

SPRINT_RESULTS_CREATE = """CREATE TABLE sprint_results (
    resultId INTEGER PRIMARY KEY,
    raceId INTEGER NOT NULL,
    driverId INTEGER NOT NULL,
    constructorId INTEGER NOT NULL,
    number INTEGER,
    grid INTEGER NOT NULL,
    position INTEGER,
    positionText TEXT NOT NULL,
    positionOrder INTEGER NOT NULL,
    points REAL NOT NULL,
    laps INTEGER NOT NULL,
    time TEXT,
    milliseconds INTEGER,
    fastestLap INTEGER,
    fastestLapTime TEXT,
    statusId INTEGER NOT NULL
)
"""

SPRINT_RESULTS_INSERT = """INSERT INTO sprint_results VALUES (
    :resultId,
    :raceId,
    :driverId,
    :constructorId,
    :number,
    :grid,
    :position,
    :positionText,
    :positionOrder,
    :points,
    :laps,
    :time,
    :milliseconds,
    :fastestLap,
    :fastestLapTime,
    :statusId
)
"""

STATUS_CREATE = """CREATE TABLE status (
    statusId INTEGER PRIMARY KEY,
    status TEXT
)
"""

STATUS_INSERT = """INSERT INTO status VALUES (
    :statusId,
    :status
)
"""


TABLE_MAP = {
    "circuits": (CIRCUITS_CREATE, CIRCUITS_INSERT),
    "constructor_results": (
        CONSTRUCTOR_RESULTS_CREATE,
        CONSTRUCTOR_RESULTS_INSERT,
    ),
    "constructor_standings": (
        CONSTRUCTOR_STANDINGS_CREATE,
        CONSTRUCTOR_STANDINGS_INSERT,
    ),
    "constructors": (CONSTRUCTORS_CREATE, CONSTRUCTORS_INSERT),
    "driver_standings": (DRIVER_STANDINGS_CREATE, DRIVER_STANDINGS_INSERT),
    "drivers": (DRIVERS_CREATE, DRIVERS_INSERT),
    "lap_times": (LAP_TIMES_CREATE, LAP_TIMES_INSERT),
    "pit_stops": (PIT_STOPS_CREATE, PIT_STOPS_INSERT),
    "qualifying": (QUALIFYING_CREATE, QUALIFYING_INSERT),
    "races": (RACES_CREATE, RACES_INSERT),
    "results": (RESULTS_CREATE, RESULTS_INSERT),
    "seasons": (SEASONS_CREATE, SEASONS_INSERT),
    "sprint_results": (SPRINT_RESULTS_CREATE, SPRINT_RESULTS_INSERT),
    "status": (STATUS_CREATE, STATUS_INSERT),
}


def clean_null_values(row: dict) -> dict:
    """Clean NULL values from the dictionary.

    NULL cells in the CSV files are filled with "\\N". This function removes
    them from the dictionary.
    """
    return {k: v if v != "\\N" else None for k, v in row.items()}


def import_table(con: Connection, name: str, content: csv.DictReader) -> None:
    """Create the schema based on the name."""
    if name not in TABLE_MAP:
        click.secho(f'Schema for "{name}" not found.', fg="bright_red")
        return

    cur = con.cursor()
    click.echo(f'Creating "{name}" table.')
    create_sql, insert_sql = TABLE_MAP[name]
    cur.execute(f"DROP TABLE IF EXISTS {name}")
    cur.execute(create_sql)
    for row in content:
        try:
            cur.execute(insert_sql, clean_null_values(row))
        except ProgrammingError as exc:
            click.secho(f"{exc}:\nRow Content: {row}", fg="bright_red")
            return

    con.commit()
