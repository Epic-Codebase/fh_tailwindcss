from ...tailwind import TailwindEnum, TailwindRaw

# https://tailwindcss.com/docs/max-width

class MaxWidth(TailwindEnum):
    """
    Enum class representing container width breakpoints for Tailwind CSS.

    Attributes:
        NONE (str): No width constraint.
        SMALL (str): max-width: 640px.
        MEDIUM (str): max-width: 768px.
        LARGE (str): max-width: 1024px.
        XLARGE (str): max-width: 1280px.
        XLARGE2 (str): max-width: 1536px.

    Methods:
        arbitrary (str): Supports arbitrary values. e.g. max-w-[220px]
    """
    
    NONE = "max-w-none"      # No width constraint
    SMALL = "max-w-sm"       # max-width: 640px
    MEDIUM = "max-w-md"      # max-width: 768px
    LARGE = "max-w-lg"       # max-width: 1024px
    XLARGE = "max-w-xl"      # max-width: 1280px
    XLARGE2 = "max-w-2xl"    # max-width: 1536px


    @staticmethod
    def arbitrary(val) -> TailwindRaw:
        return TailwindRaw(f"max-w-[{val}]")
    