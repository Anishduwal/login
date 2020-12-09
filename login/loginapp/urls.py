from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.signin, name="login"),
    path('home', views.home, name='home'),
    path('register', views.register, name="register"),
    path('signout', views.signout, name="logout"),
]
