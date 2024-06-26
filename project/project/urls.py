"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('login user/',login, name = "login"),
    path('rooms/', room),
    path('register/', register),
    path('logout/', Logout),
    path('about us/', aboutUs),
    path('contact us/', contactUs),
    path('reservation/<str:room_number>/', reservation, name = "reservation"),
    path('reviews/', review, name='review'),
    path('book food/', food),
    path('order food api/<int:room>', bookFood)
]

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)