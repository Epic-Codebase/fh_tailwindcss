from fastcore.meta import delegates
from fasthtml.common import *
from .tailwind import Tailwind
from .icon import Icon

@delegates(ft_hx, keep=True)
class Modal(Tailwind):

    def __init__(self, *content, hidden=False, title=None, can_close=True, **kwargs):
        """A TailwindCSS modal component.
        Args:
            *content: Variable length argument list for the content of the modal.
            hidden (bool, optional): Whether the modal is hidden by default. Defaults to False.
            title (str, optional): The title of the modal. Defaults to None.
            can_close (bool, optional): Whether the modal can be closed. Defaults to True.
            **kwargs: Additional keyword arguments to customize the modal.
        """

        self.content = content
        self.hidden = hidden
        self.title = title
        self.can_close = can_close
        self.kwargs = kwargs

    def __ft__(self) -> FT:
        """Generates the TailwindCSS modal component."""

        def close_button():
            return Button(
                Icon("modal-close"),
                Span("Close modal", cls="sr-only"),
                type="button",
                cls="modal-close-button",
                hx_on_click=Modal.hide_script(self.kwargs.get("id")),
            )

        header_content = []
        if self.title:
            header_content.append(H3(self.title, cls="modal-title"))
        if self.can_close:
            header_content.append(close_button())
        
        modal = Div(
            Div(
                Div(
                    Div(*header_content, cls="modal-header") if header_content else None,
                    *self.content,
                    cls="modal-content"
                ),
                cls="modal-center"
            ),
            tabindex="-1",
            aria_hidden="true",
            cls=f"{'hidden ' if self.hidden else ''}modal {self.kwargs.pop('cls', '')}".strip(),
            **self.kwargs
        )
        
        return modal
