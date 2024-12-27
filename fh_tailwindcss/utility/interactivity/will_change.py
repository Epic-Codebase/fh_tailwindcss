from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/will-change

class WillChange(TailwindEnum):
    """
    Utilities for optimizing upcoming animations of elements that are expected to change.

    Attributes:
        AUTO: Default browser handling for changes.
        SCROLL: Optimizes scroll-position changes.
        CONTENTS: Optimizes content changes.
        TRANSFORM: Optimizes transform property changes.
    """

    AUTO = "will-change-auto"
    SCROLL = "will-change-scroll"
    CONTENTS = "will-change-contents"
    TRANSFORM = "will-change-transform"