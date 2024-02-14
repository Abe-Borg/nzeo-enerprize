# enerprize_api/urls.py

from django.urls import path, include
from django.contrib.auth.models import User
from . import views

urlpatterns = [
    path('get-schools-for-district/<int:district_id>/', views.get_schools_for_district, name='get_schools_for_district'),
    path('get-all-districts/', views.get_all_districts, name='get_all_districts'),
    path('get-meters-for-school-and-utility-type/<int:school_id>/<int:utility_type_id>/', views.get_meters_for_school_and_utility_type, name='get_meters_for_school_and_utility_type'),
]