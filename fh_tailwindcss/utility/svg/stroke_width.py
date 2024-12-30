from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/stroke-width

class StrokeWidth(TailwindEnum):
    """
    Utilities for styling the stroke width of SVG elements.

    Attributes:
        ZERO (str): Represents `stroke-0` for a stroke width of 0.
        ONE (str): Represents `stroke-1` for a stroke width of 1.
        TWO (str): Represents `stroke-2` for a stroke width of 2.
    """

    ZERO = "stroke-0"
    ONE = "stroke-1"
    TWO = "stroke-2"
