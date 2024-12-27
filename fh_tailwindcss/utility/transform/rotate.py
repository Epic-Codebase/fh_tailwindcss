from ...tailwind import TailwindDict, TailwindEnum

class Rotate(TailwindEnum):
    """
    Utilities for rotating elements with transform.

    Attributes:
        ROTATE (str): Rotates an element. Available options: [0, 1, 2, 3, 6, 12, 45, 90, 180].
    """

    ROTATE = "rotate"

class RotateDegrees(TailwindDict):
    pass