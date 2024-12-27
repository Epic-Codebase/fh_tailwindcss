from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/transform-origin

class TransformOrigin(TailwindEnum):
    """
    Utilities for specifying the origin for an element's transformations.

    Attributes:
        CENTER (str): Center origin. 
        TOP (str): Top origin. 
        TOP_RIGHT (str): Top-right origin.
        RIGHT (str): Right origin.
        BOTTOM_RIGHT (str): Bottom-right origin.
        BOTTOM (str): Bottom origin.
        BOTTOM_LEFT (str): Bottom-left origin.
        LEFT (str): Left origin.
        TOP_LEFT (str): Top-left origin.
    """

    CENTER = "origin-center"
    TOP = "origin-top"
    TOP_RIGHT = "origin-top-right"
    RIGHT = "origin-right"
    BOTTOM_RIGHT = "origin-bottom-right"
    BOTTOM = "origin-bottom"
    BOTTOM_LEFT = "origin-bottom-left"
    LEFT = "origin-left"
    TOP_LEFT = "origin-top-left"
