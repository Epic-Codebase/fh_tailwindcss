from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/ring-width

class RingUtilities(TailwindEnum):
    """
    Enum class representing ring utility classes in Tailwind CSS.
    Used to control focus ring appearance around elements.

    Attributes:
        RING (str): Default ring width.
        RING_0 (str): No ring.
        RING_1 (str): Thin ring.
        RING_2 (str): Medium ring.
        RING_4 (str): Thick ring.
        RING_OFFSET (str): Ring offset for outer space.
        RING_COLOR (str): Ring color.
    """
    RING = "ring"
    RING_0 = "ring-0"
    RING_1 = "ring-1"
    RING_2 = "ring-2"
    RING_4 = "ring-4"
    RING_OFFSET = "ring-offset-*"
    RING_COLOR = "ring-*"