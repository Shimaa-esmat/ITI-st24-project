
from django.urls import include, path
from accounts.views import  AccountCreatioForm

urlpatterns=[
    path("", include("django.contrib.auth.urls")),
    path("register", AccountCreatioForm.as_view(), name='accounts.register')
]