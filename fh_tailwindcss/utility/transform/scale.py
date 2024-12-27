from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/scale

class Scale(TailwindEnum):
    """
    Utilities for scaling elements with transform.

    Attributes:
        SCALE (str): Scales an element. Available options: [0, 50, 75, 90, 95, 100, 105, 110, 125, 150].
        SCALE_X (str): Scales an element along the X axis. Available options: [0, 50, 75, 90, 95, 100, 105, 110, 125, 150].
        SCALE_Y (str): Scales an element along the Y axis. Available options: [0, 50, 75, 90, 95, 100, 105, 110, 125, 150].
    """

    SCALE = "scale"
    SCALE_X = "scale-x"
    SCALE_Y = "scale-y"

class ScaleValues(TailwindDict):
    pass