"""Helper methods and complementary data."""

from typing import NamedTuple


class DriverColorStyle(NamedTuple):
    """Represents a matplotlib Color/Style pair."""

    color: str
    style: str


# 2021 F1 Team Color Hex Codes, seems in TV Graphics and the F1 site.
# Source: https://redd.it/lfpyfp
# Team Names match the ones in the `constructors` DB table
TEAM_COLORS = {
    "Alfa Romeo": "#900000",
    "AlphaTauri": "#2B4562",
    "Alpine F1 Team": "#0090FF",
    "Aston Martin": "#006F62",
    "Ferrari": "#DC0000",
    "Haas F1 Team": "#FFFFFF",
    "McLaren": "#FF8700",
    "Mercedes": "#00D2BE",
    "Red Bull": "#0600EF",
    "Williams": "#005AFF",
}


# Styles are based on the Driver's T Cam colors:
#   - Black: Solid line,
#   - Yellow: Dashed line.
DRIVER_COLORS_2022 = {
    "ALB": DriverColorStyle("#005AFF", "-"),
    "ALO": DriverColorStyle("#0090FF", "-"),
    "BOT": DriverColorStyle("#900000", "-"),
    "GAS": DriverColorStyle("#2B4562", "-"),
    "HAM": DriverColorStyle("#00D2BE", "-."),
    "HUL": DriverColorStyle("#006F62", "-."),
    "LAT": DriverColorStyle("#005AFF", "-."),
    "LEC": DriverColorStyle("#DC0000", "-"),
    "MAG": DriverColorStyle("#FFFFFF", "-"),
    "MSC": DriverColorStyle("#FFFFFF", "-."),
    "NOR": DriverColorStyle("#FF8700", "-."),
    "OCO": DriverColorStyle("#0090FF", "-."),
    "PER": DriverColorStyle("#0600EF", "-."),
    "RIC": DriverColorStyle("#FF8700", "-"),
    "RUS": DriverColorStyle("#00D2BE", "-"),
    "SAI": DriverColorStyle("#DC0000", "-."),
    "STR": DriverColorStyle("#006F62", "-"),
    "TSU": DriverColorStyle("#2B4562", "-."),
    "VER": DriverColorStyle("#0600EF", "-"),
    "VET": DriverColorStyle("#006F62", "-."),
    "ZHO": DriverColorStyle("#900000", "-."),
}
