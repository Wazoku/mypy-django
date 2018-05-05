from typing import *

from .context import Context

class TemplateDoesNotExist(Exception):
    pass

class Template:
    def __init__(
        self,
        template_string: str,
        origin: Optional[str] = None,
        name: Optional[str] = None,
        engine: Optional[Any] = None,
    ) -> None:
        ...

    def render(self, context: Union[Context, dict]):
        ...

class Node(object):
    must_be_first = False # type: bool
    child_nodelists = ('nodelist',) # type: Tuple[str]

    def render(self, context: Union[Context, dict]) -> str:
        ...

    def __iter__(self):
        ...
