from ...tailwind import TailwindEnum

# https://tailwindcss.com/docs/appearance

class Appearance(TailwindEnum):
    """
    Utilities for suppressing or restoring native form control styling.

    Attributes:
        NONE (str): Removes the default browser styling from form controls, allowing full customization. 
        AUTO (str): Restores the browser's default styling for form controls.
    """
    NONE = "appearance-none"
    AUTO = "appearance-auto"
