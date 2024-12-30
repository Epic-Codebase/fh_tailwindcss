from ...tailwind import TailwindDict

from .blur import Blur
from .brightness import Brightness
from .contrast import Contrast
from .grayscale import GrayScale
from .hue_rotate import HueRotate
from .invert import Invert
from ..effect import Opacity
from .saturate import Saturate
from .sepia import Sepia


# https://tailwindcss.com/docs/backdrop-blur

class BackdropBlur(Blur):
    """
    Utilities for applying backdrop-blur filters to an element.

    Attributes:
        NONE (str): Applies no backdrop-blur filter.
        SM (str): Applies a backdrop-blur filter with a radius of 4px.
        DEFAULT (str): Applies a backdrop-blur filter with a radius of 8px.
        MD (str): Applies a backdrop-blur filter with a radius of 12px.
        LG (str): Applies a backdrop-blur filter with a radius of 16px.
        XL (str): Applies a backdrop-blur filter with a radius of 24px.
        XXL (str): Applies a backdrop-blur filter with a radius of 40px.
        XXXL (str): Applies a backdrop-blur filter with a radius of 64px.
    """
    
    NONE = "backdrop" + str(Blur.NONE)
    SM = "backdrop" + str(Blur.SM)
    DEFAULT = "backdrop" + str(Blur.DEFAULT)
    MD = "backdrop" + str(Blur.MD)
    LG = "backdrop" + str(Blur.LG)
    XL = "backdrop" + str(Blur.XL)
    XXL = "backdrop" + str(Blur.XXL)
    XXXL = "backdrop" + str(Blur.XXXL)


# https://tailwindcss.com/docs/backdrop-brightness

class BackdropBrightness(Brightness):
    """
    Utilities for applying brightness filters to an element.

    Attributes:
    BRIGHTNESS (str): Base class for brightness utilities. Available intensity values: 
    [0, 50, 75, 90, 95, 100, 105, 110, 125, 150, 200].
    """

    BRIGHTNESS = "backdrop" + str(Brightness.BRIGHTNESS)

class BackdropBrightnesses(TailwindDict):
    pass


# https://tailwindcss.com/docs/backdrop-contrast

class BackdropContrast(Contrast):
    """
    Utilities for applying contrast filters to an element.

    Attributes:
    CONTRAST (str): Base class for contrast utilities. Available intensity values: 
    [0, 50, 75, 100, 125, 150, 200].
    """

    CONTRAST = "backdrop" + str(Contrast.CONTRAST)    

class BackdropContrasts(TailwindDict):
    pass


# https://tailwindcss.com/docs/backdrop-grayscale

class BackdropGrayScale(GrayScale):
    """
    Utilities for applying grayscale filters to an element.

    Attributes:
    GRAYSCALE_0 (str): No grayscale applied.
    GRAYSCALE (str): Applies full grayscale (100%).
    """

    GRAYSCALE_0 = "backdrop" + str(GrayScale.GRAYSCALE_0)
    GRAYSCALE = "backdrop" + str(GrayScale.GRAYSCALE)


# https://tailwindcss.com/docs/backdrop-hue-rotate

class BackdropHueRotate(HueRotate):
    """
    Utilities for applying hue-rotate filters to an element.

    Attributes:
        HUE_ROTATE (str): Applies a hue-rotate filter. Available degrees: [0, 15, 30, 60, 90, 180].
    """

    HUE_ROTATE = "backdrop" + str(HueRotate.HUE_ROTATE)

class BackdropHueRotateDegrees(TailwindDict):
    pass


# https://tailwindcss.com/docs/backdrop-invert

class BackdropInvert(Invert):
    """
    Utilities for applying invert filters to an element.

    Attributes:
    INVERT_0 (str): No invert applied.
    INVERT (str): Applies full invert (100%).
    """

    INVERT_0 = "backdrop" + str(Invert.INVERT_0)
    INVERT = "backdrop" + str(Invert.INVERT)


# https://tailwindcss.com/docs/backdrop-opacity

class BackdropOpacity(Opacity):
    """
    Utilities for controlling the opacity of an element.

    Attributes:
        OPACITY (str): Base class for opacity utilities. Available intensity values: 
        [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100].
    """

    OPACITY = "backdrop" + str(Opacity.OPACITY)

class BackdropOpacities(TailwindDict):
    pass


# https://tailwindcss.com/docs/backdrop-saturate

class BackdropSaturate(Saturate):
    """
    Utilities for applying saturation filters to an element.

    Attributes:
        SATURATE (str): Applies a saturation filter. Available percentages: [0, 50, 100, 150, 200].
    """

    SATURATE = "backdrop" + str(Saturate.SATURATE)

class BackdropSaturateValues(TailwindDict):
    pass


# https://tailwindcss.com/docs/backdrop-sepia

class BackdropSepia(Sepia):
    """
    Utilities for applying sepia filters to an element.

    Attributes:
    SEPIA_0 (str): No sepia applied.
    SEPIA (str): Applies full sepia (100%).
    """

    SEPIA_0 = "backdrop" + str(Sepia.SEPIA_0)
    SEPIA = "backdrop" + str(Sepia.SEPIA)