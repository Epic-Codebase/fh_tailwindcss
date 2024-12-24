from ...tailwind import TailwindEnum, TailwindRaw

# https://tailwindcss.com/docs/max-height

class MaxHeight(TailwindEnum):
    """
    Enum class for TailwindCSS max-height utilities.
    Represents the max-height utilities for various sizes and values.

    Attributes:
        - MAX_H: "max-h-{0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96, px, none, full, screen, svh, lvh, dvh, min, max, fit}"

    Methods:
        arbitrary (str): Supports arbitrary values. e.g. max-h-[220px]
    """

    MAX_H = "max-h"
    
    # Standard max-h sizes
    MAX_H_0 = "max-h-0"
    MAX_H_0_5 = "max-h-0.5"
    MAX_H_1 = "max-h-1"
    MAX_H_1_5 = "max-h-1.5"
    MAX_H_2 = "max-h-2"
    MAX_H_2_5 = "max-h-2.5"
    MAX_H_3 = "max-h-3"
    MAX_H_3_5 = "max-h-3.5"
    MAX_H_4 = "max-h-4"
    MAX_H_5 = "max-h-5"
    MAX_H_6 = "max-h-6"
    MAX_H_7 = "max-h-7"
    MAX_H_8 = "max-h-8"
    MAX_H_9 = "max-h-9"
    MAX_H_10 = "max-h-10"
    MAX_H_11 = "max-h-11"
    MAX_H_12 = "max-h-12"
    MAX_H_14 = "max-h-14"
    MAX_H_16 = "max-h-16"
    MAX_H_20 = "max-h-20"
    MAX_H_24 = "max-h-24"
    MAX_H_28 = "max-h-28"
    MAX_H_32 = "max-h-32"
    MAX_H_36 = "max-h-36"
    MAX_H_40 = "max-h-40"
    MAX_H_44 = "max-h-44"
    MAX_H_48 = "max-h-48"
    MAX_H_52 = "max-h-52"
    MAX_H_56 = "max-h-56"
    MAX_H_60 = "max-h-60"
    MAX_H_64 = "max-h-64"
    MAX_H_72 = "max-h-72"
    MAX_H_80 = "max-h-80"
    MAX_H_96 = "max-h-96"
    
    # Special cases for max-height
    MAX_H_PX = "max-h-px"
    MAX_H_NONE = "max-h-none"
    MAX_H_FULL = "max-h-full"
    MAX_H_SCREEN = "max-h-screen"
    MAX_H_SVH = "max-h-svh"
    MAX_H_LVH = "max-h-lvh"
    MAX_H_DVH = "max-h-dvh"
    MAX_H_MIN = "max-h-min"
    MAX_H_MAX = "max-h-max"
    MAX_H_FIT = "max-h-fit"

    
    @staticmethod
    def arbitrary(val) -> TailwindRaw:
        return TailwindRaw(f"max-h-[{val}]")