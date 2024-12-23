from fastcore.meta import delegates
from fasthtml.common import ft_hx, FT, Div
from ..tailwind import Tailwind
from ..text import Label
from ..utility import Width, Padding, Paddings, Margin, Margins, FontSize, FontWeight, BorderRadius
from .input import Input

@delegates(ft_hx, keep=True)
class LabeledInput(Tailwind):

    DEFAULT_INPUT_SETTINGS = (
        Width.FULL,
        Paddings({Padding.DEFAULT: 1.5}),
        FontSize.SMALL,
        BorderRadius.LARGE
    )

    DEFAULT_LABEL_SETTINGS = (
        Margins({Margin.TOP: 1, Margin.BOTTOM:1}),
        FontWeight.MEDIUM,
        FontSize.SMALL
    )

    def __init__(self, label: str, *w, label_settings = DEFAULT_LABEL_SETTINGS, input_settings = DEFAULT_INPUT_SETTINGS, **kwargs):
        """A TailwindCSS label and input in a container

        Args:
            label (str): Label text
            *w: Additional input child elements
            **kwargs: Additional input attributes
        """        

        input = Input(*w + tuple(input_settings), **kwargs)
        label = Label(label, *label_settings, fr=getattr(input, 'id', None))

        super().__init__(*list(w) + [label, input], **kwargs)

    def __ft__(self) -> FT:
        """Generates the TailwindCSS label and input in a container."""
        return Div(*self.w, **self.kwargs)
