from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from django.contrib import messages

from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the error below.')
    else:
        form = UserCreationForm()
    return render(request, 'usermodule/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('food_list')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'usermodule/login.html', {'form': form})

from django.contrib.auth import logout

def logout(request):
    messages.info(request, 'You have been logged out.')
    return redirect('login')