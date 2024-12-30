from ...tailwind import TailwindDict, TailwindEnum

# https://tailwindcss.com/docs/transition-duration

class TransitionDuration(TailwindEnum):
    """
    Utilities for controlling the duration of CSS transitions.

    Attributes:
        DURATION (str): Sets the transition duration. Available options: [0, 75, 100, 150, 200, 300, 500, 700, 1000] (in milliseconds).
    """

    DURATION = "duration"

class TransitionDurations(TailwindDict):
    pass