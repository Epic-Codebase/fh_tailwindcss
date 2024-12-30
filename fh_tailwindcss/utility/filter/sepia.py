from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/sepia

class Sepia(TailwindEnum):
    """
    Utilities for applying sepia filters to an element.

    Attributes:
        SEPIA_0 (str): Applies no sepia filter.
        SEPIA (str): Applies a sepia filter.
    """

    SEPIA_0 = "sepia-0"
    SEPIA = "sepia"