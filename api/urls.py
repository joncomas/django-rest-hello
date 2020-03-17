from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('users/<int:user_id>', views.UsersView.as_view(), name='id-users'),
    path('users/', views.UsersView.as_view(), name='all-users')
]