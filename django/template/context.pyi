from typing import *

VT = TypeVar('VT')

class ContextDict(dict):
    def __init__(self, context: 'Context', *args, **kwargs) -> None:
        ...

    def __enter__(self):
        ...

    def __exit__(self, *args, **kwargs):
        ...

class BaseContext(Generic[VT], Mapping[str, VT]):
    def __init__(self, dict_ : Union[dict, ContextDict] = None) -> None:
        ...

    def push(self, *args, **kwargs) -> ContextDict:
        ...

    def pop(self) -> dict:
        ...

    def new(self, values: Optional[List[str]] = None) -> 'BaseContext':
        ...

    def flatten(self) -> dict:
        ...

class Context(BaseContext):
    def new(self, values: Optional[List[str]] = None) -> 'Context':
        ...
