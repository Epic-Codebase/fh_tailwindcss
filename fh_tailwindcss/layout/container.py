from fastcore.meta import delegates
from fasthtml.common import *
from ..tailwind import Tailwind
from ..style import ScreenMapping, ScreenSize
from .style import ContainerWidth

# https://tailwindcss.com/docs/container

@delegates(ft_hx, keep=True)
class Container(Tailwind):

    DEFAULT_WIDTH = ContainerWidth.NONE

    DEFAULT_SCREEN_MAPPING = ScreenMapping({
        ScreenSize.DEFAULT: [
            DEFAULT_WIDTH,
        ]
    })

    def __init__(self, *w, screen_mapping: ScreenMapping = DEFAULT_SCREEN_MAPPING, **kwargs):
        """
        A TailwindCSS grid container component.

        args:
            screen_mapping (ScreenMapping, optional): A mapping of screen sizes to container properties. 
                Defaults to DEFAULT_SCREEN_MAPPING.
        """

        screen_mapping = screen_mapping if isinstance(screen_mapping, ScreenMapping) else ScreenMapping(screen_mapping if screen_mapping else {})
        
        super().__init__(*list(w) + [screen_mapping], **kwargs)


    def __ft__(self) -> FT:
        return Div(*self.w, cls=f"{self.__css__()} container".strip(), **self.kwargs)
    