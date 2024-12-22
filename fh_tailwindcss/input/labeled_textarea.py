from fastcore.meta import delegates
from fasthtml.common import ft_hx, FT, Div
from ..tailwind import Tailwind
from ..text import Label
from ..utility import Padding, Paddings
from .textarea import Textarea

@delegates(ft_hx, keep=True)
class LabeledTextarea(Tailwind):
    
    def __init__(self, label: str | Label, *w, textarea: Textarea = None, **kwargs):
        """A TailwindCSS label and input in a container

        Args:
            label (str): Label text
            *w: Additional input child elements
            **kwargs: Additional input attributes
        """

        textarea = textarea or Textarea(*w, Paddings({Padding.DEFAULT: 1.5}), **kwargs)
        label = label if isinstance(label, Label) else Label(label, fr=getattr(textarea, 'id', None))

        super().__init__(*list(w) + [label, textarea], **kwargs)

    def __ft__(self) -> FT:
        """Generates the TailwindCSS label and input in a container."""
        
        return Div(*self.w, **self.kwargs)
