from ...tailwind import TailwindEnum

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
    """
    BORDER_TRANSPARENT = "border-transparent"
    BORDER_BLACK = "border-black"
    BORDER_WHITE = "border-white"
    BORDER_GRAY = "border-gray-*"
    BORDER_RED = "border-red-*"
    BORDER_BLUE = "border-blue-*"
    BORDER_GREEN = "border-green-*"
    BORDER_YELLOW = "border-yellow-*"