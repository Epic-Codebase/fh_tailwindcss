from ...tailwind import TailwindEnum, TailwindRaw

# https://tailwindcss.com/docs/min-height

class MinHeight(TailwindEnum):
    """
    Enum class for TailwindCSS min-height utilities.
    Represents the min-height utilities for various sizes and values.

    Attributes:
        - MIN_H: "min-h-{0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96, px, full, screen, svh, lvh, dvh, min, max, fit}"
    Methods:
        arbitrary (str): Supports arbitrary values. e.g. min-h-[220px]
    """
    
    MIN_H = "min-h"
    
    # Standard min-h sizes
    MIN_H_0 = "min-h-0"
    MIN_H_0_5 = "min-h-0.5"
    MIN_H_1 = "min-h-1"
    MIN_H_1_5 = "min-h-1.5"
    MIN_H_2 = "min-h-2"
    MIN_H_2_5 = "min-h-2.5"
    MIN_H_3 = "min-h-3"
    MIN_H_3_5 = "min-h-3.5"
    MIN_H_4 = "min-h-4"
    MIN_H_5 = "min-h-5"
    MIN_H_6 = "min-h-6"
    MIN_H_7 = "min-h-7"
    MIN_H_8 = "min-h-8"
    MIN_H_9 = "min-h-9"
    MIN_H_10 = "min-h-10"
    MIN_H_11 = "min-h-11"
    MIN_H_12 = "min-h-12"
    MIN_H_14 = "min-h-14"
    MIN_H_16 = "min-h-16"
    MIN_H_20 = "min-h-20"
    MIN_H_24 = "min-h-24"
    MIN_H_28 = "min-h-28"
    MIN_H_32 = "min-h-32"
    MIN_H_36 = "min-h-36"
    MIN_H_40 = "min-h-40"
    MIN_H_44 = "min-h-44"
    MIN_H_48 = "min-h-48"
    MIN_H_52 = "min-h-52"
    MIN_H_56 = "min-h-56"
    MIN_H_60 = "min-h-60"
    MIN_H_64 = "min-h-64"
    MIN_H_72 = "min-h-72"
    MIN_H_80 = "min-h-80"
    MIN_H_96 = "min-h-96"
    
    # Special cases for min-height
    MIN_H_PX = "min-h-px"
    MIN_H_FULL = "min-h-full"
    MIN_H_SCREEN = "min-h-screen"
    MIN_H_SVH = "min-h-svh"
    MIN_H_LVH = "min-h-lvh"
    MIN_H_DVH = "min-h-dvh"
    MIN_H_MIN = "min-h-min"
    MIN_H_MAX = "min-h-max"
    MIN_H_FIT = "min-h-fit"


    @staticmethod
    def arbitrary(val) -> TailwindRaw:
        return TailwindRaw(f"min-h-[{val}]")
