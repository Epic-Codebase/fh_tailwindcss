from ..tailwind import TailwindEnum, TailwindStack

# https://tailwindcss.com/docs/hover-focus-and-other-states

class PseudoClass(TailwindEnum):
    HOVER = "hover"
    FOCUS = "focus"
    FOCUS_WITHIN = "focus-within"
    FOCUS_VISIBLE = "focus-visible"
    ACTIVE = "active"
    VISITED = "visited"
    TARGET = "target"
    FIRST = "first"
    LAST = "last"
    ONLY = "only"
    ODD = "odd"
    EVEN = "even"
    FIRST_OF_TYPE = "first-of-type"
    LAST_OF_TYPE = "last-of-type"
    ONLY_OF_TYPE = "only-of-type"
    EMPTY = "empty"
    DISABLED = "disabled"
    ENABLED = "enabled"
    CHECKED = "checked"
    INDETERMINATE = "indeterminate"
    DEFAULT = "default"
    REQUIRED = "required"
    VALID = "valid"
    INVALID = "invalid"
    IN_RANGE = "in-range"
    OUT_OF_RANGE = "out-of-range"
    PLACEHOLDER_SHOWN = "placeholder-shown"
    AUTOFILL = "autofill"
    READ_ONLY = "read-only"
    READ_WRITE = "read-write"
    
    
class PseudoClassStack(TailwindStack):
    pass
