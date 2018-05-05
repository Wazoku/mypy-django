import datetime
from typing import *

from django.db import models

class AnonymousUser(object):
    id = None # type: None
    pk = None # type: None
    username = '' # type: str
    is_staff = False # type: bool
    is_active = False # type: bool
    is_superuser = False # type: bool

    def __hash__(self) -> int:
        return 1

    def is_anonymous(self) -> bool:
        return True

    def is_authenticated(self) -> bool:
        return False

    def get_username(self) -> str:
        ...

class AbstractBaseUser(models.Model):
    Meta = ... # type: Any
    password = ... # type: str
    last_login = ... # type: datetime.datetime
    is_active = True # type: bool

    def get_username(self) -> str:
        ...

    def natural_key(self) -> tuple:
        ...

    def is_anonymous(self) -> bool:
        return False

    def is_authenticated(self) -> bool:
        return True

    def set_password(self, raw_password: str):
        ...

    def check_password(self, raw_password: str):
        ...

    def set_unusable_password(self):
        ...

    def has_usable_password(self) -> bool:
        ...

    def get_full_name(self) -> str:
        ...

    def get_short_name(self) -> str:
        ...

    def get_session_auth_hash(self) -> str:
        ...

class BaseUserManager(models.Manager):
    @classmethod
    def normalize_email(cls, email: str) -> str:
        pass

    def make_random_password(
        self,
        length: int = 10,
        allowed_chars: str = (
            'abcdefghjkmnpqrstuvwxyz'
            'ABCDEFGHJKLMNPQRSTUVWXYZ'
            '23456789'
        ),
    ) -> str:
        ...

    def get_by_natural_key(self, username: str) -> AbstractBaseUser:
        ...
