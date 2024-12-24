from fastcore.meta import delegates
from fasthtml.common import *
from ..tailwind import Tailwind
from ..modifier import ResponsiveBreakpoint, ResponsiveBreakpointStack
from ..utility import Display
from .grid_template_columns import GridTemplateColumns
from .grid_template_rows import GridTemplateRows
from .gap import Gap, Gaps

@delegates(ft_hx, keep=True)
class InlineGrid(Tailwind):

    DEFAULT_COLS = GridTemplateColumns.COLS_1
    DEFAULT_ROWS = GridTemplateRows.ROWS_1
    DEFAULT_GAPS = Gaps({Gap.DEFAULT: 4})

    DEFAULT_RESPONSIVE_BREAKPOINT = ResponsiveBreakpointStack({
        ResponsiveBreakpoint.DEFAULT: [
            DEFAULT_COLS,
            DEFAULT_ROWS,
            DEFAULT_GAPS,
        ]
    })

    def __init__(self, *w, **kwargs):
        """
        A TailwindCSS inline grid container component.
        """

        super().__init__(*list(w) + [Display.INLINE_GRID], **kwargs)


    def __ft__(self) -> FT:
        return Div(*self.w, cls=f"{self.__css__()}".strip(), **self.kwargs)