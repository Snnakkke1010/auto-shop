from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse
from django.views.generic import UpdateView

from tasks.models import Product
from .forms import ProfileUpdateForm, UserUpdateForm
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
    user_profile = get_object_or_404(Profile, slug=slug)
    user_products = Product.objects.filter(creator=user_profile)

    page = request.GET.get('page', 1)
    paginator = Paginator(user_products, 3)

    try:
        user_products = paginator.page(page)
    except PageNotAnInteger:
        user_products = paginator.page(1)
    except EmptyPage:
        user_products = paginator.page(paginator.num_pages)

    return render(request, 'users/profile.html', {'user_profile': user_profile, 'user_products': user_products})


@login_required
def update_profile(request, slug):
    profile = request.user.profile
    user = request.user

    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        user_form = UserUpdateForm(request.POST, instance=user)

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('home')

    else:
        profile_form = ProfileUpdateForm(instance=profile)
        user_form = UserUpdateForm(instance=user)

    return render(request, 'users/update.html', {'profile_form': profile_form, 'user_form': user_form})