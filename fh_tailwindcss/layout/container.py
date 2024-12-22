from fastcore.meta import delegates
from fasthtml.common import *
from ..tailwind import Tailwind
from ..modifier import ResponsiveBreakpoint, ResponsiveBreakpointStack
from ..utility import MaxWidth

# https://tailwindcss.com/docs/container

@delegates(ft_hx, keep=True)
class Container(Tailwind):

    DEFAULT_WIDTH = MaxWidth.NONE

    DEFAULT_RESPONSIVE_BREAKPOINT = ResponsiveBreakpointStack({
        ResponsiveBreakpoint.DEFAULT: [
            DEFAULT_WIDTH,
        ]
    })

    def __init__(self, *w, **kwargs):
        """
        A TailwindCSS grid container component.

        args:
            screen_mapping (ScreenMapping, optional): A mapping of screen sizes to container properties. 
                Defaults to DEFAULT_SCREEN_MAPPING.
        """

        super().__init__(*w, **kwargs)


    def __ft__(self) -> FT:
        return Div(*self.w, cls=f"{self.__css__()} container".strip(), **self.kwargs)
    