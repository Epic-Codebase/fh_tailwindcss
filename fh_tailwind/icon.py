from fastcore.meta import delegates
from fasthtml.common import *
from .tailwind import Tailwind

@delegates(ft_hx, keep=True)
class Icon(Tailwind):

    def __init__(self, name: str, size: str = None, **kwargs):
        """A TailwindCSS icon component.
        
        Args:
            name (str): The name of the icon.
                e.g. "modal-close", "alert-close", "search"
            size (str, optional): The size of the icon. Defaults to None.
                Choose one of the values from {sm|lg|xl} 
            **kwargs: Additional keyword arguments to customize the icon.
        """

        self.name = name
        self.size = size
        self.kwargs = kwargs

    def __ft__(self) -> FT:
        classes = [f"icon icon-{self.name}"]
        if self.size:
            classes.append(f"icon-{self.size}")
        if "cls" in self.kwargs:
            classes.append(self.kwargs.pop("cls"))
        return Span(cls=" ".join(classes), **self.kwargs)
