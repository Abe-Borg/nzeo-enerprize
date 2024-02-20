# enerprize_api/views.py
from django.shortcuts import render
from school_management.models import School, Meter
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


def get_service_agreements_for_school(request, school_id):
    # Use get_object_or_404 to handle cases where the school does not exist
    school = get_object_or_404(School, pk=school_id)
    # Retrieve service agreement IDs for the given school
    service_agreements = school.serviceagreement_set.all().values_list('service_agreement_id', flat=True)
    service_agreement_list = list(service_agreements)
    if service_agreement_list:
        return JsonResponse({'service_agreements': service_agreement_list})
    else:
        # No service agreements found for the given school ID
        return JsonResponse({'error': 'No service agreements found for the given school ID'}, status=404)


def get_meters_for_service_agreement(request, service_agreement_id):
    if service_agreement_id:
        meters = Meter.objects.filter(meter_service_agreement_id=service_agreement_id).values_list('meter_id', flat=True)
        meter_list = list(meters)
        # Check if the service agreement has meters associated with it
        if meter_list:
            return JsonResponse({'meters': meter_list})
        else:
            # No meters found for the given service agreement ID
            return JsonResponse({'error': 'No meters found for the given service agreement ID'}, status=404)
    else:
        # Service agreement ID not provided or is None
        return JsonResponse({'error': 'Service agreement ID is required'}, status=400)

def get_school_gross_floor_area(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    gross_floor_area = school.calculate_school_area_sqft()
    return JsonResponse({'gross_floor_area': gross_floor_area})
