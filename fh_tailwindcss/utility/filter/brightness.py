from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/brightness

class Brightness(TailwindEnum):
    """
    Utilities for applying brightness filters to an element.

    Attributes:
    BRIGHTNESS (str): Base class for brightness utilities. Available intensity values: 
    [0, 50, 75, 90, 95, 100, 105, 110, 125, 150, 200].
    """

    BRIGHTNESS = "brightness"

class Brightnesses(TailwindDict):
    pass