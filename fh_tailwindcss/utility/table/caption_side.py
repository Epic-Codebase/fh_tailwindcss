from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/caption-side

class CaptionSide(TailwindEnum):
    """
    Utilities for controlling the alignment of a caption element inside a table.

    Attributes:
        TOP (str): Aligns the caption to the top of the table.
        BOTTOM (str): Aligns the caption to the bottom of the table.
    """

    TOP = "caption-top"
    BOTTOM = "caption-bottom"
