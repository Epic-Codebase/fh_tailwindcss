from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/transition-property

class TransitionProperty(TailwindEnum):
    """
    Utilities for controlling which CSS properties transition.

    Attributes:
        NONE (str): Disables all transitions.
        ALL (str): Applies transitions to all properties.
        DEFAULT (str): Applies default transitions to common properties like color, background-color, and transform.
        COLORS (str): Applies transitions to color-related properties.
        OPACITY (str): Applies transitions to opacity.
        SHADOW (str): Applies transitions to box-shadow.
        TRANSFORM (str): Applies transitions to transform.
    """

    NONE = "transition-none"
    ALL = "transition-all"
    DEFAULT = "transition"
    COLORS = "transition-colors"
    OPACITY = "transition-opacity"
    SHADOW = "transition-shadow"
    TRANSFORM = "transition-transform"
