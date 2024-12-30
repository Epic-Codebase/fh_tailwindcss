from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/box-shadow-color

class BoxShadowColor(TailwindEnum):
    """
    Utilities for controlling the color of a box shadow.
    
    Attributes:
    INHERIT (str): Inherits the box shadow color.
    CURRENT (str): Sets the box shadow color to the current text color.
    TRANSPARENT (str): Makes the box shadow color transparent.
    BLACK (str): A solid black box shadow color.
    WHITE (str): A solid white box shadow color.
    SLATE (str): Shades of slate colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    GRAY (str): Shades of gray colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    ZINC (str): Shades of zinc colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    NEUTRAL (str): Shades of neutral colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    STONE (str): Shades of stone colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    RED (str): Shades of red colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    ORANGE (str): Shades of orange colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    AMBER (str): Shades of amber colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    YELLOW (str): Shades of yellow colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    LIME (str): Shades of lime colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    GREEN (str): Shades of green colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    EMERALD (str): Shades of emerald colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    TEAL (str): Shades of teal colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    CYAN (str): Shades of cyan colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    SKY (str): Shades of sky colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    BLUE (str): Shades of blue colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    INDIGO (str): Shades of indigo colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    VIOLET (str): Shades of violet colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    PURPLE (str): Shades of purple colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    FUCHSIA (str): Shades of fuchsia colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    PINK (str): Shades of pink colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    ROSE (str): Shades of rose colors. Available options: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950].
    """

    INHERIT = "shadow-inherit"
    CURRENT = "shadow-current"
    TRANSPARENT = "shadow-transparent"
    BLACK = "shadow-black"
    WHITE = "shadow-white"

    SLATE = "shadow-slate"
    GRAY = "shadow-gray"
    ZINC = "shadow-zinc"
    NEUTRAL = "shadow-neutral"
    STONE = "shadow-stone"
    RED = "shadow-red"
    ORANGE = "shadow-orange"
    AMBER = "shadow-amber"
    YELLOW = "shadow-yellow"
    LIME = "shadow-lime"
    GREEN = "shadow-green"
    EMERALD = "shadow-emerald"
    TEAL = "shadow-teal"
    CYAN = "shadow-cyan"
    SKY = "shadow-sky"
    BLUE = "shadow-blue"
    INDIGO = "shadow-indigo"
    VIOLET = "shadow-violet"
    PURPLE = "shadow-purple"
    FUCHSIA = "shadow-fuchsia"
    PINK = "shadow-pink"
    ROSE = "shadow-rose"

class BoxShadowColors(TailwindDict):
    pass