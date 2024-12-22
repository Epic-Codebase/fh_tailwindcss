from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/border-width

class BorderWidth(TailwindEnum):
    """
    Enum class representing border-width utility classes in Tailwind CSS.
    Used to control the width of borders.

    Attributes:
        BORDER (str): Default border width.
        BORDER_0 (str): No border.
        BORDER_2 (str): 2px border width.
        BORDER_4 (str): 4px border width.
        BORDER_8 (str): 8px border width.
        BORDER_X (str): Horizontal borders width.
        BORDER_Y (str): Vertical borders width.
    """
    BORDER = "border"
    BORDER_0 = "border-0"
    BORDER_2 = "border-2"
    BORDER_4 = "border-4"
    BORDER_8 = "border-8"
    BORDER_X = "border-x"
    BORDER_Y = "border-y"