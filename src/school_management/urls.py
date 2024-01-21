from django.urls import path
from . import views

urlpatterns = [
    path('school-home', views.school_home, name = 'school_home'),
    path('site-staff-home', views.site_staff_home, name = 'stite_staff_home'),
]