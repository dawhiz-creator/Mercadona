"""
URL configuration for mercadona project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from django.contrib import admin


import environ
from dotenv import load_dotenv
from pathlib import Path
import environ
from django.core.management.utils import get_random_secret_key
import os

urlpatterns = [
    path('', include('mercadona_promos.urls')),
    path('admin/', admin.site.urls),
    # path(env('SECRET_ADMIN_URL') + '/admin/', admin.site.urls),
]

