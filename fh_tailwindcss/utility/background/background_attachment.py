from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/background-attachment

class BackgroundAttachment(TailwindEnum):
    """
    Enum class representing background-attachment utility classes in Tailwind CSS.
    Used to control the background attachment behavior of elements.

    Attributes:
        BG_FIXED (str): Fixed background attachment.
        BG_LOCAL (str): Local background attachment.
        BG_SCROLL (str): Scroll background attachment.
    """
    BG_FIXED = "bg-fixed"
    BG_LOCAL = "bg-local"
    BG_SCROLL = "bg-scroll"

