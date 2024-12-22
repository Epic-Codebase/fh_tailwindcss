from ..tailwind import TailwindEnum, TailwindStack

# https://tailwindcss.com/docs/hover-focus-and-other-states

class FeatureQuery(TailwindEnum):
    MOTION_SAFE = "motion-safe"
    MOTION_REDUCE = "motion-reduce"
    CONTRAST_MORE = "contrast-more"
    CONTRAST_LESS = "contrast-less"


class FeatureQueryStack(TailwindStack):
    pass