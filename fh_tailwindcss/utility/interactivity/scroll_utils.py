from ...tailwind import TailwindDict, TailwindEnum


# https://tailwindcss.com/docs/scroll-behavior

class ScrollBehavior(TailwindEnum):
    """
    Utilities for controlling the scroll behavior of an element.

    Attributes:
        AUTO (str): Sets the scroll behavior to the default (equivalent to `scroll-behavior: auto`).
        SMOOTH (str): Enables smooth scrolling (equivalent to `scroll-behavior: smooth`).
    """
    AUTO = "scroll-auto"
    SMOOTH = "scroll-smooth"


# https://tailwindcss.com/docs/scroll-margin

class ScrollMargin(TailwindEnum):
    """
    Utilities for controlling the scroll offset around items in a snap container.

    Attributes:
        M (str): Defines the scroll-margin for all sides.
                 Possible values: '0', 'px', '0.5', '1', '1.5', '2', '2.5', '3', 
                 '3.5', '4', '5', '6', '7', '8', '9', '10', '11', '12', '14', 
                 '16', '20', '24', '28', '32', '36', '40', '44', '48', '52', 
                 '56', '60', '64', '72', '80', '96', 'auto'.
        MX (str): Defines the horizontal scroll-margin (left and right).
                  Possible values: Same as `M`.
        MY (str): Defines the vertical scroll-margin (top and bottom).
                  Possible values: Same as `M`.
        MT (str): Defines the top scroll-margin.
                  Possible values: Same as `M`.
        MR (str): Defines the right scroll-margin.
                  Possible values: Same as `M`.
        MB (str): Defines the bottom scroll-margin.
                  Possible values: Same as `M`.
        ML (str): Defines the left scroll-margin.
                  Possible values: Same as `M`.
        MS (str): Defines the start inline scroll-margin.
                  Possible values: Same as `M`.
        ME (str): Defines the end inline scroll-margin.
                  Possible values: Same as `M`.
    """
    M = "scroll-m"
    MX = "scroll-mx"
    MY = "scroll-my"
    MT = "scroll-mt"
    MR = "scroll-mr"
    MB = "scroll-mb"
    ML = "scroll-ml"
    MS = "scroll-ms"
    ME = "scroll-me"

class ScrollMargins(TailwindDict):
    pass


# https://tailwindcss.com/docs/scroll-padding

class ScrollPadding(TailwindEnum):
    """
    Utilities for controlling the scroll padding around items in a snap container.

    Attributes:
        P (str): Defines the scroll-padding for all sides.
                 Possible values: '0', 'px', '0.5', '1', '1.5', '2', '2.5', '3', 
                 '3.5', '4', '5', '6', '7', '8', '9', '10', '11', '12', '14', 
                 '16', '20', '24', '28', '32', '36', '40', '44', '48', '52', 
                 '56', '60', '64', '72', '80', '96', 'auto'.
        PX (str): Defines the horizontal scroll-padding (left and right).
                  Possible values: Same as `P`.
        PY (str): Defines the vertical scroll-padding (top and bottom).
                  Possible values: Same as `P`.
        PT (str): Defines the top scroll-padding.
                  Possible values: Same as `P`.
        PR (str): Defines the right scroll-padding.
                  Possible values: Same as `P`.
        PB (str): Defines the bottom scroll-padding.
                  Possible values: Same as `P`.
        PL (str): Defines the left scroll-padding.
                  Possible values: Same as `P`.
        PS (str): Defines the start inline scroll-padding.
                  Possible values: Same as `P`.
        PE (str): Defines the end inline scroll-padding.
                  Possible values: Same as `P`.
    """
    P = "scroll-p"
    PX = "scroll-px"
    PY = "scroll-py"
    PT = "scroll-pt"
    PR = "scroll-pr"
    PB = "scroll-pb"
    PL = "scroll-pl"
    PS = "scroll-ps"
    PE = "scroll-pe"

class ScrollPaddings(TailwindDict):
    pass


# https://tailwindcss.com/docs/scroll-snap-align

class ScrollSnapAlign(TailwindEnum):
    """
    Utilities for controlling the alignment of snap points in a scroll container.

    Attributes:
        START (str): Aligns snap points to the start of the scroll container.
        CENTER (str): Aligns snap points to the center of the scroll container.
        END (str): Aligns snap points to the end of the scroll container.
        NONE (str): Disables alignment of snap points.
    """
    START = "snap-start"
    CENTER = "snap-center"
    END = "snap-end"
    NONE = "snap-align-none"


# https://tailwindcss.com/docs/scroll-snap-stop

class ScrollSnapStop(TailwindEnum):
    """
    Utilities for controlling whether the scroll container should stop on a snap point.

    Attributes:
        NORMAL (str): Allows the scroll container to stop on snap points.
        ALWAYS (str): Forces the scroll container to stop on snap points.
    """
    NORMAL = "snap-normal"
    ALWAYS = "snap-always"


# https://tailwindcss.com/docs/scroll-snap-type

class ScrollSnapType(TailwindEnum):
    """
    Utilities for controlling the scroll snapping behavior of an element.

    Attributes:
        NONE (str): Disables scroll snapping.
        MANDATORY (str): Forces the scroll container to snap to the nearest snap point.
        PROXIMITY (str): Forces the scroll container to snap to the nearest snap point.
        BOTH (str): Forces the scroll container to snap to the nearest snap point.
        MANDATORY (str): Forces the scroll container to snap to the nearest snap point.
        PROXIMITY (str): Forces the scroll container to snap to the nearest snap point.
    """
    NONE = "snap-none"
    MANDATORY = "snap-mandatory"
    PROXIMITY = "snap-proximity"
    BOTH = "snap-both"
    X = "snap-x"
    Y = "snap-y"
