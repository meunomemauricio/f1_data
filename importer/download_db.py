import shutil
import urllib.request
from pathlib import Path

import click

URL = "https://ergast.com/downloads/f1db_csv.zip"


@click.command()
@click.option(
    "-o",
    "--output",
    type=click.Path(dir_okay=True, file_okay=True),
    default="data/f1db_csv.zip",
)
def run(output: str) -> None:
    """Download the Ergast CSV files into the specified folder."""
    path = Path(output)
    if path.is_dir():
        path = path / "f1db_csv.zip"

    click.echo(f"Downloading the Ergast CSV files to {path}.")
    with urllib.request.urlopen(URL) as response, path.open("wb") as out_file:
        shutil.copyfileobj(response, out_file)


if __name__ == "__main__":
    run()
