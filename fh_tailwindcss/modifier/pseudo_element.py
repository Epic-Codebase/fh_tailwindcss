from ..tailwind import TailwindEnum, TailwindStack

# https://tailwindcss.com/docs/hover-focus-and-other-states

class PseudoElement(TailwindEnum):
    BEFORE = "before"
    AFTER = "after"
    PLACEHOLDER = "placeholder"
    SELECTION = "selection"
    MARKER = "marker"
    FILE_SELECTOR_BUTTON = "file-selector-button"


class PseudoElementStack(TailwindStack):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.separator = '::'