# enerprize_api/views.py
from django.shortcuts import render
from school_management.models import School
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def get_schools_for_district(request, district_id):
    schools = School.objects.filter(district_id=district_id).values('id', 'name')
    school_list = list(schools)
    return JsonResponse({'schools': school_list})






