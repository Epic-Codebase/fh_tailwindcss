from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/border-spacing

class BorderSpacing(TailwindEnum):
    """
    Utilities for controlling the spacing between table borders.

    Attributes:
        SPACING (str): Sets uniform border spacing. Available options: [0, px, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96].
        SPACING_X (str): Sets horizontal border spacing. Available options: [0, px, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96].
        SPACING_Y (str): Sets vertical border spacing. Available options: [0, px, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96].
    """

    SPACING = "border-spacing"
    SPACING_X = "border-spacing-x"
    SPACING_Y = "border-spacing-y"

class BorderSpacings(TailwindDict):
    pass
