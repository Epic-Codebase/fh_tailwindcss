from ...tailwind import TailwindEnum

class Resize(TailwindEnum):
    """
    Utilities for controlling how an element can be resized.

    Attributes:
        NONE (str): Disables resizing on the element (equivalent to `resize: none`).
        Y (str): Allows vertical resizing (equivalent to `resize: vertical`).
        X (str): Allows horizontal resizing (equivalent to `resize: horizontal`).
        DEFAULT (str): Allows both vertical and horizontal resizing (equivalent to `resize: both`).
    """
    NONE = "resize-none"
    Y = "resize-y"
    X = "resize-x"
    DEFAULT = "resize"
