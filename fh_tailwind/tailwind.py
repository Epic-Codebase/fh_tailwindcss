from abc import ABC, abstractmethod
from fastcore.meta import delegates
from fasthtml.common import ft_hx, FT

@delegates(ft_hx, keep=True)
class Tailwind(ABC):

    def __init__(self, *w, **kwargs):
        self.w = w
        self.kwargs = kwargs

    @abstractmethod
    def __ft__(self) -> FT:
        """Generates the TailwindCSS component. Should not be called by users directly."""
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
