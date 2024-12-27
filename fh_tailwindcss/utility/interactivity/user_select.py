from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/user-select

class UserSelect(TailwindEnum):
    """
    Utilities for controlling whether the user can select text in an element.

    Attributes:
        NONE: Prevents text selection.
        TEXT: Allows text selection.
        ALL: Allows selection of all content.
        AUTO: Enables default text selection behavior.
    """

    NONE = "select-none"
    TEXT = "select-text"
    ALL = "select-all"
    AUTO = "select-auto"
