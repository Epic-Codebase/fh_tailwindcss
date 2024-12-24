from ..tailwind import TailwindEnum, TailwindDict

# https://tailwindcss.com/docs/gap

class Gap(TailwindEnum):
    """
    Enum class for TailwindCSS gap utilities.
    Represents the gap classes, with specific variants for `gap`, `gap-x`, and `gap-y`.

    Attributes:
        - GAP: "gap-{0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96}"
        - GAP_X: [column] "gap-x-{0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96}"
        - GAP_Y: [row] "gap-y-{0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96}"
        - GAP_PX: "1px"
        - GAP_X_PX: [column] "1px"
        - GAP_Y_PX: [row] "1px"
    """
    
    DEFAULT = "gap"
    GAP_X = "gap-x"
    GAP_Y = "gap-y"
    GAP_PX = "gap-px"
    GAP_X_PX = "gap-x-px"
    GAP_Y_PX = "gap-y-px"


class Gaps(TailwindDict, dict[Gap, int]):
    """
    A dictionary that holds the gap(Gap:int) values for a TailwindCSS component.
    """
    pass
