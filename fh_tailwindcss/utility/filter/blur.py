from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/blur

class Blur(TailwindEnum):
    """
    Utilities for applying blur filters to an element.

    Attributes:
    NONE (str): No blur applied.
    SM (str): Applies a small blur (4px).
    DEFAULT (str): Applies a default blur (8px).
    MD (str): Applies a medium blur (12px).
    LG (str): Applies a large blur (16px).
    XL (str): Applies an extra-large blur (24px).
    XXL (str): Applies a double extra-large blur (40px).
    XXXL (str): Applies a triple extra-large blur (64px).
    """

    NONE = "blur-none"
    SM = "blur-sm"
    DEFAULT = "blur"
    MD = "blur-md"
    LG = "blur-lg"
    XL = "blur-xl"
    XXL = "blur-2xl"
    XXXL = "blur-3xl"