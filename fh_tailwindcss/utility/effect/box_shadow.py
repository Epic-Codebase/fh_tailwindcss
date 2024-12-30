from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/box-shadow

class BoxShadow(TailwindEnum):
    """
    Utilities for controlling the box shadow of an element.

    Attributes:
        SM (str): A small shadow for minimal emphasis.
            Equivalent to `box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);`.

        DEFAULT (str): The default shadow providing balanced depth.
            Equivalent to `box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);`.

        MD (str): A medium shadow suitable for moderate emphasis.
            Equivalent to `box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);`.

        LG (str): A large shadow for elements requiring higher prominence.
            Equivalent to `box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);`.

        XL (str): An extra-large shadow for significant emphasis.
            Equivalent to `box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);`.

        XXL (str): A prominent shadow with greater spread and softness.
            Equivalent to `box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25);`.

        INNER (str): An inner shadow for inset effects.
            Equivalent to `box-shadow: inset 0 2px 4px 0 rgb(0 0 0 / 0.05);`.

        NONE (str): Removes any applied shadow.
            Equivalent to `box-shadow: 0 0 #0000;`.
    """
    SM = "shadow-sm"
    DEFAULT = "shadow"
    MD = "shadow-md"
    LG = "shadow-lg"
    XL = "shadow-xl"
    XXL = "shadow-2xl"
    INNER = "shadow-inner"
    NONE = "shadow-none"
