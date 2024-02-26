# enerprize_api/urls.py

from django.urls import path, include
from django.contrib.auth.models import User
from . import views
 
urlpatterns = [
    path('get-schools-for-district/<int:district_id>/', views.get_schools_for_district, name='get_schools_for_district'),
    path('get-all-districts/', views.get_all_districts, name='get_all_districts'),
    path('get-service-agreements-for-school/<int:school_id>/<str:utility_type>', views.get_service_agreements_for_school, name='get_service_agreements_for_school'),
    path('get_meters_for_service_agreement/<int:service_agreement_id>/', views.get_meters_for_service_agreement, name='get_meters_for_service_agreement'),
    path('get-school-gross-floor-area/<int:school_id>/', views.get_school_gross_floor_area, name='get_school_gross_floor_area'),
    path('get-school-electricity-usage/<int:school_id>/', views.get_school_electricity_usage, name='get_school_electricity_usage'),
    path('get-school-natural-gas-usage/<int:school_id>/', views.get_school_natural_gas_usage, name='get_school_natural_gas_usage'),
]