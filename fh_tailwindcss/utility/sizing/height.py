from ...tailwind import TailwindEnum, TailwindRaw

# https://tailwindcss.com/docs/height

class Height(TailwindEnum):
    """
    Enum class representing height utility classes in Tailwind CSS.

    Attributes:
        FULL (str): 100% height.
        HALF (str): 50% height.
        PER1_3 (str): 33.333% height.
        PER2_3 (str): 66.666% height.
        PER1_4 (str): 25% height.
        PER3_4 (str): 75% height.
        PER1_5 (str): 20% height.
        PER2_5 (str): 40% height.
        PER3_5 (str): 60% height.
        PER4_5 (str): 80% height.
        PER1_6 (str): 16.666% height.
        PER5_6 (str): 83.333% height.
        ZERO (str): 0px height.
        PX (str): 1px height.
        REM0_5 (str): 0.125rem (2px) height.
        REM1 (str): 0.25rem (4px) height.
        REM1_5 (str): 0.375rem (6px) height.
        REM2 (str): 0.5rem (8px) height.
        REM2_5 (str): 0.625rem (10px) height.
        REM3 (str): 0.75rem (12px) height.
        REM3_5 (str): 0.875rem (14px) height.
        REM4 (str): 1rem (16px) height.
        REM5 (str): 1.25rem (20px) height.
        REM6 (str): 1.5rem (24px) height.
        REM7 (str): 1.75rem (28px) height.
        REM8 (str): 2rem (32px) height.
        AUTO (str): Automatically size based on content.
        MIN_CONTENT (str): min-content height.
        MAX_CONTENT (str): max-content height.
        FIT (str): Fits the content snugly.
        SCREEN (str): 100vh (full viewport height).
        SVH (str): 100svh (viewport height in svh units).
        LVH (str): 100lvh (viewport height in lvh units).
        DVH (str): 100dvh (viewport height in dvh units).

    Methods:
        arbitrary (str): Supports arbitrary values. e.g. h-[32rem]
    """

    FULL = "h-full"             # 100%
    HALF = "h-1/2"              # 50%
    PER1_3 = "h-1/3"            # 33.333%
    PER2_3 = "h-2/3"            # 66.666%
    PER1_4 = "h-1/4"            # 25%
    PER3_4 = "h-3/4"            # 75%
    PER1_5 = "h-1/5"            # 20%
    PER2_5 = "h-2/5"            # 40%
    PER3_5 = "h-3/5"            # 60%
    PER4_5 = "h-4/5"            # 80%
    PER1_6 = "h-1/6"            # 16.666%
    PER5_6 = "h-5/6"            # 83.333%
    ZERO = "h-0"                # 0px
    PX = "h-px"                 # 1px
    REM0_5 = "h-0.5"            # 0.125rem (2px)
    REM1 = "h-1"                # 0.25rem (4px)
    REM1_5 = "h-1.5"            # 0.375rem (6px)
    REM2 = "h-2"                # 0.5rem (8px)
    REM2_5 = "h-2.5"            # 0.625rem (10px)
    REM3 = "h-3"                # 0.75rem (12px)
    REM3_5 = "h-3.5"            # 0.875rem (14px)
    REM4 = "h-4"                # 1rem (16px)
    REM5 = "h-5"                # 1.25rem (20px)
    REM6 = "h-6"                # 1.5rem (24px)
    REM7 = "h-7"                # 1.75rem (28px)
    REM8 = "h-8"                # 2rem (32px)
    AUTO = "h-auto"             # Automatically size based on content
    MIN_CONTENT = "h-min"       # min-content
    MAX_CONTENT = "h-max"       # max-content
    FIT = "h-fit"               # Fits the content snugly
    SCREEN = "h-screen"         # 100vh (full viewport height)
    SVH = "h-svh"               # 100svh (viewport height in svh units)
    LVH = "h-lvh"               # 100lvh (viewport height in lvh units)
    DVH = "h-dvh"               # 100dvh (viewport height in dvh units)
    
    @staticmethod
    def arbitrary(val) -> TailwindRaw:
        return TailwindRaw(f"h-[{val}]")