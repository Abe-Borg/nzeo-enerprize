from django.urls import path
from . import views

urlpatterns = [
    path('school_home/<int:school_id>', views.school_home, name = 'school_home'),
    path('school-analytics/<int:school_id>/', views.school_analytics, name = 'school_analytics'),
    path('equipment-home/<int:equipment_id>/', views.equipment_home, name = 'equipment_home'),
    path('add_utility_bill', views.add_utility_bill, name = 'add_utility_bill'),
    path('check_calculations', views.check_calculations, name = 'check_calculations'),
    path('building-home/<int:building_id>/', views.building_home, name = 'building_home'),
]