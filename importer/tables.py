import csv
from pathlib import Path
from sqlite3 import Connection, Cursor

import click

from importer.schema import CIRCUITS_CREATE, CIRCUITS_INSERT


def _create_circuits(cur: Cursor, content: csv.DictReader):
    """Create and fill the Circuits table."""
    cur.execute("DROP TABLE IF EXISTS circuits")
    cur.execute(CIRCUITS_CREATE)
    for row in content:
        cur.execute(CIRCUITS_INSERT, row)


TABLE_MAP = {
    "circuits": _create_circuits,
    # "constructor_results",
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


def create_table(con: Connection, name: str, content: csv.DictReader) -> None:
    """Create the schema based on the name."""
    path = Path(name)
    click.echo(f'Creating "{path.stem}" table.')
    routine = TABLE_MAP.get(path.stem)
    if routine:
        routine(cur=con.cursor(), content=content)
        con.commit()
