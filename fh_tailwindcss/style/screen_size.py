from ..tailwind import TailwindEnum

# https://tailwindcss.com/docs/screens#configuring-custom-screens

class ScreenSize(TailwindEnum):
    DEFAULT = ""    # Default screen size.
    SMALL = "sm"    # Small screen size. Typically used for devices with a width of 640px or more.
    MEDIUM = "md"   # Medium screen size. Typically used for devices with a width of 768px or more.
    LARGE = "lg"    # Large screen size. Typically used for devices with a width of 1024px or more. 
    XLARGE = "xl"   # Extra-large screen size. Typically used for devices with a width of 1280px or more.
    XLARGE2 = "2xl" # 2X-large screen size. Typically used for devices with a width of 1536px or more.