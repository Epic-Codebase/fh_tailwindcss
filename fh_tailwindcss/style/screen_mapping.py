
from typing import Union

from . import ScreenSize, Margins, Paddings, Gaps

class ScreenMapping(dict[ScreenSize, tuple[Union[Margins, Paddings, Gaps, any]]]):
    
    def __css__(self):

        css = []
        for screen_size, items in self.items():
            if isinstance(items, (tuple, list)):
                for item in items:
                    prefix = f"{screen_size.__css__()}{':' if screen_size != ScreenSize.DEFAULT else ''}"
                    if hasattr(item, '__css__'):
                        item = ' '.join([prefix + item for item in item.__css__().split(' ')])
                    else:
                        item = prefix + str(item) 
                    
                    css.append(item)

        return ' '.join(css)