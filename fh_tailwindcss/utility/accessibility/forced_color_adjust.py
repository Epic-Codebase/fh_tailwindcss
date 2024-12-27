from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/forced-color-adjust

class ForcedColorAdjust(TailwindEnum):
    """
    Utilities for opting in and out of forced colors.

    Attributes:
        AUTO (str): Represents `forced-color-adjust-auto` to allow forced color adjustment.
        NONE (str): Represents `forced-color-adjust-none` to disable forced color adjustment.
    """

    AUTO = "forced-color-adjust-auto"
    NONE = "forced-color-adjust-none"
