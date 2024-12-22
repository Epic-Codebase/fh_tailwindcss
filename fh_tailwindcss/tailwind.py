from abc import ABC, abstractmethod
from enum import Enum
from fastcore.meta import delegates
from fasthtml.common import ft_hx, FT


class TailwindCSS:
    """
    Base Tailwin CSS class. Any Tailwind component that produces a CSS string derives from this class.
    """

    @abstractmethod
    def __css__(self) -> str:
        pass


@delegates(ft_hx, keep=True)
class Tailwind(ABC):
    """Base Tailwind CSS component class. Any Tailwind component that produces a FT derives from this class."""

    def __init__(self, *w, **kwargs):
        self.css_components, self.w = self.__extract_css_types_from_list__(w)
        self.kwargs = kwargs


    def __extract_css_types_from_list__(self, any_list):
        """Separates CSS components and NON-CSS components from any list."""

        css_components = []
        non_css_components = []
        for item in any_list[:]:
            # The Tailwind class implements the "__css__" method, but it does not produce CSS, only build CSS from CSS producers.
            if hasattr(item, '__css__') and not hasattr(item, '__ft__'):
                css_components.append(item)
            else:                
                non_css_components.append(item)
            
        return css_components, non_css_components


    def get_css_from_list(self, list) -> str:
        result = []
        for item in list:
            if hasattr(item, '__css__'):
                result.append(item.__css__())
        return ' '.join(result)


    def __css__(self):
        return self.get_css_from_list(self.css_components)
    

    @abstractmethod
    def __ft__(self) -> FT:
        """Generates the Tailwind CSS component."""

        pass
    
    
    @staticmethod
    def generate_hx_vals(vals: list, defaults: dict = None):
        """Generate the HTMX vals based on a list of HTML component IDs.
        
        Args:
            vals (list): A list of HTML component IDs.
            defaults (dict, optional): A dictionary of default values for the HTMX vals. 
                Defaults to None.
        """

        assert vals, "The `vals` list must not be empty."

        # Prepare the default JS code for the keys in the defaults dictionary
        defaults_js = ", ".join(
            f'"{key}": "{value}"'
            for key, value in (defaults or {}).items()
        )

        # Prepare the dynamic JS code for `vals`
        dynamic_js = ", ".join(
            f'"{val}": (document.getElementById("{val}") ? document.getElementById("{val}").value : null)'
            for val in vals
        )

        # Combine the defaults and dynamic values into one JS object
        combined_js = ", ".join(filter(None, [defaults_js, dynamic_js]))

        # Return the full JavaScript expression wrapped in curly braces
        return f"js:{{ {combined_js} }}"
    

class TailwindEnum(TailwindCSS, Enum):
    """Base Tailwind CSS enum class. Any enum that produces a CSS derives from this class."""

    def __css__(self) -> str:
        return self.value if self else ""


class TailwindDict(TailwindCSS, dict):
    """Base Tailwind CSS dict class. Any dict that produces a CSS derives from this class."""

    def __css__(self):
        return ' '.join([f"{key.__css__() if hasattr(key, '__css__') else str(key)}-{str(val)}" for key, val in self.items() if val is not None])
    

class TailwindStack(TailwindDict):
    """Base Tailwind CSS [modifiers] stack."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.separator = ':'


    def __css__(self):
        css = []
        for key, value in self.items():
            if isinstance(value, (tuple, list)):
                for item in value:
                    key_css = key.__css__()
                    prefix = key_css + self.separator if key_css else ''

                    if hasattr(item, '__css__'):
                        item = ' '.join([prefix + item for item in str(item.__css__()).split(' ')])
                    else:
                        item = prefix + str(item)

                    css.append(item)

        return ' '.join(css)