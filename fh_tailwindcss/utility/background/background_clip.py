from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/background-clip

class BackgroundClip(TailwindEnum):
    """
    Enum for TailwindCSS background-clip utility classes.
    Represents different clipping behaviors for the background.

    Variants:
    - BORDER: "bg-clip-border" (background-clip: border-box;)
    - PADDING: "bg-clip-padding" (background-clip: padding-box;)
    - CONTENT: "bg-clip-content" (background-clip: content-box;)
    - TEXT: "bg-clip-text" (background-clip: text;)
    """
    BORDER = "bg-clip-border"
    PADDING = "bg-clip-padding"
    CONTENT = "bg-clip-content"
    TEXT = "bg-clip-text"
