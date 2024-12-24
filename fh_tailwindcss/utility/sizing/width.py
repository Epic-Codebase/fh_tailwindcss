from ...tailwind import TailwindEnum, TailwindRaw

# https://tailwindcss.com/docs/width

class Width(TailwindEnum):
    """
    Enum class representing width utility classes in Tailwind CSS.

    Attributes:
        FULL (str): 100% width.
        HALF (str): 50% width.
        PER1_3 (str): 33.333% width.
        PER2_3 (str): 66.666% width.
        PER1_4 (str): 25% width.
        PER3_4 (str): 75% width.
        PER1_5 (str): 20% width.
        PER2_5 (str): 40% width.
        PER3_5 (str): 60% width.
        PER4_5 (str): 80% width.
        PER1_6 (str): 16.666% width.
        PER5_6 (str): 83.333% width.
        ZERO (str): 0px width.
        PX (str): 1px width.
        REM0_5 (str): 0.125rem (2px) width.
        REM1 (str): 0.25rem (4px) width.
        REM1_5 (str): 0.375rem (6px) width.
        REM2 (str): 0.5rem (8px) width.
        REM2_5 (str): 0.625rem (10px) width.
        REM3 (str): 0.75rem (12px) width.
        REM3_5 (str): 0.875rem (14px) width.
        REM4 (str): 1rem (16px) width.
        REM5 (str): 1.25rem (20px) width.
        REM6 (str): 1.5rem (24px) width.
        REM7 (str): 1.75rem (28px) width.
        REM8 (str): 2rem (32px) width.
        REM9 (str): 2.25rem (36px) width.
        REM10 (str): 2.5rem (40px) width.
        REM11 (str): 2.75rem (44px) width.
        REM12 (str): 3rem (48px) width.
        REM14 (str): 3.5rem (56px) width.
        REM16 (str): 4rem (64px) width.
        REM20 (str): 5rem (80px) width.
        REM24 (str): 6rem (96px) width.
        REM28 (str): 7rem (112px) width.
        REM32 (str): 8rem (128px) width.
        REM36 (str): 9rem (144px) width.
        REM40 (str): 10rem (160px) width.
        REM44 (str): 11rem (176px) width.
        REM48 (str): 12rem (192px) width.
        REM52 (str): 13rem (208px) width.
        REM56 (str): 14rem (224px) width.
        REM60 (str): 15rem (240px) width.
        REM64 (str): 16rem (256px) width.
        REM72 (str): 18rem (288px) width.
        REM80 (str): 20rem (320px) width.
        REM96 (str): 24rem (384px) width.
        AUTO (str): Automatically size based on content.
        MIN_CONTENT (str): min-content width.
        MAX_CONTENT (str): max-content width.
        FIT (str): Fits the content snugly.
        SCREEN (str): 100vw (full viewport width).
        SVW (str): 100svw (viewport width in svw units).
        LVW (str): 100lvw (viewport width in lvw units).
        DVW (str): 100dvw (viewport width in dvw units).
    """

    FULL = "w-full"             # 100%
    HALF = "w-1/2"              # 50%
    PER1_3 = "w-1/3"            # 33.333%
    PER2_3 = "w-2/3"            # 66.666%
    PER1_4 = "w-1/4"            # 25%
    PER3_4 = "w-3/4"            # 75%
    PER1_5 = "w-1/5"            # 20%
    PER2_5 = "w-2/5"            # 40%
    PER3_5 = "w-3/5"            # 60%
    PER4_5 = "w-4/5"            # 80%
    PER1_6 = "w-1/6"            # 16.666%
    PER5_6 = "w-5/6"            # 83.333%
    ZERO = "w-0"                # 0px
    PX = "w-px"                 # 1px
    REM0_5 = "w-0.5"            # 0.125rem (2px)
    REM1 = "w-1"                # 0.25rem (4px)
    REM1_5 = "w-1.5"            # 0.375rem (6px)
    REM2 = "w-2"                # 0.5rem (8px)
    REM2_5 = "w-2.5"            # 0.625rem (10px)
    REM3 = "w-3"                # 0.75rem (12px)
    REM3_5 = "w-3.5"            # 0.875rem (14px)
    REM4 = "w-4"                # 1rem (16px)
    REM5 = "w-5"                # 1.25rem (20px)
    REM6 = "w-6"                # 1.5rem (24px)
    REM7 = "w-7"                # 1.75rem (28px)
    REM8 = "w-8"                # 2rem (32px)
    REM9 = "w-9"                # 2.25rem (36px)
    REM10 = "w-10"              # 2.5rem (40px)
    REM11 = "w-11"              # 2.75rem (44px)
    REM12 = "w-12"              # 3rem (48px)
    REM14 = "w-14"              # 3.5rem (56px)
    REM16 = "w-16"              # 4rem (64px)
    REM20 = "w-20"              # 5rem (80px)
    REM24 = "w-24"              # 6rem (96px)
    REM28 = "w-28"              # 7rem (112px)
    REM32 = "w-32"              # 8rem (128px)
    REM36 = "w-36"              # 9rem (144px)
    REM40 = "w-40"              # 10rem (160px)
    REM44 = "w-44"              # 11rem (176px)
    REM48 = "w-48"              # 12rem (192px)
    REM52 = "w-52"              # 13rem (208px)
    REM56 = "w-56"              # 14rem (224px)
    REM60 = "w-60"              # 15rem (240px)
    REM64 = "w-64"              # 16rem (256px)
    REM72 = "w-72"              # 18rem (288px)
    REM80 = "w-80"              # 20rem (320px)
    REM96 = "w-96"              # 24rem (384px)
    AUTO = "w-auto"             # Automatically size based on content
    MIN_CONTENT = "w-min"       # min-content
    MAX_CONTENT = "w-max"       # max-content
    FIT = "w-fit"               # Fits the content snugly
    SCREEN = "w-screen"         # 100vw (full viewport width)
    SVW = "w-svw"               # 100svw (viewport width in svw units)
    LVW = "w-lvw"               # 100lvw (viewport width in lvw units)
    DVW = "w-dvw"               # 100dvw (viewport width in dvw units)

    
    @staticmethod
    def arbitrary(val) -> TailwindRaw:
        return TailwindRaw(f"w-[{val}]")