# district_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.district_admin_home, name = 'district_admin_home'),
    path('overview/', views.district_overview, name = 'district_overview'),
    path('district_analytics', views.district_analytics, name = 'district_analytics'),
    path('district-leaderboards/', views.district_leaderboards, name = 'district_leaderboards'),
]