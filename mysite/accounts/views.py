from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from accounts.forms import CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
class AccountCreationForm(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "registration/register.html"
    success_url = "/accounts/login"


@login_required()
def profile(request):
    return render(request, "accounts/profile.html", context={"user": request.user})


@login_required()
def edit_profile(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password")
            if password:
                user.set_password(password)
                user.save()
                update_session_auth_hash(request, user)
            else:
                user.save()
            return redirect("accounts.profile")
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, "accounts/edit_profile.html", {"form": form})


@login_required()
def all_users(request):
    users = User.objects.all()
    return render(request, "accounts/users.html", context={"users": users})


@login_required()
def search_users(request):
    if request.method == "POST":
        username = request.POST.get("id")
        users = User.objects.filter(id=username)
        return render(request, "accounts/users.html", context={"users": users})
    return render(request, "accounts/users.html")
