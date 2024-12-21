from fasthtml.common import fast_app, serve, Meta, Script, Main
from fh_tailwindcss import Container, ContainerWidth, GridContainer, GridColumns, LabeledInput, LabeledTextarea, ScreenSize, Margins, Margin, Gaps, Gap, Paddings, Padding, Width

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
        Container(
            GridContainer(
                GridContainer(
                    LabeledInput("ID:", type='text'),
                    screen_mapping={                
                        ScreenSize.DEFAULT: [
                            GridColumns.COLS_1,
                            Width.PER1_6,
                        ]
                    },       
                ),
                GridContainer(
                    LabeledInput("COD:", type='text'),
                    screen_mapping={                
                        ScreenSize.DEFAULT: [
                            GridColumns.COLS_1,
                            Width.PER1_6,
                        ]
                    },       
                ),
                screen_mapping={                
                    ScreenSize.SMALL: [
                        GridColumns.COLS_2
                    ]
                }, 
            ),
            GridContainer(
                LabeledInput("Email:", type='text', placeholder='Enter your email'),            
            ),
            GridContainer(
                LabeledInput("User Name:", type='text', placeholder='Enter your user name'),
                LabeledInput("Password:", type='text', placeholder='Enter your password'),
                screen_mapping={                
                    ScreenSize.SMALL: [
                        GridColumns.COLS_2,
                        GridContainer.DEFAULT_GAPS,
                        GridContainer.DEFAULT_MARGINS,
                    ]
                }, 
            ),
            GridContainer(            
                LabeledInput("Gender:", type='text', placeholder='Enter your gender'),
                LabeledInput("Phone:", type='text', placeholder='Enter your phone'),
                LabeledInput("Age:", type='number', placeholder='Enter your age'),
                screen_mapping={                
                    ScreenSize.DEFAULT: [
                        GridColumns.COLS_3,
                        Gaps({
                            Gap.DEFAULT: 2}),
                        Margins({
                            Margin.TOP: 1, 
                            Margin.BOTTOM: 1}),
                    ]
                },
            ),
            GridContainer(
                LabeledTextarea("Details:", type='text', rows=4),
                screen_mapping={                
                    ScreenSize.DEFAULT: [
                        GridContainer.DEFAULT_COLS,
                        Paddings({Padding.DEFAULT: 5}),
                    ]
                },
            ),          
            ContainerWidth.XLARGE2,
            screen_mapping=None, # If you don't care for screen sizes...
        )
    )

serve()