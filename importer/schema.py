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
    # "lap_times",
    # "pit_stops",
    # "qualifying",
    # "races",
    # "results",
    # "seasons",
    # "sprint_results",
    # "status",
}


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
        # TODO: Null values are comming as "\\N"
        try:
            cur.execute(insert_sql, row)
        except ProgrammingError as exc:
            click.secho(f"{exc}:\nRow Content: {row}")
            return

    con.commit()
