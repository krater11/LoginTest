from django.contrib import admin
from django.urls import path, include
from LoginTest import views

urlpatterns = [
    path('regist/', views.regist.as_view()),
    path('login/', views.login.as_view()),

    path('image/', views.ImagePostView.as_view()),
    path('imagelist/', views.ImageListView.as_view())
]
