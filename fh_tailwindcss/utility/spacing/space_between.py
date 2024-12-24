from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/space

class SpaceBetween(TailwindEnum):
    """
    Enum class for TailwindCSS space-between utilities.
    Represents the space-x and space-y utilities that apply margin between elements.

    Attributes:
        - SPACE_X: "space-x-{0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96}"
        - SPACE_Y: "space-y-{0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96}"
        - SPACE_X_PX: "space-x-px"
        - SPACE_Y_PX: "space-y-px"
        - SPACE_X_REVERSE: "space-x-reverse"
        - SPACE_Y_REVERSE: "space-y-reverse"
    """
    
    SPACE_X = "space-x"
    SPACE_Y = "space-y"
    SPACE_X_PX = "space-x-px"
    SPACE_Y_PX = "space-y-px"
    SPACE_X_REVERSE = "space-x-reverse"
    SPACE_Y_REVERSE = "space-y-reverse"


class SpacesBetween(TailwindDict, dict[SpaceBetween, float]):
    """
    A dictionary that holds the spaces between (SpaceBetween:float) values for a TailwindCSS component.
    """
    pass