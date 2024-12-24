from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/background-repeat

class BackgroundRepeat(TailwindEnum):
    """
    Enum for TailwindCSS background-repeat utility classes.
    Represents the background repeat behavior.

    Variants:
    - REPEAT: "bg-repeat" (background-repeat: repeat;)
    - NO_REPEAT: "bg-no-repeat" (background-repeat: no-repeat;)
    - REPEAT_X: "bg-repeat-x" (background-repeat: repeat-x;)
    - REPEAT_Y: "bg-repeat-y" (background-repeat: repeat-y;)
    - REPEAT_ROUND: "bg-repeat-round" (background-repeat: round;)
    - REPEAT_SPACE: "bg-repeat-space" (background-repeat: space;)
    """
    REPEAT = "bg-repeat"
    NO_REPEAT = "bg-no-repeat"
    REPEAT_X = "bg-repeat-x"
    REPEAT_Y = "bg-repeat-y"
    REPEAT_ROUND = "bg-repeat-round"
    REPEAT_SPACE = "bg-repeat-space"
