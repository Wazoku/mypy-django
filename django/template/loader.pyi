from typing import *

from .base import TemplateDoesNotExist, Template

def get_template(
    template_name: str,
    dirs: List[str] = None,
    using: Optional[str] = None,
) -> Template:
    ...

def select_template(template_name_list, using: Optional[Any] = ...): ...

def render_to_string(
    template_name,
    context: Optional[Any] = ...,
    request: Optional[Any] = ...,
    using: Optional[Any] = ...
): ...
