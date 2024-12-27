from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/translate

class Translate(TailwindEnum):
    """
    Utilities for translating elements with transform.

    Attributes:
        X (str): Horizontal translation. Available options: [0, px, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96, 1/2, 1/3, 2/3, 1/4, 2/4, 3/4, full].
        Y (str): Vertical translation. Available options: [0, px, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96, 1/2, 1/3, 2/3, 1/4, 2/4, 3/4, full].
    """

    X = "translate-x"
    Y = "translate-y"

class TranslateValues(TailwindDict):
    pass