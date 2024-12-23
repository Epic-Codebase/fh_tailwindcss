import fasthtml.common as fh
from fastcore.meta import delegates
from ..tailwind import Tailwind
from ..utility import Width, FontSize, BorderRadius

@delegates(fh.ft_hx, keep=True)
class Input(Tailwind):
    

    def __ft__(self) -> fh.FT:
        """Generates the TailwindCSS input."""
        return fh.Input(
            *self.w,
            cls=f"{self.__css__()} bg-gray-50 border border-gray-300 text-gray-900 focus:ring-primary-600 focus:border-primary-600 block dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500", 
            **self.kwargs),
