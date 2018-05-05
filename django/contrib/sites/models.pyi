from typing import Any

from django.db import models

class SiteManager(models.Manager):
    ...

class Site(models.Model):
    Meta = ... # type: Any
    objects = ... # type: SiteManager
    domain = ... # type: str
    name = ... # type: str
