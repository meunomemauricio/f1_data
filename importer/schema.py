"""SQL Statements for importing CSV data."""

import csv
from sqlite3 import Connection

import click

CIRCUITS_CREATE = """CREATE TABLE circuits (
    circuitId INTEGER PRIMARY KEY NOT NULL,
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
    constructorResultsId INTEGER PRIMARY KEY NOT NULL,
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

TABLE_MAP = {
    "circuits": (CIRCUITS_CREATE, CIRCUITS_INSERT),
    "constructor_results": (
        CONSTRUCTOR_RESULTS_CREATE,
        CONSTRUCTOR_RESULTS_INSERT,
    ),
    # "constructor_standings",
    # "constructors",
    # "driver_standings",
    # "drivers",
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
        cur.execute(insert_sql, row)

    con.commit()
