from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/transition-delay

class TransitionDelay(TailwindEnum):
    """
    Utilities for controlling the delay of CSS transitions.

    Attributes:
        DELAY (str): Sets the transition delay. Available options: [0, 75, 100, 150, 200, 300, 500, 700, 1000] (in milliseconds).
    """

    DELAY = "delay"

class TransitionDelays(TailwindDict):
    pass