from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/screen-readers

class ScreenReader(TailwindEnum):
    """
    Utilities for improving accessibility with screen readers.

    Attributes:
        SR_ONLY (str): Represents `sr-only` for making an element visually hidden but accessible to screen readers.
        NOT_SR_ONLY (str): Represents `not-sr-only` for making an element visible and accessible to both screen readers and users.
    """

    SR_ONLY = "sr-only"
    NOT_SR_ONLY = "not-sr-only"
