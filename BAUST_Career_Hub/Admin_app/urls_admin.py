from django.contrib import admin
from django.urls import path
from Admin_app import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('footer/', views.footer, name = "footer"),
    path('signin/', views.signin, name = "signin"),
    path('signup/', views.signup, name = "signup"),

]