from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/font-weight

class FontWeight(TailwindEnum):
    """
    Enum class representing different font sizes with their corresponding Tailwind CSS classes.

    Attributes:
        THIN (str): Represents the 'font-thin' Tailwind CSS class with font-weight 100 (Thin).
        EXTRALIGHT (str): Represents the 'font-extralight' Tailwind CSS class with font-weight 200 (Extra Light).
        LIGHT (str): Represents the 'font-light' Tailwind CSS class with font-weight 300 (Light).
        NORMAL (str): Represents the 'font-normal' Tailwind CSS class with font-weight 400 (Normal).
        MEDIUM (str): Represents the 'font-medium' Tailwind CSS class with font-weight 500 (Medium).
        SEMIBOLD (str): Represents the 'font-semibold' Tailwind CSS class with font-weight 600 (Semi-Bold).
        BOLD (str): Represents the 'font-bold' Tailwind CSS class with font-weight 700 (Bold).
        EXTRABOLD (str): Represents the 'font-extrabold' Tailwind CSS class with font-weight 800 (Extra Bold).
        BLACK (str): Represents the 'font-black' Tailwind CSS class with font-weight 900 (Black).
    """
    THIN = 'font-thin'
    EXTRALIGHT = 'font-extralight'
    LIGHT = 'font-light'
    NORMAL = 'font-normal'
    MEDIUM = 'font-medium'
    SEMIBOLD = 'font-semibold'
    BOLD = 'font-bold'
    EXTRABOLD = 'font-extrabold'
    BLACK = 'font-black'
