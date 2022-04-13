"""Import data from the Ergast CSVs into a SQLite database."""
import csv
import sqlite3
from io import TextIOWrapper
from zipfile import ZipFile

import click

from importer.tables import create_table


@click.command()
@click.option(
    "-i",
    "--input_file",
    type=click.Path(dir_okay=False, file_okay=True, exists=True),
    default="data/f1db_csv.zip",
)
@click.option(
    "-o",
    "--output",
    type=click.Path(dir_okay=False, file_okay=True),
    default="data/f1data.sqlite",
)
def run(input_file: str, output: str):
    con = sqlite3.connect(output)
    with ZipFile(input_file) as input_zip:
        for name in input_zip.namelist():
            with input_zip.open(name) as csv_fd:
                reader = csv.DictReader(TextIOWrapper(csv_fd, "utf-8"))
                create_table(con=con, name=name, content=reader)

    con.close()


if __name__ == "__main__":
    run()