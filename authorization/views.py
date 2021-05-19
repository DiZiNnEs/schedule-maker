from django.contrib.auth import (
    forms,
    authenticate,
    login,
)
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView

from authorization.forms import LoginForm


class LoginView(View):
    form_class = LoginForm
    template_name = 'authentication/login.html'

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Invalid data')


class RegistrationView(CreateView):
    form_class = forms.UserCreationForm
    template_name = 'authentication/registration.html'

    def get_success_url(self):
        return reverse('login')
