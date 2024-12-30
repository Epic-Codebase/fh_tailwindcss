from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/table-layout

class TableLayout(TailwindEnum):
    """
    Utilities for controlling the table layout algorithm.

    Attributes:
        AUTO (str): Sets the table layout to auto.
        FIXED (str): Sets the table layout to fixed.
    """

    AUTO = "table-auto"
    FIXED = "table-fixed"
