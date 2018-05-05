# Stubs for django.db.models (Python 3.5)
#
# This module was modifed by w0rp.

from django.db.models.manager import Manager
from django.db.models.base import Model
from django.db.models.query import Q, QuerySet, Prefetch
from django.db.models.expressions import (
    Expression,
    ExpressionWrapper,
    F,
    Value,
    Func,
    Case,
    When,
)
from django.db.models.aggregates import *
from django.db.models.fields import *
from django.db.models.fields.related import (
    ForeignKey,
    ForeignObject,
    OneToOneField,
    ManyToManyField,
    ManyToOneRel,
    ManyToManyRel,
    OneToOneRel,
)
from django.db.models.lookups import Lookup, Transform
from django.db.models.deletion import (
    CASCADE,
    PROTECT,
    SET,
    SET_NULL,
    SET_DEFAULT,
    DO_NOTHING,
    ProtectedError,
)

def permalink(func): ...
