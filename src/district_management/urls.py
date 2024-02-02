# district_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.district_admin_home, name = 'district_admin_home')
]