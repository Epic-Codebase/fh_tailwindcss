from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/background-size

class BackgroundSize(TailwindEnum):
    """
    Enum for TailwindCSS background-size utility classes.
    Represents the background sizing behavior.

    Variants:
    - AUTO: "bg-auto" (background-size: auto;)
    - COVER: "bg-cover" (background-size: cover;)
    - CONTAIN: "bg-contain" (background-size: contain;)
    """
    AUTO = "bg-auto"
    COVER = "bg-cover"
    CONTAIN = "bg-contain"
