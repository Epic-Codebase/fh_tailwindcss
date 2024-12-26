from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/hue-rotate

class HueRotate(TailwindEnum):
    """
    Utilities for applying hue-rotate filters to an element.

    Attributes:
        HUE_ROTATE (str): Applies a hue-rotate filter. Available degrees: [0, 15, 30, 60, 90, 180].
    """

    HUE_ROTATE = "hue-rotate"

class HueRotateDegrees(TailwindDict):
    pass