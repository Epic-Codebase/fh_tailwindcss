from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/invert

class Invert(TailwindEnum):
    """
    Utilities for applying invert filters to an element.

    Attributes:
        INVERT_0 (str): Applies no invert filter.
        INVERT (str): Applies a full invert filter.
    """

    INVERT_0 = "invert-0"
    INVERT = "invert"
