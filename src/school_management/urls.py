from django.urls import path
from . import views

urlpatterns = [
    path('school_home', views.school_home, name = 'school_home'),
    path('equipment-home', views.equipment_home, name = 'equipment_home'),
    path('add_utility_bill', views.add_utility_bill, name = 'add_utility_bill'),
    path('check_calculations', views.check_calculations, name = 'check_calculations'),
]