"""
URL configuration for sobota_2_17 project.

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
from django.urls import path, include
from .views import NamiotListView, reserve, NamiotDetailView, unreserve, ReservedListView

urlpatterns = [
    path("", NamiotListView.as_view(), name="index"),
    path("reserve/<int:namiot_id>", reserve, name="reserve"),
    path("unreserve/<int:rezerwacja_id>", unreserve, name="unreserve"),
    path('<int:pk>', NamiotDetailView.as_view(), name="details"),
    path('reserved', ReservedListView.as_view(), name='reserved')
]
