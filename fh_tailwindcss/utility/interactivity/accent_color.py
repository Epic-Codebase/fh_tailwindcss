from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/accent-color

class AccentColor(TailwindEnum):
    """
    Utilities for controlling the accent color of form controls.

    Attributes:
        INHERIT: Use the `inherit` keyword to inherit the accent color.
        CURRENT: Use the current color for the accent.
        TRANSPARENT: Make the accent color transparent.
        BLACK: Black accent color (no shades available).
        WHITE: White accent color (no shades available).
        SLATE: Slate accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        GRAY: Gray accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        ZINC: Zinc accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        NEUTRAL: Neutral accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        STONE: Stone accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        RED: Red accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        ORANGE: Orange accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        AMBER: Amber accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        YELLOW: Yellow accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        LIME: Lime accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        GREEN: Green accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        EMERALD: Emerald accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        TEAL: Teal accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        CYAN: Cyan accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        SKY: Sky accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        BLUE: Blue accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        INDIGO: Indigo accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        VIOLET: Violet accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        PURPLE: Purple accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        FUCHSIA: Fuchsia accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        PINK: Pink accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
        ROSE: Rose accent color with shades 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.
    """

    INHERIT = "accent-inherit"
    CURRENT = "accent-current"
    TRANSPARENT = "accent-transparent"
    BLACK = "accent-black"
    WHITE = "accent-white"

    SLATE = "accent-slate"
    GRAY = "accent-gray"
    ZINC = "accent-zinc"
    NEUTRAL = "accent-neutral"
    STONE = "accent-stone"
    RED = "accent-red"
    ORANGE = "accent-orange"
    AMBER = "accent-amber"
    YELLOW = "accent-yellow"
    LIME = "accent-lime"
    GREEN = "accent-green"
    EMERALD = "accent-emerald"
    TEAL = "accent-teal"
    CYAN = "accent-cyan"
    SKY = "accent-sky"
    BLUE = "accent-blue"
    INDIGO = "accent-indigo"
    VIOLET = "accent-violet"
    PURPLE = "accent-purple"
    FUCHSIA = "accent-fuchsia"
    PINK = "accent-pink"
    ROSE = "accent-rose"

class AccentColors(TailwindDict):
    pass
