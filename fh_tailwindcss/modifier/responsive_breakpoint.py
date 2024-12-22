from ..tailwind import TailwindEnum, TailwindStack

# https://tailwindcss.com/docs/hover-focus-and-other-states
# https://tailwindcss.com/docs/responsive-design

class ResponsiveBreakpoint(TailwindEnum):
    """
    Breakpoint enumeration for Tailwind CSS screen sizes.
    This class defines the various screen size breakpoints used in Tailwind CSS.
    Each breakpoint corresponds to a specific minimum screen width.
    Attributes:
        DEFAULT (str): Default screen size.
        SMALL (str): Small screen size. Typically used for devices with a width of 640px or more.
        MEDIUM (str): Medium screen size. Typically used for devices with a width of 768px or more.
        LARGE (str): Large screen size. Typically used for devices with a width of 1024px or more.
        XLARGE (str): Extra-large screen size. Typically used for devices with a width of 1280px or more.
        XLARGE2 (str): 2X-large screen size. Typically used for devices with a width of 1536px or more.
    """

    DEFAULT = ""
    SMALL = "sm"
    MEDIUM = "md"
    LARGE = "lg"
    XLARGE = "xl"
    XLARGE2 = "2xl"


class ResponsiveBreakpointStack(TailwindStack):
    pass