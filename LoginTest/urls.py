from django.contrib import admin
from django.urls import path, include
from LoginTest import views

urlpatterns = [
    path('UserRegistration/', views.UserRegistrationView.as_view()),
    path('UserLogin/',views.UserLoginView.as_view()),

    path('regist/',views.regist.as_view()),
    path('login/',views.login.as_view())
]
