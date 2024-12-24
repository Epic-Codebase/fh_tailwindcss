from ...tailwind import TailwindEnum, TailwindDict

# https://tailwindcss.com/docs/background-color

class BackgroundColor(TailwindEnum):
    """
    Enum for TailwindCSS background color utility classes.
    Represents the abstract class names. Refer to the documentation for specific variants.

    Variants for each enum:
    - INHERIT: "bg-inherit" (background-color: inherit;)
    - CURRENT: "bg-current" (background-color: currentColor;)
    - TRANSPARENT: "bg-transparent" (background-color: transparent;)
    - BLACK: "bg-black" (background-color: rgb(0 0 0 / var(--tw-bg-opacity, 1));)
    - WHITE: "bg-white" (background-color: rgb(255 255 255 / var(--tw-bg-opacity, 1));)
    - SLATE: "bg-slate-{50,100,200,300,400,500,600,700,800,900,950}"
    - GRAY: "bg-gray-{50,100,200,300,400,500,600,700,800,900,950}"
    - ZINC: "bg-zinc-{50,100,200,300,400,500,600,700,800,900,950}"
    - NEUTRAL: "bg-neutral-{50,100,200,300,400,500,600,700,800,900,950}"
    - STONE: "bg-stone-{50,100,200,300,400,500,600,700,800,900,950}"
    - RED: "bg-red-{50,100,200,300,400,500,600,700,800,900,950}"
    - ORANGE: "bg-orange-{50,100,200,300,400,500,600,700,800,900,950}"
    - AMBER: "bg-amber-{50,100,200,300,400,500,600,700,800,900,950}"
    - YELLOW: "bg-yellow-{50,100,200,300,400,500,600,700,800,900,950}"
    - LIME: "bg-lime-{50,100,200,300,400,500,600,700,800,900,950}"
    - GREEN: "bg-green-{50,100,200,300,400,500,600,700,800,900,950}"
    - EMERALD: "bg-emerald-{50,100,200,300,400,500,600,700,800,900,950}"
    - TEAL: "bg-teal-{50,100,200,300,400,500,600,700,800,900,950}"
    - CYAN: "bg-cyan-{50,100,200,300,400,500,600,700,800,900,950}"
    - SKY: "bg-sky-{50,100,200,300,400,500,600,700,800,900,950}"
    - BLUE: "bg-blue-{50,100,200,300,400,500,600,700,800,900,950}"
    - INDIGO: "bg-indigo-{50,100,200,300,400,500,600,700,800,900,950}"
    - VIOLET: "bg-violet-{50,100,200,300,400,500,600,700,800,900,950}"
    - PURPLE: "bg-purple-{50,100,200,300,400,500,600,700,800,900,950}"
    - FUCHSIA: "bg-fuchsia-{50,100,200,300,400,500,600,700,800,900,950}"
    - PINK: "bg-pink-{50,100,200,300,400,500,600,700,800,900,950}"
    - ROSE: "bg-rose-{50,100,200,300,400,500,600,700,800,900,950}"
    """
    
    INHERIT = "bg-inherit"
    CURRENT = "bg-current"
    TRANSPARENT = "bg-transparent"
    BLACK = "bg-black"
    WHITE = "bg-white"
    SLATE = "bg-slate"
    GRAY = "bg-gray"
    ZINC = "bg-zinc"
    NEUTRAL = "bg-neutral"
    STONE = "bg-stone"
    RED = "bg-red"
    ORANGE = "bg-orange"
    AMBER = "bg-amber"
    YELLOW = "bg-yellow"
    LIME = "bg-lime"
    GREEN = "bg-green"
    EMERALD = "bg-emerald"
    TEAL = "bg-teal"
    CYAN = "bg-cyan"
    SKY = "bg-sky"
    BLUE = "bg-blue"
    INDIGO = "bg-indigo"
    VIOLET = "bg-violet"
    PURPLE = "bg-purple"
    FUCHSIA = "bg-fuchsia"
    PINK = "bg-pink"
    ROSE = "bg-rose"

class BackgroundColors(TailwindDict):
    pass