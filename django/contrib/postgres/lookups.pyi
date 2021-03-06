# Stubs for django.contrib.postgres.lookups (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.db.models import Lookup, Transform
from .search import SearchVector as SearchVector, SearchVectorExact as SearchVectorExact, SearchVectorField as SearchVectorField

class PostgresSimpleLookup(Lookup):
    def as_sql(self, qn, connection): ...

class DataContains(PostgresSimpleLookup):
    lookup_name = ...  # type: str
    operator = ...  # type: str

class ContainedBy(PostgresSimpleLookup):
    lookup_name = ...  # type: str
    operator = ...  # type: str

class Overlap(PostgresSimpleLookup):
    lookup_name = ...  # type: str
    operator = ...  # type: str

class HasKey(PostgresSimpleLookup):
    lookup_name = ...  # type: str
    operator = ...  # type: str
    prepare_rhs = ...  # type: bool

class HasKeys(PostgresSimpleLookup):
    lookup_name = ...  # type: str
    operator = ...  # type: str
    def get_prep_lookup(self): ...

class HasAnyKeys(HasKeys):
    lookup_name = ...  # type: str
    operator = ...  # type: str

class Unaccent(Transform):
    bilateral = ...  # type: bool
    lookup_name = ...  # type: str
    function = ...  # type: str

class SearchLookup(SearchVectorExact):
    lookup_name = ...  # type: str
    lhs = ...  # type: Any
    def process_lhs(self, qn, connection): ...

class TrigramSimilar(PostgresSimpleLookup):
    lookup_name = ...  # type: str
    operator = ...  # type: str
