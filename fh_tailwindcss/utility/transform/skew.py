from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/skew

class Skew(TailwindEnum):
    """
    Utilities for skewing elements with transform.

    Attributes:
        X (str): Horizontal skew. Available options: [0, 1, 2, 3, 6, 12].
        Y (str): Vertical skew. Available options: [0, 1, 2, 3, 6, 12].
    """

    X = "skew-x"
    Y = "skew-y"

class SkewDegrees(TailwindDict):
    pass
