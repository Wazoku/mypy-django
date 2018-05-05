# Stubs for django.db.models (Python 3.5)
#
# This module was modifed by w0rp.

from django.db.models.manager import Manager as Manager
from django.db.models.base import Model as Model
from django.db.models.query import Q as Q, QuerySet as QuerySet, Prefetch as Prefetch
from django.db.models.expressions import (
    Expression as Expression,
    ExpressionWrapper as ExpressionWrapper,
    F as F,
    Value as Value,
    Func as Func,
    Case as Case,
    When as When,
)
from django.db.models.aggregates import *
from django.db.models.fields import *
from django.db.models.fields.related import (
    ForeignKey as ForeignKey,
    ForeignObject as ForeignObject,
    OneToOneField as OneToOneField,
    ManyToManyField as ManyToManyField,
    ManyToOneRel as ManyToOneRel,
    ManyToManyRel as ManyToManyRel,
    OneToOneRel as OneToOneRel,
)
from django.db.models.lookups import Lookup as Lookup, Transform as Transform
from django.db.models.deletion import (
    CASCADE as CASCADE,
    PROTECT as PROTECT,
    SET as SET,
    SET_NULL as SET_NULL,
    SET_DEFAULT as SET_DEFAULT,
    DO_NOTHING as DO_NOTHING,
    ProtectedError as ProtectedError,
)

def permalink(func): ...
