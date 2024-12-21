from fastcore.meta import delegates
from fasthtml.common import *
from ..tailwind import Tailwind
from ..style import ScreenMapping, ScreenSize, Margin, Margins, Gap, Gaps
from .grid_columns import GridColumns

# https://tailwindcss.com/docs/grid-template-columns

@delegates(ft_hx, keep=True)
class GridContainer(Tailwind):

    DEFAULT_COLS = GridColumns.COLS_1
    DEFAULT_GAPS = Gaps({Gap.DEFAULT: 2})
    DEFAULT_MARGINS = Margins({Margin.TOP: 1, Margin.BOTTOM: 1})

    DEFAULT_SCREEN_MAPPING = ScreenMapping({
        ScreenSize.DEFAULT: [
            DEFAULT_COLS,
            DEFAULT_GAPS,
            DEFAULT_MARGINS,
        ]
    })

    def __init__(self, *w, screen_mapping: ScreenMapping = DEFAULT_SCREEN_MAPPING, **kwargs):
        """
        A TailwindCSS grid container component.

        args:
            screen_mapping (ScreenMapping, optional): A mapping of screen sizes to grid properties. 
                Defaults to DEFAULT_SCREEN_MAPPING.
        """
        
        screen_mapping = screen_mapping if isinstance(screen_mapping, ScreenMapping) else ScreenMapping(screen_mapping if screen_mapping else {})
        
        super().__init__(*list(w) + [screen_mapping], **kwargs)


    def __ft__(self) -> FT:
        return Div(*self.w, cls=f"grid {self.__css__()}".strip(), **self.kwargs)
    