# district_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.district_admin_home, name = 'district_admin_home'),
    path('overview/', views.district_overview, name = 'district_overview'),
    path('analytics/school_level', views.school_level_analytics, name = 'school_level_analytics'),
    path('analytics/district_level', views.district_level_analytics, name = 'district_level_analytics'),
    path('district-leaderboards/', views.district_leaderboards, name = 'district_leaderboards'),
]