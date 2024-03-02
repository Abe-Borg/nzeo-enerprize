from django.urls import path
from . import views

urlpatterns = [
    path('', views.nzeo_admin_home, name = 'nzeo_admin_home'),
    path('all-districts-leaderboards/', views.all_districts_leaderboards, name = 'all_districts_leaderboards'),
]