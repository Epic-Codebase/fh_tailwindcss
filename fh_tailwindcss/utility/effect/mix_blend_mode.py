from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/mix-blend-mode

class MixBlendMode(TailwindEnum):
    """
    Utilities for controlling how an element should blend with the background.

    Attributes:
    NORMAL (str): Sets the blend mode to normal.
    MULTIPLY (str): Sets the blend mode to multiply.
    SCREEN (str): Sets the blend mode to screen.
    OVERLAY (str): Sets the blend mode to overlay.
    DARKEN (str): Sets the blend mode to darken.
    LIGHTEN (str): Sets the blend mode to lighten.
    COLOR_DODGE (str): Sets the blend mode to color-dodge.
    COLOR_BURN (str): Sets the blend mode to color-burn.
    HARD_LIGHT (str): Sets the blend mode to hard-light.
    SOFT_LIGHT (str): Sets the blend mode to soft-light.
    DIFFERENCE (str): Sets the blend mode to difference.
    EXCLUSION (str): Sets the blend mode to exclusion.
    HUE (str): Sets the blend mode to hue.
    SATURATION (str): Sets the blend mode to saturation.
    COLOR (str): Sets the blend mode to color.
    LUMINOSITY (str): Sets the blend mode to luminosity.
    PLUS_DARKER (str): Sets the blend mode to plus-darker.
    PLUS_LIGHTER (str): Sets the blend mode to plus-lighter.
    """

    NORMAL = "mix-blend-normal"
    MULTIPLY = "mix-blend-multiply"
    SCREEN = "mix-blend-screen"
    OVERLAY = "mix-blend-overlay"
    DARKEN = "mix-blend-darken"
    LIGHTEN = "mix-blend-lighten"
    COLOR_DODGE = "mix-blend-color-dodge"
    COLOR_BURN = "mix-blend-color-burn"
    HARD_LIGHT = "mix-blend-hard-light"
    SOFT_LIGHT = "mix-blend-soft-light"
    DIFFERENCE = "mix-blend-difference"
    EXCLUSION = "mix-blend-exclusion"
    HUE = "mix-blend-hue"
    SATURATION = "mix-blend-saturation"
    COLOR = "mix-blend-color"
    LUMINOSITY = "mix-blend-luminosity"
    PLUS_DARKER = "mix-blend-plus-darker"
    PLUS_LIGHTER = "mix-blend-plus-lighter"