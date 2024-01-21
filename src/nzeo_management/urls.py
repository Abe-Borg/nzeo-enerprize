from django.urls import path
from . import views

urlpatterns = [
    path('', views.nzeo_admin_home, name = 'nzeo_admin_home'),
]