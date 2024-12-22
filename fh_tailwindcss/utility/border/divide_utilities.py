from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/divide-width

class DivideUtilities(TailwindEnum):
    """
    Enum class representing divide utility classes in Tailwind CSS.
    Used to control the appearance of dividers between elements.

    Attributes:
        DIVIDE_X (str): Horizontal dividers.
        DIVIDE_Y (str): Vertical dividers.
        DIVIDE_TRANSPARENT (str): Transparent divider color.
        DIVIDE_CURRENT (str): Current color divider.
        DIVIDE_GRAY (str): Gray divider (varies by shade).
        DIVIDE_DASHED (str): Dashed dividers.
        DIVIDE_NONE (str): No dividers.
    """
    DIVIDE_X = "divide-x"
    DIVIDE_Y = "divide-y"
    DIVIDE_TRANSPARENT = "divide-transparent"
    DIVIDE_CURRENT = "divide-current"
    DIVIDE_GRAY = "divide-gray-*"
    DIVIDE_DASHED = "divide-dashed"
    DIVIDE_NONE = "divide-none"