from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from accounts.forms import  RegistrationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import  login_required
from django.shortcuts import get_object_or_404
from accounts.forms import UserForm
from django.db.models import Q  

# Create your views here.
class AccountCreatioForm(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "registration/register.html"
    success_url = "/accounts/login"

@login_required()
def profile(request):
    # user = User.objects.get(id = request.id)
    return render(request, 'accounts/profile.html',context={"user": request.user})


def edit_profile(request):
    user = get_object_or_404(User,id = request.user.id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts.profile')
    else:
        form = UserForm(instance=user)

    return render(request, 'accounts/edit_profile.html', {'form': form})    


def all_users(request):
    users = User.objects.all()
    return render(request, 'accounts/users.html',context={'users':users})

def search_users(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        users = User.objects.filter(username__contains = username)
        return render(request, 'accounts/users.html',context={'users':users})
