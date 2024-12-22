import fasthtml.common as fh
from fastcore.meta import delegates
from ..tailwind import Tailwind
from ..utility import Margins, Margin, FontWeight, FontSize

@delegates(fh.ft_hx, keep=True)
class Label(Tailwind):
    
    def __init__(self, label: str, *w, margins: Margins = Margins({Margin.TOP: 1, Margin.BOTTOM:1}), font_weight: FontWeight = FontWeight.MEDIUM, font_size: FontSize = FontSize.SMALL, **kwargs):
        """
        A TailwindCSS label component.

        args: 
            label (str): Label text.
            *w: Additional input child elements.
            margins (Margins, optional): Margins for the label. Defaults to Margins({Margin.TOP: 1, Margin.BOTTOM: 1}).
            font_weight (FontWeight, optional): Font weight for the label. Defaults to FontWeight.MEDIUM.
            font_size (FontSize, optional): Font size for the label. Defaults to FontSize.SMALL.
            **kwargs: Additional input attributes.
        """

        super().__init__(*list(w) + [label, margins, font_weight, font_size], **kwargs)
        

    def __ft__(self) -> fh.FT:
        """Generates the TailwindCSS label."""
        return fh.Label(
            *self.w,          
            cls=f"{self.__css__()} block text-gray-900 dark:text-white".strip(),
            **self.kwargs
        ),