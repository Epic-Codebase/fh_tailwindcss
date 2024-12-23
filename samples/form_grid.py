from fasthtml.common import fast_app, serve, Meta, Script, Main, Span
from fh_tailwindcss import *

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
    input_settings= (
        Paddings({Padding.DEFAULT: 1.5}),
        FontSize.SMALL,
        BorderRadius.LARGE,
    )
    
    id_input_settings = (
        *input_settings,
        Width.REM20,
        # sm:hover:w-full
        # sm:focus:border-purple-500
        ResponsiveBreakpointStack({
            ResponsiveBreakpoint.SMALL: [     
                PseudoClassStack({
                    PseudoClass.HOVER: [Width.FULL],
                    PseudoClass.FOCUS: [BorderColors({BorderColor.BORDER_PURPLE: 500})]
                })
            ]
        }),  
    )

    email_input_settings = (
        *input_settings,
        Width.PER1_4,
        # invalid:border-pink-500
        PseudoClassStack({
            PseudoClass.INVALID: [BorderColors({BorderColor.BORDER_PINK: 500})]    
        }) 
    )

    return Main(
        Grid(
            Gaps({Gap.DEFAULT: 2}),
            GridTemplateColumns.COLS_1,
            Margins({Margin.TOP: 1, Margin.BOTTOM: 1}),
            LabeledInput("ID:", input_settings=id_input_settings, type='text'),
            LabeledInput("Email", input_settings=email_input_settings, type="email")        
        ),
    )


serve()