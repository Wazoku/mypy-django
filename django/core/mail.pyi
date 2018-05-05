from typing import *

class EmailMessage:
    def __init__(
        self,
        subject: str = '',
        body: str = '',
        from_email: Optional[str] = None,
        to: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None,
        connection: Optional[Any] = None,
        attachments: Optional[Any] = None,
        headers: Optional[Any] = None,
        alternatives: Optional[Any] = None,
        cc: Optional[List[str]] = None,
        reply_to: Optional[str] = None
    ) -> None:
        ...

    def message(self) -> str:
        ...

    def recipients(self) -> List[str]:
        ...

    def send(self, fail_silently: bool = False):
        ...

    def attach(
        self,
        filename: Optional[str] = None,
        content: Optional[bytes] = None,
        mimetype: Optional[str] = None
    ):
        ...

    def attach_file(self, path: str, mimetype: Optional[str] = None):
        ...

class EmailMultiAlternatives(EmailMessage):
    def attach_alternative(self, content: bytes, mimetype: str):
        ...
