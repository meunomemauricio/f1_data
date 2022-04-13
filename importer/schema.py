"""SQL Statements for importing CSV data."""

CIRCUITS_CREATE = """CREATE TABLE circuits (
    circuitId INTEGER,
    circuitRef TEXT,
    name TEXT,
    country TEXT,
    lat REAL,
    lng REAL,
    alt INTEGER,
    url TEXT
)
"""

CIRCUITS_INSERT = """INSERT INTO circuits VALUES (
    :circuitId,
    :circuitRef,
    :name,
    :country,
    :lat,
    :lng,
    :alt,
    :url
)
"""
