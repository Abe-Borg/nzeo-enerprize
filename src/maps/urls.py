from django.urls import path
from . import views

urlpatterns = [
    path('overall-map', views.overall_map, name = 'overall_map'),
    path('district-map', views.district_map, name = 'district_map'),
    path('school-map', views.school_map, name = 'school_map'),
    path('building-map', views.building_map, name = 'building_map'),
]