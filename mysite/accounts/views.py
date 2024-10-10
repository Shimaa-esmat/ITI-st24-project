from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.forms import  RegistrationForm
from django.views.generic.edit import CreateView

# Create your views here.
class AccountCreatioForm(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "registration/register.html"
    success_url = "/accounts/login"
