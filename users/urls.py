from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

    path('profile/<slug:slug>/', profile_view, name='profile'),
    path('profile/update/<slug:slug>', update_profile, name='update'),
]