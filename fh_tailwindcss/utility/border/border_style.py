from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/border-style

class BorderStyle(TailwindEnum):
    """
    Enum class representing border-style utility classes in Tailwind CSS.
    Used to control the style of borders.

    Attributes:
        BORDER_SOLID (str): Solid border style.
        BORDER_DASHED (str): Dashed border style.
        BORDER_DOTTED (str): Dotted border style.
        BORDER_DOUBLE (str): Double border style.
        BORDER_NONE (str): No border style.
    """
    BORDER_SOLID = "border-solid"
    BORDER_DASHED = "border-dashed"
    BORDER_DOTTED = "border-dotted"
    BORDER_DOUBLE = "border-double"
    BORDER_NONE = "border-none"