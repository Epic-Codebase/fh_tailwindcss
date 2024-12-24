from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/background-origin

class BackgroundOrigin(TailwindEnum):
    """
    Enum for TailwindCSS background-origin utility classes.
    Represents different origins for the background positioning area.

    Variants:
    - BORDER: "bg-origin-border" (background-origin: border-box;)
    - PADDING: "bg-origin-padding" (background-origin: padding-box;)
    - CONTENT: "bg-origin-content" (background-origin: content-box;)
    """
    BORDER = "bg-origin-border"
    PADDING = "bg-origin-padding"
    CONTENT = "bg-origin-content"
