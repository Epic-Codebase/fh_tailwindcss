from ...tailwind import TailwindEnum, TailwindRaw

# https://tailwindcss.com/docs/size

class Size(TailwindEnum):
    """
    Enum class representing size utility classes for both width and height in Tailwind CSS.

    This includes fixed sizes, percentage-based sizes, fractional sizes, and content-fit utilities.

    Each enum field maps to a corresponding size class that applies equal width and height.

    Methods:
        arbitrary (str): Supports arbitrary values. e.g. size-[32rem]
    """
    SIZE_0 = "size-0"  # width: 0px; height: 0px;
    SIZE_PX = "size-px"  # width: 1px; height: 1px;
    SIZE_0_5 = "size-0.5"  # width: 0.125rem; height: 0.125rem; /* 2px */
    SIZE_1 = "size-1"  # width: 0.25rem; height: 0.25rem; /* 4px */
    SIZE_2 = "size-2"  # width: 0.5rem; height: 0.5rem; /* 8px */
    SIZE_3 = "size-3"  # width: 0.75rem; height: 0.75rem; /* 12px */
    SIZE_4 = "size-4"  # width: 1rem; height: 1rem; /* 16px */
    SIZE_5 = "size-5"  # width: 1.25rem; height: 1.25rem; /* 20px */
    SIZE_6 = "size-6"  # width: 1.5rem; height: 1.5rem; /* 24px */
    SIZE_7 = "size-7"  # width: 1.75rem; height: 1.75rem; /* 28px */
    SIZE_8 = "size-8"  # width: 2rem; height: 2rem; /* 32px */
    SIZE_9 = "size-9"  # width: 2.25rem; height: 2.25rem; /* 36px */
    SIZE_10 = "size-10"  # width: 2.5rem; height: 2.5rem; /* 40px */
    SIZE_11 = "size-11"  # width: 2.75rem; height: 2.75rem; /* 44px */
    SIZE_12 = "size-12"  # width: 3rem; height: 3rem; /* 48px */
    SIZE_14 = "size-14"  # width: 3.5rem; height: 3.5rem; /* 56px */
    SIZE_16 = "size-16"  # width: 4rem; height: 4rem; /* 64px */
    SIZE_20 = "size-20"  # width: 5rem; height: 5rem; /* 80px */
    SIZE_24 = "size-24"  # width: 6rem; height: 6rem; /* 96px */
    SIZE_28 = "size-28"  # width: 7rem; height: 7rem; /* 112px */
    SIZE_32 = "size-32"  # width: 8rem; height: 8rem; /* 128px */
    SIZE_36 = "size-36"  # width: 9rem; height: 9rem; /* 144px */
    SIZE_40 = "size-40"  # width: 10rem; height: 10rem; /* 160px */
    SIZE_44 = "size-44"  # width: 11rem; height: 11rem; /* 176px */
    SIZE_48 = "size-48"  # width: 12rem; height: 12rem; /* 192px */
    SIZE_52 = "size-52"  # width: 13rem; height: 13rem; /* 208px */
    SIZE_56 = "size-56"  # width: 14rem; height: 14rem; /* 224px */
    SIZE_60 = "size-60"  # width: 15rem; height: 15rem; /* 240px */
    SIZE_64 = "size-64"  # width: 16rem; height: 16rem; /* 256px */
    SIZE_72 = "size-72"  # width: 18rem; height: 18rem; /* 288px */
    SIZE_80 = "size-80"  # width: 20rem; height: 20rem; /* 320px */
    SIZE_96 = "size-96"  # width: 24rem; height: 24rem; /* 384px */
    SIZE_AUTO = "size-auto"  # width: auto; height: auto;

    # Fractional Sizes
    SIZE_1_2 = "size-1/2"  # width: 50%; height: 50%;
    SIZE_1_3 = "size-1/3"  # width: 33.333333%; height: 33.333333%;
    SIZE_2_3 = "size-2/3"  # width: 66.666667%; height: 66.666667%;
    SIZE_1_4 = "size-1/4"  # width: 25%; height: 25%;
    SIZE_2_4 = "size-2/4"  # width: 50%; height: 50%;
    SIZE_3_4 = "size-3/4"  # width: 75%; height: 75%;
    SIZE_1_5 = "size-1/5"  # width: 20%; height: 20%;
    SIZE_2_5 = "size-2/5"  # width: 40%; height: 40%;
    SIZE_3_5 = "size-3/5"  # width: 60%; height: 60%;
    SIZE_4_5 = "size-4/5"  # width: 80%; height: 80%;
    SIZE_1_6 = "size-1/6"  # width: 16.666667%; height: 16.666667%;
    SIZE_2_6 = "size-2/6"  # width: 33.333333%; height: 33.333333%;
    SIZE_3_6 = "size-3/6"  # width: 50%; height: 50%;
    SIZE_4_6 = "size-4/6"  # width: 66.666667%; height: 66.666667%;
    SIZE_5_6 = "size-5/6"  # width: 83.333333%; height: 83.333333%;

    SIZE_1_12 = "size-1/12"  # width: 8.333333%; height: 8.333333%;
    SIZE_2_12 = "size-2/12"  # width: 16.666667%; height: 16.666667%;
    SIZE_3_12 = "size-3/12"  # width: 25%; height: 25%;
    SIZE_4_12 = "size-4/12"  # width: 33.333333%; height: 33.333333%;
    SIZE_5_12 = "size-5/12"  # width: 41.666667%; height: 41.666667%;
    SIZE_6_12 = "size-6/12"  # width: 50%; height: 50%;
    SIZE_7_12 = "size-7/12"  # width: 58.333333%; height: 58.333333%;
    SIZE_8_12 = "size-8/12"  # width: 66.666667%; height: 66.666667%;
    SIZE_9_12 = "size-9/12"  # width: 75%; height: 75%;
    SIZE_10_12 = "size-10/12"  # width: 83.333333%; height: 83.333333%;
    SIZE_11_12 = "size-11/12"  # width: 91.666667%; height: 91.666667%;

    # Content Sizes
    SIZE_FULL = "size-full"  # width: 100%; height: 100%;
    SIZE_MIN = "size-min"  # width: min-content; height: min-content;
    SIZE_MAX = "size-max"  # width: max-content; height: max-content;
    SIZE_FIT = "size-fit"  # width: fit-content; height: fit-content;


    @staticmethod
    def arbitrary(val) -> TailwindRaw:
        return TailwindRaw(f"size-[{val}]")