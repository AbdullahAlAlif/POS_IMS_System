from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
from .forms import CustomUserCreationForm


@guest
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('inventory:product_list')
    else:
        initial_data = {'username': '', 'email': '', 'password1': '', 'password2': ''}
        form = CustomUserCreationForm(initial=initial_data)
    return render(request, 'authentication/auth/register.html',{'form':form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('inventory:product_list')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'authentication/auth/login.html',{'form':form})

@auth
def dashboard_view(request):
    return render(request, 'inventory:product_list')

def logout_view(request):
    logout(request)
    return redirect('login')
