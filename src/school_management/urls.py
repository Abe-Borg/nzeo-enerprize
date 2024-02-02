from django.urls import path
from . import views

urlpatterns = [
    path('school_home', views.school_home, name = 'school_home'),
    path('school_staff_home', views.school_staff_home, name = 'school_staff_home'),
]