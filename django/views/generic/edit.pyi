# Stubs for django.views.generic.edit (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.forms import models as model_forms
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.detail import BaseDetailView, SingleObjectMixin, SingleObjectTemplateResponseMixin

PERCENT_PLACEHOLDER_REGEX = ... # type: Any

class FormMixinBase(type):
    def __new__(cls, name, bases, attrs): ...

class FormMixin:
    initial = ... # type: Any
    form_class = ... # type: Any
    success_url = ... # type: Any
    prefix = ... # type: Any
    def get_initial(self): ...
    def get_prefix(self): ...
    def get_form_class(self): ...
    def get_form(self, form_class=None): ...
    def get_form_kwargs(self): ...
    def get_success_url(self): ...
    def form_valid(self, form): ...
    def form_invalid(self, form): ...
    def get_context_data(self, **kwargs): ...

class ModelFormMixin(FormMixin, SingleObjectMixin):
    fields = ... # type: Any
    def get_form_class(self): ...
    def get_form_kwargs(self): ...
    success_url = ... # type: Any
    def get_success_url(self): ...
    object = ... # type: Any
    def form_valid(self, form): ...

class ProcessFormView(View):
    def get(self, request, *args, **kwargs): ...
    def post(self, request, *args, **kwargs): ...
    def put(self, *args, **kwargs): ...

class BaseFormView(FormMixin, ProcessFormView): ...
class FormView(TemplateResponseMixin, BaseFormView): ...

class BaseCreateView(ModelFormMixin, ProcessFormView):
    object = ... # type: Any
    def get(self, request, *args, **kwargs): ...
    def post(self, request, *args, **kwargs): ...

class CreateView(SingleObjectTemplateResponseMixin, BaseCreateView):
    template_name_suffix = ... # type: Any

class BaseUpdateView(ModelFormMixin, ProcessFormView):
    object = ... # type: Any
    def get(self, request, *args, **kwargs): ...
    def post(self, request, *args, **kwargs): ...

class UpdateView(SingleObjectTemplateResponseMixin, BaseUpdateView):
    template_name_suffix = ... # type: Any

class DeletionMixin:
    success_url = ... # type: Any
    object = ... # type: Any
    def delete(self, request, *args, **kwargs): ...
    def post(self, request, *args, **kwargs): ...
    def get_success_url(self): ...

class BaseDeleteView(DeletionMixin, BaseDetailView): ...

class DeleteView(SingleObjectTemplateResponseMixin, BaseDeleteView):
    template_name_suffix = ... # type: Any
