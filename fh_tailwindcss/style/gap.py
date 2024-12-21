from ..tailwind import TailwindEnum, TailwindDict

# https://tailwindcss.com/docs/gap

class Gap(TailwindEnum):
    """
    Enum class representing different types of gaps that can be applied in a layout.

    Attributes:
        DEFAULT (str): Applies gap to all sides.
        X (str): Applies horizontal gap (between columns).
        Y (str): Applies vertical gap (between rows).
        TOP (str): Applies gap at the top.
        RIGHT (str): Applies gap at the right.
        BOTTOM (str): Applies gap at the bottom.
        LEFT (str): Applies gap at the left.
    """
    DEFAULT = "gap"
    X = "gap-x"
    Y = "gap-y"

    def __css__(self) -> str:
        return self.value if self else ""
    

class Gaps(TailwindDict, dict[Gap, int]):
    """
    A dictionary that holds the gap(Gap:int) values for a TailwindCSS component.
    """
    pass
