from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/caret-color

class CaretColor(TailwindEnum):
    """
    Utilities for controlling the color of the text input cursor.

    Attributes:
        INHERIT (str): Uses the parent element's caret color.
        CURRENT (str): Sets the caret color to the current text color.
        TRANSPARENT (str): Makes the caret color fully transparent.
        BLACK (str): Applies the black color (#000).
        WHITE (str): Applies the white color (#fff).
        SLATE (str): Accepts shades 50-950 for slate tones (e.g., #f8fafc for 50).
        GRAY (str): Accepts shades 50-950 for gray tones (e.g., #f9fafb for 50).
        ZINC (str): Accepts shades 50-950 for zinc tones (e.g., #fafafa for 50).
        NEUTRAL (str): Accepts shades 50-950 for neutral tones (e.g., #fafafa for 50).
        STONE (str): Accepts shades 50-950 for stone tones (e.g., #fafaf9 for 50).
        RED (str): Accepts shades 50-950 for red tones (e.g., #fef2f2 for 50).
        ORANGE (str): Accepts shades 50-950 for orange tones (e.g., #fff7ed for 50).
        AMBER (str): Accepts shades 50-950 for amber tones (e.g., #fffbeb for 50).
        YELLOW (str): Accepts shades 50-950 for yellow tones (e.g., #fefce8 for 50).
        LIME (str): Accepts shades 50-950 for lime tones (e.g., #f7fee7 for 50).
        GREEN (str): Accepts shades 50-950 for green tones (e.g., #f0fdf4 for 50).
        EMERALD (str): Accepts shades 50-950 for emerald tones (e.g., #ecfdf5 for 50).
        TEAL (str): Accepts shades 50-950 for teal tones (e.g., #f0fdfa for 50).
        CYAN (str): Accepts shades 50-950 for cyan tones (e.g., #ecfeff for 50).
        SKY (str): Accepts shades 50-950 for sky tones (e.g., #f0f9ff for 50).
        BLUE (str): Accepts shades 50-950 for blue tones (e.g., #eff6ff for 50).
        INDIGO (str): Accepts shades 50-950 for indigo tones (e.g., #eef2ff for 50).
        VIOLET (str): Accepts shades 50-950 for violet tones (e.g., #f5f3ff for 50).
        PURPLE (str): Accepts shades 50-950 for purple tones (e.g., #faf5ff for 50).
        FUCHSIA (str): Accepts shades 50-950 for fuchsia tones (e.g., #fdf4ff for 50).
        PINK (str): Accepts shades 50-950 for pink tones (e.g., #fdf2f8 for 50).
        ROSE (str): Accepts shades 50-950 for rose tones (e.g., #fff1f2 for 50).
    """
    INHERIT = "caret-inherit"
    CURRENT = "caret-current"
    TRANSPARENT = "caret-transparent"
    BLACK = "caret-black"
    WHITE = "caret-white"
    SLATE = "caret-slate"
    GRAY = "caret-gray"
    ZINC = "caret-zinc"
    NEUTRAL = "caret-neutral"
    STONE = "caret-stone"
    RED = "caret-red"
    ORANGE = "caret-orange"
    AMBER = "caret-amber"
    YELLOW = "caret-yellow"
    LIME = "caret-lime"
    GREEN = "caret-green"
    EMERALD = "caret-emerald"
    TEAL = "caret-teal"
    CYAN = "caret-cyan"
    SKY = "caret-sky"
    BLUE = "caret-blue"
    INDIGO = "caret-indigo"
    VIOLET = "caret-violet"
    PURPLE = "caret-purple"
    FUCHSIA = "caret-fuchsia"
    PINK = "caret-pink"
    ROSE = "caret-rose"

class CaretColors(TailwindDict):
    pass