from django.contrib import admin
from django.urls import path, include
from form_signup import views

urlpatterns = [
    path("signupdetails/<int:pk>", views.SignUp.as_view()),
    path("signupdetails", views.SignUp.as_view()) 
]
