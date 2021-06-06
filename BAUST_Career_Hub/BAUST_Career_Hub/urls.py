
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib.auth import views

urlpatterns = [
    #path('accounts/', include('Admin_app.urls')),
    path('admin/', admin.site.urls),
    path('', include('Admin_app.urls')),
    
]
