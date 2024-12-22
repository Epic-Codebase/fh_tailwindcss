from fastcore.meta import delegates
from fasthtml.common import *
from ..tailwind import Tailwind
from ..modifier import ResponsiveBreakpoint, ResponsiveBreakpointStack
from ..utility import Margin, Margins, Gap, Gaps, Display
from .grid_template_columns import GridTemplateColumns
from .grid_template_rows import GridTemplateRows

# https://tailwindcss.com/docs/grid-template-columns

@delegates(ft_hx, keep=True)
class Grid(Tailwind):

    DEFAULT_COLS = GridTemplateColumns.COLS_1
    DEFAULT_ROWS = GridTemplateRows.ROWS_1
    DEFAULT_GAPS = Gaps({Gap.DEFAULT: 2})
    DEFAULT_MARGINS = Margins({Margin.TOP: 1, Margin.BOTTOM: 1})

    DEFAULT_RESPONSIVE_BREAKPOINT = ResponsiveBreakpointStack({
        ResponsiveBreakpoint.DEFAULT: [
            DEFAULT_COLS,
            DEFAULT_ROWS,
            DEFAULT_GAPS,
            DEFAULT_MARGINS,
        ]
    })

    def __init__(self, *w, **kwargs):
        """
        A TailwindCSS grid container component.

        args:
            screen_mapping (ScreenMapping, optional): A mapping of screen sizes to grid properties. 
                Defaults to DEFAULT_SCREEN_MAPPING.
        """
        
        super().__init__(*list(w) + [Display.GRID], **kwargs)


    def __ft__(self) -> FT:
        return Div(*self.w, cls=f"{self.__css__()}".strip(), **self.kwargs)
    