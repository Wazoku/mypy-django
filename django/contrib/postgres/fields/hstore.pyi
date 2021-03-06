# Stubs for django.contrib.postgres.fields.hstore (Python 3.5)
#
# This file was generated by stubgen and edited by w0rp.

from typing import Any

from django.db.models import Field


class HStoreField(Field):
    empty_strings_allowed = ...  # type: bool
    description = ...  # type: Any
    default_error_messages = ...  # type: Any

    def db_type(self, connection): ...

    def get_transform(self, name): ...

    def validate(self, value, model_instance): ...

    def to_python(self, value): ...

    def value_to_string(self, obj): ...

    def formfield(self, **kwargs): ...
