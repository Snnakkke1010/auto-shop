# ваші_вигляди/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from .forms import ProfileUpdateForm
from .models import Profile


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Увійти в систему після реєстрації
            Profile.objects.create(user=user)  # Створення профілю
            return redirect('home')  # Змініть 'home' на вашу домашню сторінку
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Змініть 'home' на вашу домашню сторінку
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile_view(request, slug):
    context = get_object_or_404(Profile, user__username=slug)
    return render(request, 'users/profile.html', {'context': context})

@login_required
def update_profile(request, slug):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileUpdateForm()
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'users/update.html', {'form': form})

