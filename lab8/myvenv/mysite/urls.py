"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from shopback.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', get_products),
    path('api/products/<int:id>/', get_one_product),
    path('api/categories/', get_categories),
    path('api/categories/<int:id>/', get_one_category),
    path('api/categories/<int:id>/products/', list_of_products_by_category),
]
