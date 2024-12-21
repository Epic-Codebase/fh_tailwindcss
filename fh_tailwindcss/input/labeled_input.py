from fastcore.meta import delegates
from fasthtml.common import ft_hx, FT, Div
from ..tailwind import Tailwind
from ..text import Label
from ..style import Padding, Paddings
from .input import Input

@delegates(ft_hx, keep=True)
class LabeledInput(Tailwind):
    
    def __init__(self, label: str | Label, *w, input: Input = None, **kwargs):
        """A TailwindCSS label and input in a container

        Args:
            label (str): Label text
            *w: Additional input child elements
            **kwargs: Additional input attributes
        """

        input = input or Input(*w, Paddings({Padding.DEFAULT: 1.5}), **kwargs)
        label = label if isinstance(label, Label) else Label(label, fr=getattr(input, 'id', None))

        super().__init__(*list(w) + [label, input], **kwargs)

    def __ft__(self) -> FT:
        """Generates the TailwindCSS label and input in a container."""
        return Div(*self.w, **self.kwargs)
