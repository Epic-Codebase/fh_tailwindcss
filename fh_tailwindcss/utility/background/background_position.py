from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/background-position

class BackgroundPosition(TailwindEnum):
    """
    Enum for TailwindCSS background-position utility classes.
    Represents different positions for background images.

    Variants:
    - BOTTOM: "bg-bottom" (background-position: bottom;)
    - CENTER: "bg-center" (background-position: center;)
    - LEFT: "bg-left" (background-position: left;)
    - LEFT_BOTTOM: "bg-left-bottom" (background-position: left bottom;)
    - LEFT_TOP: "bg-left-top" (background-position: left top;)
    - RIGHT: "bg-right" (background-position: right;)
    - RIGHT_BOTTOM: "bg-right-bottom" (background-position: right bottom;)
    - RIGHT_TOP: "bg-right-top" (background-position: right top;)
    - TOP: "bg-top" (background-position: top;)
    """
    BOTTOM = "bg-bottom"
    CENTER = "bg-center"
    LEFT = "bg-left"
    LEFT_BOTTOM = "bg-left-bottom"
    LEFT_TOP = "bg-left-top"
    RIGHT = "bg-right"
    RIGHT_BOTTOM = "bg-right-bottom"
    RIGHT_TOP = "bg-right-top"
    TOP = "bg-top"
