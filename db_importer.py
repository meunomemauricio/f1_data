"""Import data from the Ergast CSVs into a SQLite database."""

import click


@click.command()
@click.option(
    "-i",
    "--input",
    type=click.Path(file_okay=True, exists=True, dir_okay=False),
)
@click.option(
    "-o",
    "--output",
    type=click.Path(file_okay=False, exists=False, dir_okay=True),
)
def run(input: str, output: str):
    """"""
    print(input)
    print(output)


if __name__ == "__main__":
    run()
