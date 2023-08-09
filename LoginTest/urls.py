from django.contrib import admin
from django.urls import path, include
from LoginTest import views

urlpatterns = [
    path('Registration/', views.UserRegistrationView.as_view()),
    path('Login/',views.UserLoginView.as_view()),
]
