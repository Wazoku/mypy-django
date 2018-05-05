from typing import *

from django.db import models

class ContentTypeManager(models.Manager):
    def get_for_model(self, model, for_concrete_model=True) -> 'ContentType':
        ...

    def clear_cache(self):
        ...

class ContentType(models.Model):
    Meta = ... # type: Any
    objects = ... # type: ContentTypeManager
    app_label = ... # type: str
    name = ... # type: str
