from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView,
)
from django.views import generic
from django.urls import reverse_lazy

from project.authentication import forms as auth_forms


class LoginView(BaseLoginView):
    template_name = "accounts/login.html"


class SignUpView(generic.CreateView):
    form_class = auth_forms.UserCreationForm
    success_url = reverse_lazy("auth:login")
    template_name = "accounts/signup.html"

class LogoutView(BaseLogoutView):
    pass
