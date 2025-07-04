"""
URL configuration for restaurant_ms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from restaurant import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.healthcheck, name='healthcheck'),
    path('restaurant/<uuid:restaurant_id>/', views.get_restaurants, name='get'),
    path('restaurant/', views.add_restaurant, name='add_restaurant'),
    path('restaurant/delete/<uuid:restaurant_id>/', views.delete_restaurant, name='delete_restaurant'),
    path('restaurant/all/', views.get_all_restaurants, name='get_all_restaurants'),
]
