from ..tailwind import TailwindEnum

# https://tailwindcss.com/docs/grid-column

class GridColumnStartEnd(TailwindEnum):
    """
    Enum class representing grid column utilities in Tailwind CSS.

    Attributes:
        AUTO (str): Sets the grid column to auto.
        SPAN_1 to SPAN_12 (str): Sets the grid column to span from 1 to 12.
        SPAN_FULL (str): Sets the grid column to span the full width.
        START_1 to START_13 (str): Sets the grid column start position from 1 to 13.
        START_AUTO (str): Sets the grid column start to auto.
        END_1 to END_13 (str): Sets the grid column end position from 1 to 13.
        END_AUTO (str): Sets the grid column end to auto.
    """

    AUTO = "col-auto"                # grid-column: auto;
    SPAN_1 = "col-span-1"            # grid-column: span 1 / span 1;
    SPAN_2 = "col-span-2"            # grid-column: span 2 / span 2;
    SPAN_3 = "col-span-3"            # grid-column: span 3 / span 3;
    SPAN_4 = "col-span-4"            # grid-column: span 4 / span 4;
    SPAN_5 = "col-span-5"            # grid-column: span 5 / span 5;
    SPAN_6 = "col-span-6"            # grid-column: span 6 / span 6;
    SPAN_7 = "col-span-7"            # grid-column: span 7 / span 7;
    SPAN_8 = "col-span-8"            # grid-column: span 8 / span 8;
    SPAN_9 = "col-span-9"            # grid-column: span 9 / span 9;
    SPAN_10 = "col-span-10"          # grid-column: span 10 / span 10;
    SPAN_11 = "col-span-11"          # grid-column: span 11 / span 11;
    SPAN_12 = "col-span-12"          # grid-column: span 12 / span 12;
    SPAN_FULL = "col-span-full"      # grid-column: 1 / -1;

    START_1 = "col-start-1"          # grid-column-start: 1;
    START_2 = "col-start-2"          # grid-column-start: 2;
    START_3 = "col-start-3"          # grid-column-start: 3;
    START_4 = "col-start-4"          # grid-column-start: 4;
    START_5 = "col-start-5"          # grid-column-start: 5;
    START_6 = "col-start-6"          # grid-column-start: 6;
    START_7 = "col-start-7"          # grid-column-start: 7;
    START_8 = "col-start-8"          # grid-column-start: 8;
    START_9 = "col-start-9"          # grid-column-start: 9;
    START_10 = "col-start-10"        # grid-column-start: 10;
    START_11 = "col-start-11"        # grid-column-start: 11;
    START_12 = "col-start-12"        # grid-column-start: 12;
    START_13 = "col-start-13"        # grid-column-start: 13;
    START_AUTO = "col-start-auto"    # grid-column-start: auto;

    END_1 = "col-end-1"              # grid-column-end: 1;
    END_2 = "col-end-2"              # grid-column-end: 2;
    END_3 = "col-end-3"              # grid-column-end: 3;
    END_4 = "col-end-4"              # grid-column-end: 4;
    END_5 = "col-end-5"              # grid-column-end: 5;
    END_6 = "col-end-6"              # grid-column-end: 6;
    END_7 = "col-end-7"              # grid-column-end: 7;
    END_8 = "col-end-8"              # grid-column-end: 8;
    END_9 = "col-end-9"              # grid-column-end: 9;
    END_10 = "col-end-10"            # grid-column-end: 10;
    END_11 = "col-end-11"            # grid-column-end: 11;
    END_12 = "col-end-12"            # grid-column-end: 12;
    END_13 = "col-end-13"            # grid-column-end: 13;
    END_AUTO = "col-end-auto"        # grid-column-end: auto;
