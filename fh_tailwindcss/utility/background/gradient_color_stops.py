from ...tailwind import TailwindEnum, TailwindDict

# Enum for TailwindCSS gradient color stops
class GradientColorStop(TailwindEnum):
    """
    Enum for TailwindCSS gradient color stops utility classes.
    Represents the abstract class names. Refer to the documentation for specific variants.

    Variants for each enum:
    - INHERIT: "from-inherit" (gradient color stop: inherit;)
    - CURRENT: "from-current" (gradient color stop: currentColor;)
    - TRANSPARENT: "from-transparent" (gradient color stop: transparent;)
    - BLACK: "from-black" (gradient color stop: rgb(0 0 0 / var(--tw-bg-opacity, 1));)
    - WHITE: "from-white" (gradient color stop: rgb(255 255 255 / var(--tw-bg-opacity, 1));)
    - SLATE: "from-slate-{50,100,200,300,400,500,600,700,800,900,950}"
    - GRAY: "from-gray-{50,100,200,300,400,500,600,700,800,900,950}"
    - ZINC: "from-zinc-{50,100,200,300,400,500,600,700,800,900,950}"
    - NEUTRAL: "from-neutral-{50,100,200,300,400,500,600,700,800,900,950}"
    - STONE: "from-stone-{50,100,200,300,400,500,600,700,800,900,950}"
    - RED: "from-red-{50,100,200,300,400,500,600,700,800,900,950}"
    - ORANGE: "from-orange-{50,100,200,300,400,500,600,700,800,900,950}"
    - AMBER: "from-amber-{50,100,200,300,400,500,600,700,800,900,950}"
    - YELLOW: "from-yellow-{50,100,200,300,400,500,600,700,800,900,950}"
    - LIME: "from-lime-{50,100,200,300,400,500,600,700,800,900,950}"
    - GREEN: "from-green-{50,100,200,300,400,500,600,700,800,900,950}"
    - EMERALD: "from-emerald-{50,100,200,300,400,500,600,700,800,900,950}"
    - TEAL: "from-teal-{50,100,200,300,400,500,600,700,800,900,950}"
    - CYAN: "from-cyan-{50,100,200,300,400,500,600,700,800,900,950}"
    - SKY: "from-sky-{50,100,200,300,400,500,600,700,800,900,950}"
    - BLUE: "from-blue-{50,100,200,300,400,500,600,700,800,900,950}"
    - INDIGO: "from-indigo-{50,100,200,300,400,500,600,700,800,900,950}"
    - VIOLET: "from-violet-{50,100,200,300,400,500,600,700,800,900,950}"
    - PURPLE: "from-purple-{50,100,200,300,400,500,600,700,800,900,950}"
    - FUCHSIA: "from-fuchsia-{50,100,200,300,400,500,600,700,800,900,950}"
    - PINK: "from-pink-{50,100,200,300,400,500,600,700,800,900,950}"
    - ROSE: "from-rose-{50,100,200,300,400,500,600,700,800,900,950}"

    * The same applies for 'FROM', 'VIA', and 'TO' 
    """

    FROM_INHERIT = "from-inherit"
    FROM_CURRENT = "from-current"
    FROM_TRANSPARENT = "from-transparent"
    FROM_BLACK = "from-black"
    FROM_WHITE = "from-white"
    FROM_SLATE = "from-slate"
    FROM_GRAY = "from-gray"
    FROM_ZINC = "from-zinc"
    FROM_NEUTRAL = "from-neutral"
    FROM_STONE = "from-stone"
    FROM_RED = "from-red"
    FROM_ORANGE = "from-orange"
    FROM_AMBER = "from-amber"
    FROM_YELLOW = "from-yellow"
    FROM_LIME = "from-lime"
    FROM_GREEN = "from-green"
    FROM_EMERALD = "from-emerald"
    FROM_TEAL = "from-teal"
    FROM_CYAN = "from-cyan"
    FROM_SKY = "from-sky"
    FROM_BLUE = "from-blue"
    FROM_INDIGO = "from-indigo"
    FROM_VIOLET = "from-violet"
    FROM_PURPLE = "from-purple"
    FROM_FUCHSIA = "from-fuchsia"
    FROM_PINK = "from-pink"
    FROM_ROSE = "from-rose"

    VIA_INHERIT = "via-inherit"
    VIA_CURRENT = "via-current"
    VIA_TRANSPARENT = "via-transparent"
    VIA_BLACK = "via-black"
    VIA_WHITE = "via-white"
    VIA_SLATE = "via-slate"
    VIA_GRAY = "via-gray"
    VIA_ZINC = "via-zinc"
    VIA_NEUTRAL = "via-neutral"
    VIA_STONE = "via-stone"
    VIA_RED = "via-red"
    VIA_ORANGE = "via-orange"
    VIA_AMBER = "via-amber"
    VIA_YELLOW = "via-yellow"
    VIA_LIME = "via-lime"
    VIA_GREEN = "via-green"
    VIA_EMERALD = "via-emerald"
    VIA_TEAL = "via-teal"
    VIA_CYAN = "via-cyan"
    VIA_SKY = "via-sky"
    VIA_BLUE = "via-blue"
    VIA_INDIGO = "via-indigo"
    VIA_VIOLET = "via-violet"
    VIA_PURPLE = "via-purple"
    VIA_FUCHSIA = "via-fuchsia"
    VIA_PINK = "via-pink"
    VIA_ROSE = "via-rose"

    TO_INHERIT = "to-inherit"
    TO_CURRENT = "to-current"
    TO_TRANSPARENT = "to-transparent"
    TO_BLACK = "to-black"
    TO_WHITE = "to-white"
    TO_SLAATE = "to-slate"
    TO_GRAY = "to-gray"
    TO_ZINC = "to-zinc"
    TO_NEUTRAL = "to-neutral"
    TO_STONE = "to-stone"
    TO_RED = "to-red"
    TO_ORANGE = "to-orange"
    TO_AMBER = "to-amber"
    TO_YELLOW = "to-yellow"
    TO_LIME = "to-lime"
    TO_GREEN = "to-green"
    TO_EMERALD = "to-emerald"
    TO_TEAL = "to-teal"
    TO_CYAN = "to-cyan"


class GradientColorStops(TailwindDict):
    """
    A class representing the gradient color stops utility in Tailwind CSS.
    """

    pass