from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import CreateForm
from .mixins import OnlyUserMixin
from .models import User


class CreateAccountView(CreateView):
    form_class = CreateForm
    success_url = reverse_lazy("index")
    template_name = "registration/create.html"


class UserDeleteView(OnlyUserMixin, DeleteView):
    template_name = "registration/delete.html"
    success_url = reverse_lazy("index")
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
