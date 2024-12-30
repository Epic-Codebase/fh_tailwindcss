from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/drop-shadow

class DropShadow(TailwindEnum):
    """
    Utilities for applying drop-shadow filters to an element.

    Attributes:
    SM (str): Applies a small drop-shadow.
    DEFAULT (str): Applies a default drop-shadow.
    MD (str): Applies a medium drop-shadow.
    LG (str): Applies a large drop-shadow.
    XL (str): Applies an extra-large drop-shadow.
    TWO_XL (str): Applies a 2x extra-large drop-shadow.
    NONE (str): No drop-shadow applied.
    """

    SM = "drop-shadow-sm"
    DEFAULT = "drop-shadow"
    MD = "drop-shadow-md"
    LG = "drop-shadow-lg"
    XL = "drop-shadow-xl"
    TWO_XL = "drop-shadow-2xl"
    NONE = "drop-shadow-none"