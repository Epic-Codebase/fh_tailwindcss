from fasthtml.common import fast_app, serve, Meta, Script, Main, Span
from fh_tailwindcss import Grid, GridTemplateColumns, GridColumnStartEnd, LabeledInput, ResponsiveBreakpointStack, ResponsiveBreakpoint, PseudoClass, PseudoClassStack, StateGroup, Width
from fh_tailwindcss.tailwind import Tailwind

app,rt = fast_app(
    pico=False,
    hdrs=(
        Meta(charset="UTF-8"),
    Meta(
        name="viewport",
        content="width=device-width, initial-scale=1.0, maximum-scale=1.0",
    ),
    Meta(
        name="description",
        content="FastHTML template using Tailwind CSS for styling",
    ),
    Script(src="https://cdn.tailwindcss.com")
    ),
    default_hdrs=True,
    htmlkw={"lang": "en"},
    bodykw={"class": "bg-gray-100 dark:bg-gray-900"},
)

@rt('/')
def get(): 
    return Main(
        Grid(
            GridTemplateColumns.COLS_1,
            LabeledInput("ID:", Width.PER1_6, type='text'),
            # md:hover:
            ResponsiveBreakpointStack({
                ResponsiveBreakpoint.DEFAULT: [
                    PseudoClassStack({
                        StateGroup.GROUP_HOVER: [
                            GridTemplateColumns.COLS_1
                        ]
                    })
                ]
            }),                  
        ),
    )


serve()