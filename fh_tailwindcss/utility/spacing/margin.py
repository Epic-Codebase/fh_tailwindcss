from ...tailwind import TailwindEnum, TailwindDict

# https://tailwindcss.com/docs/margin

class Margin(TailwindEnum):
    """
    Enum class representing different margin utilities for Tailwind CSS.

    Attributes:
        DEFAULT (str): Applies margin on all sides.
        TOP (str): Applies margin to the top side.
        BOTTOM (str): Applies margin to the bottom side.
        LEFT (str): Applies margin to the left side.
        RIGHT (str): Applies margin to the right side.
        HORIZONTAL (str): Applies margin to the left and right sides.
        VERTICAL (str): Applies margin to the top and bottom sides.
        INLINE_START (str): Applies margin to the inline start side.
        INLINE_END (str): Applies margin to the inline end side.
        AUTO (str): Applies auto margin on all sides.
        HORIZONTAL_AUTO (str): Applies auto margin to the left and right sides.
        VERTICAL_AUTO (str): Applies auto margin to the top and bottom sides.
        INLINE_START_AUTO (str): Applies auto margin to the inline start side.
        INLINE_END_AUTO (str): Applies auto margin to the inline end side.
    """
    DEFAULT = "m"
    TOP = "mt"
    BOTTOM = "mb"
    LEFT = "ml"
    RIGHT = "mr"
    HORIZONTAL = "mx"
    VERTICAL = "my"
    INLINE_START = "ms"
    INLINE_END = "me"
    AUTO = "m-auto"
    HORIZONTAL_AUTO = "mx-auto"
    VERTICAL_AUTO = "my-auto"
    INLINE_START_AUTO = "ms-auto"
    INLINE_END_AUTO = "me-auto"



class Margins(TailwindDict, dict[Margin, int]):
    """
    A dictionary that holds the margin(Margin:int) values for a TailwindCSS component.
    """
    pass