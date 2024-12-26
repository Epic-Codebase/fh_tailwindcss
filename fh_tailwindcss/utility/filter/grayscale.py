from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/grayscale

class GrayScale(TailwindEnum):
    """
    Utilities for applying grayscale filters to an element.

    Attributes:
    GRAYSCALE_0 (str): No grayscale applied.
    GRAYSCALE (str): Applies full grayscale (100%).
    """

    GRAYSCALE_0 = "grayscale-0"
    GRAYSCALE = "grayscale"