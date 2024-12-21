from ..tailwind import TailwindEnum

# https://tailwindcss.com/docs/size

class Size(TailwindEnum):
    """
    Enum class representing size utility classes for both width and height in Tailwind CSS.

    Attributes:
        SIZE_0 (str): 0px width and height.
        SIZE_PX (str): 1px width and height.
        SIZE_0_5 (str): 0.125rem (2px) width and height.
        SIZE_1 (str): 0.25rem (4px) width and height.
        SIZE_1_5 (str): 0.375rem (6px) width and height.
        SIZE_2 (str): 0.5rem (8px) width and height.
        SIZE_2_5 (str): 0.625rem (10px) width and height.
        SIZE_3 (str): 0.75rem (12px) width and height.
        SIZE_3_5 (str): 0.875rem (14px) width and height.
        SIZE_4 (str): 1rem (16px) width and height.
        SIZE_5 (str): 1.25rem (20px) width and height.
        SIZE_6 (str): 1.5rem (24px) width and height.
        SIZE_7 (str): 1.75rem (28px) width and height.
        SIZE_8 (str): 2rem (32px) width and height.
        SIZE_9 (str): 2.25rem (36px) width and height.
        SIZE_10 (str): 2.5rem (40px) width and height.
        SIZE_11 (str): 2.75rem (44px) width and height.
        SIZE_12 (str): 3rem (48px) width and height.
        SIZE_14 (str): 3.5rem (56px) width and height.
        SIZE_16 (str): 4rem (64px) width and height.
        SIZE_20 (str): 5rem (80px) width and height.
        SIZE_24 (str): 6rem (96px) width and height.
        SIZE_28 (str): 7rem (112px) width and height.
        SIZE_32 (str): 8rem (128px) width and height.
        SIZE_36 (str): 9rem (144px) width and height.
        SIZE_40 (str): 10rem (160px) width and height.
        SIZE_44 (str): 11rem (176px) width and height.
        SIZE_48 (str): 12rem (192px) width and height.
        SIZE_52 (str): 13rem (208px) width and height.
        SIZE_56 (str): 14rem (224px) width and height.
        SIZE_60 (str): 15rem (240px) width and height.
        SIZE_64 (str): 16rem (256px) width and height.
        SIZE_72 (str): 18rem (288px) width and height.
        SIZE_80 (str): 20rem (320px) width and height.
        SIZE_96 (str): 24rem (384px) width and height.
        SIZE_AUTO (str): auto width and height.
        SIZE_1_2 (str): 50% width and height.
        SIZE_1_3 (str): 33.333333% width and height.
        SIZE_2_3 (str): 66.666667% width and height.
        SIZE_1_4 (str): 25% width and height.
        SIZE_2_4 (str): 50% width and height.
        SIZE_3_4 (str): 75% width and height.
        SIZE_1_5 (str): 20% width and height.
        SIZE_2_5 (str): 40% width and height.
        SIZE_3_5 (str): 60% width and height.
        SIZE_4_5 (str): 80% width and height.
        SIZE_1_6 (str): 16.666667% width and height.
        SIZE_2_6 (str): 33.333333% width and height.
        SIZE_3_6 (str): 50% width and height.
        SIZE_4_6 (str): 66.666667% width and height.
        SIZE_5_6 (str): 83.333333% width and height.
        SIZE_1_12 (str): 8.333333% width and height.
        SIZE_2_12 (str): 16.666667% width and height.
        SIZE_3_12 (str): 25% width and height.
        SIZE_4_12 (str): 33.333333% width and height.
        SIZE_5_12 (str): 41.666667% width and height.
        SIZE_6_12 (str): 50% width and height.
        SIZE_7_12 (str): 58.333333% width and height.
        SIZE_8_12 (str): 66.666667% width and height.
        SIZE_9_12 (str): 75% width and height.
        SIZE_10_12 (str): 83.333333% width and height.
        SIZE_11_12 (str): 91.666667% width and height.
        SIZE_FULL (str): 100% width and height.
        SIZE_MIN (str): min-content width and height.
        SIZE_MAX (str): max-content width and height.
        SIZE_FIT (str): fit-content width and height.
    """

    SIZE_0 = "size-0"          # 0px width and height
    SIZE_PX = "size-px"        # 1px width and height
    SIZE_0_5 = "size-0.5"      # 0.125rem (2px) width and height
    SIZE_1 = "size-1"          # 0.25rem (4px) width and height
    SIZE_1_5 = "size-1.5"      # 0.375rem (6px) width and height
    SIZE_2 = "size-2"          # 0.5rem (8px) width and height
    SIZE_2_5 = "size-2.5"      # 0.625rem (10px) width and height
    SIZE_3 = "size-3"          # 0.75rem (12px) width and height
    SIZE_3_5 = "size-3.5"      # 0.875rem (14px) width and height
    SIZE_4 = "size-4"          # 1rem (16px) width and height
    SIZE_5 = "size-5"          # 1.25rem (20px) width and height
    SIZE_6 = "size-6"          # 1.5rem (24px) width and height
    SIZE_7 = "size-7"          # 1.75rem (28px) width and height
    SIZE_8 = "size-8"          # 2rem (32px) width and height
    SIZE_9 = "size-9"          # 2.25rem (36px) width and height
    SIZE_10 = "size-10"        # 2.5rem (40px) width and height
    SIZE_11 = "size-11"        # 2.75rem (44px) width and height
    SIZE_12 = "size-12"        # 3rem (48px) width and height
    SIZE_14 = "size-14"        # 3.5rem (56px) width and height
    SIZE_16 = "size-16"        # 4rem (64px) width and height
    SIZE_20 = "size-20"        # 5rem (80px) width and height
    SIZE_24 = "size-24"        # 6rem (96px) width and height
    SIZE_28 = "size-28"        # 7rem (112px) width and height
    SIZE_32 = "size-32"        # 8rem (128px) width and height
    SIZE_36 = "size-36"        # 9rem (144px) width and height
    SIZE_40 = "size-40"        # 10rem (160px) width and height
    SIZE_44 = "size-44"        # 11rem (176px) width and height
    SIZE_48 = "size-48"        # 12rem (192px) width and height
    SIZE_52 = "size-52"        # 13rem (208px) width and height
    SIZE_56 = "size-56"        # 14rem (224px) width and height
    SIZE_60 = "size-60"        # 15rem (240px) width and height
    SIZE_64 = "size-64"        # 16rem (256px) width and height
    SIZE_72 = "size-72"        # 18rem (288px) width and height
    SIZE_80 = "size-80"        # 20rem (320px) width and height
    SIZE_96 = "size-96"        # 24rem (384px) width and height
    SIZE_AUTO = "size-auto"    # auto width and height
    SIZE_1_2 = "size-1/2"      # 50% width and height
    SIZE_1_3 = "size-1/3"      # 33.333333% width and height
    SIZE_2_3 = "size-2/3"      # 66.666667% width and height
    SIZE_1_4 = "size-1/4"      # 25% width and height
    SIZE_2_4 = "size-2/4"      # 50% width and height
    SIZE_3_4 = "size-3/4"      # 75% width and height
    SIZE_1_5 = "size-1/5"      # 20% width and height
    SIZE_2_5 = "size-2/5"      # 40% width and height
    SIZE_3_5 = "size-3/5"      # 60% width and height
    SIZE_4_5 = "size-4/5"      # 80% width and height
    SIZE_1_6 = "size-1/6"      # 16.666667% width and height
    SIZE_2_6 = "size-2/6"      # 33.333333% width and height
    SIZE_3_6 = "size-3/6"      # 50% width and height
    SIZE_4_6 = "size-4/6"      # 66.666667% width and height
    SIZE_5_6 = "size-5/6"      # 83.333333% width and height
    SIZE_1_2 = "size-1/2"      # 50% width and height
    SIZE_1_3 = "size-1/3"      # 33.333333% width and height
    SIZE_2_3 = "size-2/3"      # 66.666667% width and height
    SIZE_1_4 = "size-1/4"      # 25% width and height
    SIZE_2_4 = "size-2/4"      # 50% width and height
    SIZE_3_4 = "size-3/4"      # 75% width and height
    SIZE_1_5 = "size-1/5"      # 20% width and height
    SIZE_2_5 = "size-2/5"      # 40% width and height
    SIZE_3_5 = "size-3/5"      # 60% width and height
    SIZE_4_5 = "size-4/5"      # 80% width and height
    SIZE_1_6 = "size-1/6"      # 16.666667% width and height
    SIZE_2_6 = "size-2/6"      # 33.333333% width and height
    SIZE_3_6 = "size-3/6"      # 50% width and height
    SIZE_4_6 = "size-4/6"      # 66.666667% width and height
    SIZE_5_6 = "size-5/6"      # 83.333333% width and height
    SIZE_1_12 = "size-1/12"    # 8.333333% width and height
    SIZE_2_12 = "size-2/12"    # 16.666667% width and height
    SIZE_3_12 = "size-3/12"    # 25% width and height
    SIZE_4_12 = "size-4/12"    # 33.333333% width and height
    SIZE_5_12 = "size-5/12"    # 41.666667% width and height
    SIZE_6_12 = "size-6/12"    # 50% width and height
    SIZE_7_12 = "size-7/12"    # 58.333333% width and height
    SIZE_8_12 = "size-8/12"    # 66.666667% width and height
    SIZE_9_12 = "size-9/12"    # 75% width and height
    SIZE_10_12 = "size-10/12"  # 83.333333% width and height
    SIZE_11_12 = "size-11/12"  # 91.666667% width and height
    SIZE_FULL = "size-full"    # 100% width and height
    SIZE_MIN = "size-min"      # min-content width and height
    SIZE_MAX = "size-max"      # max-content width and height
    SIZE_FIT = "size-fit"      # fit-content width and height