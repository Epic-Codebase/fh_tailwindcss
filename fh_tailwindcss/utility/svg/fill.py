from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/fill

from ...tailwind import TailwindEnum

class Fill(TailwindEnum):
    """
    Utilities for styling the fill of SVG elements.

    Attributes:
        NONE (str): No fill.
        INHERIT (str): Inherits the fill value from the parent element.
        CURRENT (str): Uses the current text color as the fill color.
        TRANSPARENT (str): Transparent fill.
        BLACK (str): Black fill (#000).
        WHITE (str): White fill (#fff).
        SLATE (str): Slate color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        GRAY (str): Gray color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        ZINC (str): Zinc color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        NEUTRAL (str): Neutral color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        STONE (str): Stone color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        RED (str): Red color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        ORANGE (str): Orange color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        AMBER (str): Amber color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        YELLOW (str): Yellow color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        LIME (str): Lime color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        GREEN (str): Green color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        EMERALD (str): Emerald color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        TEAL (str): Teal color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        CYAN (str): Cyan color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        SKY (str): Sky color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        BLUE (str): Blue color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        INDIGO (str): Indigo color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        VIOLET (str): Violet color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        PURPLE (str): Purple color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        FUCHSIA (str): Fuchsia color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        PINK (str): Pink color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
        ROSE (str): Rose color shades available in 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.
    """

    NONE = "fill-none"
    INHERIT = "fill-inherit"
    CURRENT = "fill-current"
    TRANSPARENT = "fill-transparent"
    BLACK = "fill-black"
    WHITE = "fill-white"
    SLATE = "fill-slate"
    GRAY = "fill-gray"
    ZINC = "fill-zinc"
    NEUTRAL = "fill-neutral"
    STONE = "fill-stone"
    RED = "fill-red"
    ORANGE = "fill-orange"
    AMBER = "fill-amber"
    YELLOW = "fill-yellow"
    LIME = "fill-lime"
    GREEN = "fill-green"
    EMERALD = "fill-emerald"
    TEAL = "fill-teal"
    CYAN = "fill-cyan"
    SKY = "fill-sky"
    BLUE = "fill-blue"
    INDIGO = "fill-indigo"
    VIOLET = "fill-violet"
    PURPLE = "fill-purple"
    FUCHSIA = "fill-fuchsia"
    PINK = "fill-pink"
    ROSE = "fill-rose"


class Fills(TailwindDict):
    pass