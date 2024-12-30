from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/contrast

class Contrast(TailwindEnum):
    """
    Utilities for applying contrast filters to an element.

    Attributes:
    CONTRAST (str): Base class for contrast utilities. Available intensity values: 
    [0, 50, 75, 100, 125, 150, 200].
    """

    CONTRAST = "contrast"

class Contrasts(TailwindDict):
    pass