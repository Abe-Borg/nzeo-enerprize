# enerprize_api/urls.py

from django.urls import path, include
from django.contrib.auth.models import User
from . import views
 
urlpatterns = [
    path('get-schools-for-district/<int:district_id>/', views.get_schools_for_district, name='get_schools_for_district'),
    path('get-all-districts/', views.get_all_districts, name='get_all_districts'),
    path('get-service-agreements-for-school/<int:school_id>/<str:utility_type>', views.get_service_agreements_for_school, name='get_service_agreements_for_school'),
    path('get_meters_for_service_agreement/<int:service_agreement_id>/', views.get_meters_for_service_agreement, name='get_meters_for_service_agreement'),
    path('get-school-data/<int:school_id>/', views.get_school_data, name='get_school_data'),
    path('get-performance-metrics/<int:school_id>/<int:assigned_year>/<str:assigned_month>/', views.get_performance_metrics_year_and_month, name='get_performance_metrics_year_and_month'),
    path('get-performance-metrics-year/<int:school_id>/<int:assigned_year>/', views.get_performance_metrics_year, name='get_performance_metrics_year'),
]