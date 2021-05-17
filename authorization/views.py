from django.views import generic

from django.contrib.auth import (
    views,
    forms,
    logout
)


class LoginView(views.LoginView):
    form_class = forms.AuthenticationForm
    template_name = 'authentication/login.html'


class RegistrationView(views.FormView):
    form_class = forms.UserCreationForm
    template_name = 'authentication/registration.html'
