from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/animation

class Animation(TailwindEnum):
    """
    Utilities for animating elements with CSS animations.

    Attributes:
        NONE (str): Disables animation.
        SPIN (str): Applies a spinning animation.
        PING (str): Applies a ping animation.
        PULSE (str): Applies a pulse animation.
        BOUNCE (str): Applies a bouncing animation.
    """

    NONE = "animate-none"
    SPIN = "animate-spin"
    PING = "animate-ping"
    PULSE = "animate-pulse"
    BOUNCE = "animate-bounce"
