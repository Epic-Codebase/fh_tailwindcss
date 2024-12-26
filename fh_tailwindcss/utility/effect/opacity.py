from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/opacity

class Opacity(TailwindEnum):
    """
    Utilities for controlling the opacity of an element.

    Attributes:
    OPACITY (str): Base class for opacity utilities. Available intensity values: 
    [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100].
    """

    OPACITY = "opacity"

class Opacities(TailwindDict):
    pass