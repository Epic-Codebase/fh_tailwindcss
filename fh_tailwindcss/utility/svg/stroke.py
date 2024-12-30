from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/stroke

class Stroke(TailwindEnum):
    """
    Utilities for styling the stroke of SVG elements.

    Attributes:
        NONE (str): Represents `stroke-none` for no stroke.
        INHERIT (str): Represents `stroke-inherit` for inheriting the stroke value.
        CURRENT (str): Represents `stroke-current` to use the current color for the stroke.
        TRANSPARENT (str): Represents `stroke-transparent` for a transparent stroke.
        BLACK (str): Represents `stroke-black` for a black stroke.
        WHITE (str): Represents `stroke-white` for a white stroke.
        SLATE (str): Represents `stroke-slate` for slate color strokes.
        GRAY (str): Represents `stroke-gray` for gray color strokes.
        ZINC (str): Represents `stroke-zinc` for zinc color strokes.
        NEUTRAL (str): Represents `stroke-neutral` for neutral color strokes.
        STONE (str): Represents `stroke-stone` for stone color strokes.
        RED (str): Represents `stroke-red` for red color strokes.
        ORANGE (str): Represents `stroke-orange` for orange color strokes.
        AMBER (str): Represents `stroke-amber` for amber color strokes.
        YELLOW (str): Represents `stroke-yellow` for yellow color strokes.
        LIME (str): Represents `stroke-lime` for lime color strokes.
        GREEN (str): Represents `stroke-green` for green color strokes.
        EMERALD (str): Represents `stroke-emerald` for emerald color strokes.
        TEAL (str): Represents `stroke-teal` for teal color strokes.
        CYAN (str): Represents `stroke-cyan` for cyan color strokes.
        SKY (str): Represents `stroke-sky` for sky color strokes.
        BLUE (str): Represents `stroke-blue` for blue color strokes.
        INDIGO (str): Represents `stroke-indigo` for indigo color strokes.
        VIOLET (str): Represents `stroke-violet` for violet color strokes.
        PURPLE (str): Represents `stroke-purple` for purple color strokes.
        FUCHSIA (str): Represents `stroke-fuchsia` for fuchsia color strokes.
        PINK (str): Represents `stroke-pink` for pink color strokes.
        ROSE (str): Represents `stroke-rose` for rose color strokes.
    """

    NONE = "stroke-none"
    INHERIT = "stroke-inherit"
    CURRENT = "stroke-current"
    TRANSPARENT = "stroke-transparent"
    BLACK = "stroke-black"
    WHITE = "stroke-white"
    SLATE = "stroke-slate"
    GRAY = "stroke-gray"
    ZINC = "stroke-zinc"
    NEUTRAL = "stroke-neutral"
    STONE = "stroke-stone"
    RED = "stroke-red"
    ORANGE = "stroke-orange"
    AMBER = "stroke-amber"
    YELLOW = "stroke-yellow"
    LIME = "stroke-lime"
    GREEN = "stroke-green"
    EMERALD = "stroke-emerald"
    TEAL = "stroke-teal"
    CYAN = "stroke-cyan"
    SKY = "stroke-sky"
    BLUE = "stroke-blue"
    INDIGO = "stroke-indigo"
    VIOLET = "stroke-violet"
    PURPLE = "stroke-purple"
    FUCHSIA = "stroke-fuchsia"
    PINK = "stroke-pink"
    ROSE = "stroke-rose"

class Strokes(TailwindDict):
    pass