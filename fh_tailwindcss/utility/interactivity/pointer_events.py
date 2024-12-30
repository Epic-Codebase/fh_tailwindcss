from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/pointer-events

class PointerEvents(TailwindEnum):
    """
    Utilities for controlling whether an element responds to pointer events.

    Attributes:
        NONE (str): Disables pointer events on the element (equivalent to `pointer-events: none`).
        AUTO (str): Enables pointer events on the element (equivalent to `pointer-events: auto`).
    """
    NONE = "pointer-events-none"
    AUTO = "pointer-events-auto"
