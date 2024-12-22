from ..tailwind import TailwindEnum, TailwindStack

# https://tailwindcss.com/docs/hover-focus-and-other-states

class AttributeSelector(TailwindEnum):
    DIR_RTL = "[dir=\"rtl\"]"
    DIR_LTR = "[dir=\"ltr\"]"
    OPEN = "[open]"


class AttributeSelectorStack(TailwindStack):
    pass