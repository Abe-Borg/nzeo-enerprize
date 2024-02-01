# enerprize_api/urls.py

from django.urls import path, include
from django.contrib.auth.models import User
from . import views

urlpatterns = [
    path('get-schools-for-district/<int:district_id>/', views.get_schools_for_district, name='get_schools_for_district'),
]