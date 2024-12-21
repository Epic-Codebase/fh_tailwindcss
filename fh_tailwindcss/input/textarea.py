import fasthtml.common as fh
from fastcore.meta import delegates
from ..tailwind import Tailwind
from ..style import Width, FontSize, BorderRadius

@delegates(fh.ft_hx, keep=True)
class Textarea(Tailwind):
    
    def __init__(self, *w, width: Width = Width.FULL, text_size: FontSize = FontSize.SMALL, border: BorderRadius = BorderRadius.LARGE, **kwargs):
        """
        A TailwindCSS input component.
        Args:
            *w: Variable length argument list for additional positional arguments.
            text_size (TextSize, optional): The text size for the input component. Defaults to TextSize.SMALL.
            border (BorderRadius, optional): The border radius for the input component. Defaults to BorderRadius.LARGE.
            **kwargs: Arbitrary keyword arguments for additional properties.      
        """
        super().__init__(*list(w) + [width, text_size, border], **kwargs)


    def __ft__(self) -> fh.FT:
        """Generates the TailwindCSS input."""
        return fh.Textarea(
            *self.w, 
            cls=f"{self.__css__()} block text-gray-900 bg-gray-50 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500", 
            **self.kwargs),
