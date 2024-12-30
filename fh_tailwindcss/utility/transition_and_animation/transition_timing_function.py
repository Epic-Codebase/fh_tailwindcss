from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/transition-timing-function

class TransitionTimingFunction(TailwindEnum):
    """
    Utilities for controlling the easing of CSS transitions.

    Attributes:
        LINEAR (str): Applies a linear easing function.
        IN (str): Applies an "ease-in" cubic-bezier easing function.
        OUT (str): Applies an "ease-out" cubic-bezier easing function.
        IN_OUT (str): Applies an "ease-in-out" cubic-bezier easing function.
    """

    LINEAR = "ease-linear"
    IN = "ease-in"
    OUT = "ease-out"
    IN_OUT = "ease-in-out"
