from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/background-image

class BackgroundImage(TailwindEnum):
    """
    Enum for TailwindCSS background-image utility classes.
    Represents different background image utilities including gradients.

    Variants:
    - NONE: "bg-none" (background-image: none;)
    - GRADIENT_TO_T: "bg-gradient-to-t" (background-image: linear-gradient(to top, var(--tw-gradient-stops));)
    - GRADIENT_TO_TR: "bg-gradient-to-tr" (background-image: linear-gradient(to top right, var(--tw-gradient-stops));)
    - GRADIENT_TO_R: "bg-gradient-to-r" (background-image: linear-gradient(to right, var(--tw-gradient-stops));)
    - GRADIENT_TO_BR: "bg-gradient-to-br" (background-image: linear-gradient(to bottom right, var(--tw-gradient-stops));)
    - GRADIENT_TO_B: "bg-gradient-to-b" (background-image: linear-gradient(to bottom, var(--tw-gradient-stops));)
    - GRADIENT_TO_BL: "bg-gradient-to-bl" (background-image: linear-gradient(to bottom left, var(--tw-gradient-stops));)
    - GRADIENT_TO_L: "bg-gradient-to-l" (background-image: linear-gradient(to left, var(--tw-gradient-stops));)
    - GRADIENT_TO_TL: "bg-gradient-to-tl" (background-image: linear-gradient(to top left, var(--tw-gradient-stops));)
    """
    NONE = "bg-none"
    GRADIENT_TO_T = "bg-gradient-to-t"
    GRADIENT_TO_TR = "bg-gradient-to-tr"
    GRADIENT_TO_R = "bg-gradient-to-r"
    GRADIENT_TO_BR = "bg-gradient-to-br"
    GRADIENT_TO_B = "bg-gradient-to-b"
    GRADIENT_TO_BL = "bg-gradient-to-bl"
    GRADIENT_TO_L = "bg-gradient-to-l"
    GRADIENT_TO_TL = "bg-gradient-to-tl"
