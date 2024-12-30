from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/saturate

class Saturate(TailwindEnum):
    """
    Utilities for applying saturation filters to an element.

    Attributes:
        SATURATE (str): Applies a saturation filter. Available percentages: [0, 50, 100, 150, 200].
    """

    SATURATE = "saturate"

class SaturateValues(TailwindDict):
    pass
