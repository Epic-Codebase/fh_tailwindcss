from ...tailwind import TailwindEnum, TailwindDict

# https://tailwindcss.com/docs/border-color

class BorderColor(TailwindEnum):
    """
    Enum class representing border-color utility classes in Tailwind CSS.
    Used to control the color of borders.

    Attributes:
        BORDER_TRANSPARENT (str): Transparent border color.
        BORDER_BLACK (str): Black border color.
        BORDER_WHITE (str): White border color.
        BORDER_GRAY (str): Gray border color (varies by shade).
        BORDER_RED (str): Red border color (varies by shade).
        BORDER_BLUE (str): Blue border color (varies by shade).
        BORDER_GREEN (str): Green border color (varies by shade).
        BORDER_YELLOW (str): Yellow border color (varies by shade).
        BORDER_PURPLE (str): Purple border color (varies by shade).
        BORDER_PINK (str): Pink border color (varies by shade).
        BORDER_INDIGO (str): Indigo border color (varies by shade).
        BORDER_TEAL (str): Teal border color (varies by shade).
        BORDER_CYAN (str): Cyan border color (varies by shade).
        BORDER_LIME (str): Lime border color (varies by shade).
        BORDER_AMBER (str): Amber border color (varies by shade).
        BORDER_FUCHSIA (str): Fuchsia border color (varies by shade).
        BORDER_ROSE (str): Rose border color (varies by shade).
    """
    BORDER_TRANSPARENT = "border-transparent"
    BORDER_BLACK = "border-black"
    BORDER_WHITE = "border-white"
    BORDER_GRAY = "border-gray"
    BORDER_RED = "border-red"
    BORDER_BLUE = "border-blue"
    BORDER_GREEN = "border-green"
    BORDER_YELLOW = "border-yellow"
    BORDER_PURPLE = "border-purple"
    BORDER_PINK = "border-pink"
    BORDER_INDIGO = "border-indigo"
    BORDER_TEAL = "border-teal"
    BORDER_CYAN = "border-cyan"
    BORDER_LIME = "border-lime"
    BORDER_AMBER = "border-amber"
    BORDER_FUCHSIA = "border-fuchsia"
    BORDER_ROSE = "border-rose"


class BorderColors(TailwindDict):
    """
    A class representing the border colors utility in Tailwind CSS.
    """
    pass