from ...tailwind import TailwindEnum

# https://chatgpt.com/c/67621b7c-4b24-8008-a905-a66e8581eca4

class BorderRadius(TailwindEnum):
    """
    Enum class representing different border radius values in Tailwind CSS.

    Attributes:
        NONE (str): No rounding (0px).
        SMALL (str): Small rounding (0.125rem).
        DEFAULT (str): Default rounding (0.25rem).
        MEDIUM (str): Medium rounding (0.375rem).
        LARGE (str): Large rounding (0.5rem).
        XLARGE (str): Extra large rounding (0.75rem).
        XXLARGE (str): 2x larger rounding (1rem).
        XXXLARGE (str): 3x larger rounding (1.5rem).
        FULL (str): Fully rounded, circular shape (9999px).
        AND OTHER VARIANTS FOR START, END, TOP, BOTTOM, AND LEFT/RIGHT CORNERS.
    """
    NONE = 'rounded-none'
    SMALL = 'rounded-sm'
    DEFAULT = 'rounded'
    MEDIUM = 'rounded-md'
    LARGE = 'rounded-lg'
    XLARGE = 'rounded-xl'
    XLARGE2 = 'rounded-2xl'
    XLARGE3 = 'rounded-3xl'
    FULL = 'rounded-full'

    # Start (border-start)
    START_NONE = 'rounded-s-none'
    START_SMALL = 'rounded-s-sm'
    START_DEFAULT = 'rounded-s'
    START_MEDIUM = 'rounded-s-md'
    START_LARGE = 'rounded-s-lg'
    START_XLARGE = 'rounded-s-xl'
    START_XLARGE2 = 'rounded-s-2xl'
    START_XLARGE3 = 'rounded-s-3xl'
    START_FULL = 'rounded-s-full'

    # End (border-end)
    END_NONE = 'rounded-e-none'
    END_SMALL = 'rounded-e-sm'
    END_DEFAULT = 'rounded-e'
    END_MEDIUM = 'rounded-e-md'
    END_LARGE = 'rounded-e-lg'
    END_XLARGE = 'rounded-e-xl'
    END_XLARGE2 = 'rounded-e-2xl'
    END_XLARGE3 = 'rounded-e-3xl'
    END_FULL = 'rounded-e-full'

    # Top (border-top)
    TOP_NONE = 'rounded-t-none'
    TOP_SMALL = 'rounded-t-sm'
    TOP_DEFAULT = 'rounded-t'
    TOP_MEDIUM = 'rounded-t-md'
    TOP_LARGE = 'rounded-t-lg'
    TOP_XLARGE = 'rounded-t-xl'
    TOP_XLARGE2 = 'rounded-t-2xl'
    TOP_XLARGE3 = 'rounded-t-3xl'
    TOP_FULL = 'rounded-t-full'

    # Right (border-right)
    RIGHT_NONE = 'rounded-r-none'
    RIGHT_SMALL = 'rounded-r-sm'
    RIGHT_DEFAULT = 'rounded-r'
    RIGHT_MEDIUM = 'rounded-r-md'
    RIGHT_LARGE = 'rounded-r-lg'
    RIGHT_XLARGE = 'rounded-r-xl'
    RIGHT_XLARGE2 = 'rounded-r-2xl'
    RIGHT_XLARGE3 = 'rounded-r-3xl'
    RIGHT_FULL = 'rounded-r-full'

    # Bottom (border-bottom)
    BOTTOM_NONE = 'rounded-b-none'
    BOTTOM_SMALL = 'rounded-b-sm'
    BOTTOM_DEFAULT = 'rounded-b'
    BOTTOM_MEDIUM = 'rounded-b-md'
    BOTTOM_LARGE = 'rounded-b-lg'
    BOTTOM_XLARGE = 'rounded-b-xl'
    BOTTOM_XLARGE2 = 'rounded-b-2xl'
    BOTTOM_XLARGE3 = 'rounded-b-3xl'
    BOTTOM_FULL = 'rounded-b-full'

    # Left (border-left)
    LEFT_NONE = 'rounded-l-none'
    LEFT_SMALL = 'rounded-l-sm'
    LEFT_DEFAULT = 'rounded-l'
    LEFT_MEDIUM = 'rounded-l-md'
    LEFT_LARGE = 'rounded-l-lg'
    LEFT_XLARGE = 'rounded-l-xl'
    LEFT_XLARGE2 = 'rounded-l-2xl'
    LEFT_XLARGE3 = 'rounded-l-3xl'
    LEFT_FULL = 'rounded-l-full'

    # Start-Start (border-start-start)
    SS_NONE = 'rounded-ss-none'
    SS_SMALL = 'rounded-ss-sm'
    SS_DEFAULT = 'rounded-ss'
    SS_MEDIUM = 'rounded-ss-md'
    SS_LARGE = 'rounded-ss-lg'
    SS_XLARGE = 'rounded-ss-xl'
    SS_XLARGE2 = 'rounded-ss-2xl'
    SS_XLARGE3 = 'rounded-ss-3xl'
    SS_FULL = 'rounded-ss-full'

    # Start-End (border-start-end)
    SE_NONE = 'rounded-se-none'
    SE_SMALL = 'rounded-se-sm'
    SE_DEFAULT = 'rounded-se'
    SE_MEDIUM = 'rounded-se-md'
    SE_LARGE = 'rounded-se-lg'
    SE_XLARGE = 'rounded-se-xl'
    SE_XLARGE2 = 'rounded-se-2xl'
    SE_XLARGE3 = 'rounded-se-3xl'
    SE_FULL = 'rounded-se-full'

    # End-End (border-end-end)
    EE_NONE = 'rounded-ee-none'
    EE_SMALL = 'rounded-ee-sm'
    EE_DEFAULT = 'rounded-ee'
    EE_MEDIUM = 'rounded-ee-md'
    EE_LARGE = 'rounded-ee-lg'
    EE_XLARGE = 'rounded-ee-xl'
    EE_XLARGE2 = 'rounded-ee-2xl'
    EE_XLARGE3 = 'rounded-ee-3xl'
    EE_FULL = 'rounded-ee-full'

    # End-Start (border-end-start)
    ES_NONE = 'rounded-es-none'
    ES_SMALL = 'rounded-es-sm'
    ES_DEFAULT = 'rounded-es'
    ES_MEDIUM = 'rounded-es-md'
    ES_LARGE = 'rounded-es-lg'
    ES_XLARGE = 'rounded-es-xl'
    ES_XLARGE2 = 'rounded-es-2xl'
    ES_XLARGE3 = 'rounded-es-3xl'
    ES_FULL = 'rounded-es-full'

    # Top-Left (border-top-left)
    TL_NONE = 'rounded-tl-none'
    TL_SMALL = 'rounded-tl-sm'
    TL_DEFAULT = 'rounded-tl'
    TL_MEDIUM = 'rounded-tl-md'
    TL_LARGE = 'rounded-tl-lg'
    TL_XLARGE = 'rounded-tl-xl'
    TL_XLARGE2 = 'rounded-tl-2xl'
    TL_XLARGE3 = 'rounded-tl-3xl'
    TL_FULL = 'rounded-tl-full'

    # Top-Right (border-top-right)
    TR_NONE = 'rounded-tr-none'
    TR_SMALL = 'rounded-tr-sm'
    TR_DEFAULT = 'rounded-tr'
    TR_MEDIUM = 'rounded-tr-md'
    TR_LARGE = 'rounded-tr-lg'
    TR_XLARGE = 'rounded-tr-xl'
    TR_XLARGE2 = 'rounded-tr-2xl'
    TR_XLARGE3 = 'rounded-tr-3xl'
    TR_FULL = 'rounded-tr-full'

    # Bottom-Right (border-bottom-right)
    BR_NONE = 'rounded-br-none'
    BR_SMALL = 'rounded-br-sm'
    BR_DEFAULT = 'rounded-br'
    BR_MEDIUM = 'rounded-br-md'
    BR_LARGE = 'rounded-br-lg'
    BR_XLARGE = 'rounded-br-xl'
    BR_XLARGE2 = 'rounded-br-2xl'
    BR_XLARGE3 = 'rounded-br-3xl'
    BR_FULL = 'rounded-br-full'

    # Bottom-Left (border-bottom-left)
    BL_NONE = 'rounded-bl-none'
    BL_SMALL = 'rounded-bl-sm'
    BL_DEFAULT = 'rounded-bl'
    BL_MEDIUM = 'rounded-bl-md'
    BL_LARGE = 'rounded-bl-lg'
    BL_XLARGE = 'rounded-bl-xl'
    BL_XLARGE2 = 'rounded-bl-2xl'
    BL_XLARGE3 = 'rounded-bl-3xl'
    BL_FULL = 'rounded-bl-full'