from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/border-collapse

class BorderCollapse(TailwindEnum):
    """
    Utilities for controlling whether table borders should collapse or be separated.

    Attributes:
        COLLAPSE (str): Sets table borders to collapse.
        SEPARATE (str): Sets table borders to be separated.
    """

    COLLAPSE = "border-collapse"
    SEPARATE = "border-separate"
