from ...tailwind import TailwindEnum, TailwindRaw

# https://tailwindcss.com/docs/min-width

class MinWidth(TailwindEnum):
    """
    Enum class for TailwindCSS min-width utilities.
    Represents the min-width utilities for various sizes and values.

    Attributes:
        - MIN_W: "min-w-{0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96, px, full, min, max, fit}"

    Methods:
        arbitrary (str): Supports arbitrary values. e.g. min-w-[220px]
    """
    
    MIN_W = "min-w"
    
    # Standard min-w sizes
    MIN_W_0 = "min-w-0"
    MIN_W_0_5 = "min-w-0.5"
    MIN_W_1 = "min-w-1"
    MIN_W_1_5 = "min-w-1.5"
    MIN_W_2 = "min-w-2"
    MIN_W_2_5 = "min-w-2.5"
    MIN_W_3 = "min-w-3"
    MIN_W_3_5 = "min-w-3.5"
    MIN_W_4 = "min-w-4"
    MIN_W_5 = "min-w-5"
    MIN_W_6 = "min-w-6"
    MIN_W_7 = "min-w-7"
    MIN_W_8 = "min-w-8"
    MIN_W_9 = "min-w-9"
    MIN_W_10 = "min-w-10"
    MIN_W_11 = "min-w-11"
    MIN_W_12 = "min-w-12"
    MIN_W_14 = "min-w-14"
    MIN_W_16 = "min-w-16"
    MIN_W_20 = "min-w-20"
    MIN_W_24 = "min-w-24"
    MIN_W_28 = "min-w-28"
    MIN_W_32 = "min-w-32"
    MIN_W_36 = "min-w-36"
    MIN_W_40 = "min-w-40"
    MIN_W_44 = "min-w-44"
    MIN_W_48 = "min-w-48"
    MIN_W_52 = "min-w-52"
    MIN_W_56 = "min-w-56"
    MIN_W_60 = "min-w-60"
    MIN_W_64 = "min-w-64"
    MIN_W_72 = "min-w-72"
    MIN_W_80 = "min-w-80"
    MIN_W_96 = "min-w-96"
    
    # Special cases for min-width
    MIN_W_PX = "min-w-px"
    MIN_W_FULL = "min-w-full"
    MIN_W_MIN = "min-w-min"
    MIN_W_MAX = "min-w-max"
    MIN_W_FIT = "min-w-fit"


    @staticmethod
    def arbitrary(val) -> TailwindRaw:
        return TailwindRaw(f"min-w-[{val}]")