"""Import data from the Ergast CSVs into a SQLite database."""
import csv
import sqlite3
from io import TextIOWrapper
from pathlib import Path
from zipfile import BadZipFile, ZipFile

import click

from importer.schema import import_table


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
    try:
        with ZipFile(input_file) as input_zip:
            for name in input_zip.namelist():
                with input_zip.open(name) as csv_fd:
                    reader = csv.DictReader(TextIOWrapper(csv_fd, "utf-8"))
                    path = Path(name)
                    import_table(con=con, name=path.stem, content=reader)
    except BadZipFile as exc:
        click.secho(f"Error while opening {input_file}: {exc}", fg="red")

    con.close()


if __name__ == "__main__":
    run()
