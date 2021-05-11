from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('signin/', views.signin, name = "signin"),
    path('signup/', views.signup, name = "signup"),
    path('student_signup/', views.student_signup, name = "student_signup"),
    path('student_signup_save/', views.student_signup_save, name = "student_signup_save"),
    path('teacher_signup/', views.teacher_signup, name = "teacher_signup"),
]