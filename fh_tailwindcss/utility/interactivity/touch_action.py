from fh_tailwindcss.tailwind import TailwindEnum

# https://tailwindcss.com/docs/touch-action


class TouchAction(TailwindEnum):
    """
    Utilities for controlling how an element can be scrolled and zoomed on touchscreens.

    Attributes:
        AUTO: Enables default browser handling for touch actions.
        NONE: Disables all touch actions.
        PAN_X: Allows horizontal panning.
        PAN_LEFT: Enables panning only to the left.
        PAN_RIGHT: Enables panning only to the right.
        PAN_Y: Allows vertical panning.
        PAN_UP: Enables panning only upwards.
        PAN_DOWN: Enables panning only downwards.
        PINCH_ZOOM: Enables pinch-to-zoom functionality.
        MANIPULATION: Restricts actions to panning and pinch zooming.
    """

    AUTO = "touch-auto"
    NONE = "touch-none"
    PAN_X = "touch-pan-x"
    PAN_LEFT = "touch-pan-left"
    PAN_RIGHT = "touch-pan-right"
    PAN_Y = "touch-pan-y"
    PAN_UP = "touch-pan-up"
    PAN_DOWN = "touch-pan-down"
    PINCH_ZOOM = "touch-pinch-zoom"
    MANIPULATION = "touch-manipulation"
