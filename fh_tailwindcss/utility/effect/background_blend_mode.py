from ...tailwind import TailwindEnum

class BackgroundBlendMode(TailwindEnum):
    """
    Utilities for controlling how an element's background image should blend with its background color.

    Attributes:
    NORMAL (str): Sets the background blend mode to normal.
    MULTIPLY (str): Sets the background blend mode to multiply.
    SCREEN (str): Sets the background blend mode to screen.
    OVERLAY (str): Sets the background blend mode to overlay.
    DARKEN (str): Sets the background blend mode to darken.
    LIGHTEN (str): Sets the background blend mode to lighten.
    COLOR_DODGE (str): Sets the background blend mode to color-dodge.
    COLOR_BURN (str): Sets the background blend mode to color-burn.
    HARD_LIGHT (str): Sets the background blend mode to hard-light.
    SOFT_LIGHT (str): Sets the background blend mode to soft-light.
    DIFFERENCE (str): Sets the background blend mode to difference.
    EXCLUSION (str): Sets the background blend mode to exclusion.
    HUE (str): Sets the background blend mode to hue.
    SATURATION (str): Sets the background blend mode to saturation.
    COLOR (str): Sets the background blend mode to color.
    LUMINOSITY (str): Sets the background blend mode to luminosity.
    """

    NORMAL = "bg-blend-normal"
    MULTIPLY = "bg-blend-multiply"
    SCREEN = "bg-blend-screen"
    OVERLAY = "bg-blend-overlay"
    DARKEN = "bg-blend-darken"
    LIGHTEN = "bg-blend-lighten"
    COLOR_DODGE = "bg-blend-color-dodge"
    COLOR_BURN = "bg-blend-color-burn"
    HARD_LIGHT = "bg-blend-hard-light"
    SOFT_LIGHT = "bg-blend-soft-light"
    DIFFERENCE = "bg-blend-difference"
    EXCLUSION = "bg-blend-exclusion"
    HUE = "bg-blend-hue"
    SATURATION = "bg-blend-saturation"
    COLOR = "bg-blend-color"
    LUMINOSITY = "bg-blend-luminosity"