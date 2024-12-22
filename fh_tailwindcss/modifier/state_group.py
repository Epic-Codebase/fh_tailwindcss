from ..tailwind import TailwindEnum, TailwindStack

# https://tailwindcss.com/docs/hover-focus-and-other-states

class StateGroup(TailwindEnum):
    GROUP_HOVER = "group-hover"
    GROUP_FOCUS = "group-focus"
    PEER_HOVER = "peer-hover"
    PEER_FOCUS = "peer-focus"
    PEER_CHECKED = "peer-checked"
    PEER_DISABLED = "peer-disabled"
    PEER_REQUIRED = "peer-required"
    PEER_INVALID = "peer-invalid"


class StateGroupStack(TailwindStack):
    pass
