from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/padding

class Padding(TailwindEnum):
    """
    An enumeration representing different types of padding in Tailwind CSS.

    Attributes:
        DEFAULT (str): Applies padding on all sides.
        TOP (str): Applies padding at the top.
        RIGHT (str): Applies padding at the right.
        BOTTOM (str): Applies padding at the bottom.
        LEFT (str): Applies padding at the left.
        HORIZONTAL (str): Applies horizontal padding (left and right).
        VERTICAL (str): Applies vertical padding (top and bottom).
        INLINE_START (str): Applies inline start padding.
        INLINE_END (str): Applies inline end padding.
    """
    DEFAULT = "p"
    TOP = "pt"
    RIGHT = "pr"
    BOTTOM = "pb"
    LEFT = "pl"
    HORIZONTAL = "px"
    VERTICAL = "py"
    INLINE_START = "ps"
    INLINE_END = "pe"
    

class Paddings(TailwindDict, dict[Padding, int]):
    """
    A dictionary that holds the padding(Padding:int) values for a TailwindCSS component.
    """
    pass
    
