# enerprize_api/views.py
from django.shortcuts import render
from school_management.models import School
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from district_management.models import SchoolDistrict


def get_schools_for_district(request, district_id):
    schools = School.objects.filter(school_district_id=district_id).values('id', 'school_name')
    school_list = list(schools)
    return JsonResponse({'schools': school_list})

def get_all_districts(request):
    districts = SchoolDistrict.objects.all().values('id', 'district_name')
    district_list = list(districts)
    return JsonResponse({'districts': district_list})

def get_meters_for_school_and_utility_type(request, school_id, utility_type_id):
    school = get_object_or_404(School, pk=school_id)
    meters = school.meter_set.filter(meter_type=utility_type_id).values('meter_id')
    meter_list = list(meters)
    return JsonResponse({'meters': meter_list})


def get_school_gross_floor_area(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    gross_floor_area = school.calculate_school_area_sqft()
    return JsonResponse({'gross_floor_area': gross_floor_area})
