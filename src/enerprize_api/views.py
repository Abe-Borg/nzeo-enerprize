# enerprize_api/views.py
from django.shortcuts import render
from school_management.models import School, Meter, ServiceAgreement, PerformanceMetrics, Equipment, Building
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from district_management.models import SchoolDistrict
from django.views.decorators.csrf import csrf_exempt
import json


def get_schools_for_district(request, district_id):
    schools = School.objects.filter(school_district_id=district_id).values('id', 'school_name')
    school_list = list(schools)
    return JsonResponse({'schools': school_list})

def get_all_districts(request):
    districts = SchoolDistrict.objects.all().values('id', 'district_name')
    district_list = list(districts)
    return JsonResponse({'districts': district_list})

def get_service_agreements_for_school(request, school_id, utility_type):
    # Use get_object_or_404 to handle cases where the school does not exist
    school = get_object_or_404(School, pk=school_id)
    # Retrieve service agreement IDs for the given school and utility type
    service_agreements = ServiceAgreement.objects.filter(
        school=school, 
        utility_type=utility_type
    ).values_list('service_agreement_id', flat=True)
    
    service_agreement_list = list(service_agreements)
    if service_agreement_list:
        return JsonResponse({'service_agreements': service_agreement_list})
    else:
        # No service agreements found for the given school ID and utility type
        return JsonResponse({'error': 'No service agreements found for the given school ID and utility type'}, status=404)

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

def get_school_data(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    data = {
        'school_area_sqft': school.calculate_school_area_sqft(),
        'number_of_students': school.school_student_population,
        'campus_energy_demand_kW': school.calculate_electricity_usage(),
        'campus_gas_demand_kbtuh': school.calculate_natural_gas_usage(),
        'school_district': school.school_district.district_name,
        'school_name': school.school_name,
        'school_address': school.school_address,

    }
    return JsonResponse(data)

def get_performance_metrics_year_and_month(request, school_id, assigned_year, assigned_month):
    metrics = PerformanceMetrics.objects.filter(
        school = school_id,
        assigned_year=assigned_year,
        assigned_month=assigned_month
    ).values()     
    return JsonResponse(list(metrics), safe=False)

def get_performance_metrics_year(request, school_id, assigned_year):
    metrics = PerformanceMetrics.objects.filter(
        school_id=school_id,
        assigned_year=assigned_year
    ).values()
    return JsonResponse(list(metrics), safe=False)

@csrf_exempt
def update_coordinates(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            equipment_data = data.get('equipment', [])
            building_data = data.get('buildings', [])
            
            for item in equipment_data:
                Equipment.objects.filter(id=item['id']).update(equipment_coordinates=item['coordinates'])  
            for item in building_data:
                Building.objects.filter(id=item['id']).update(building_coordinates=item['coordinates']) 
            return JsonResponse({'status': 'success', 'message': 'Coordinates updated successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
def get_equipment_for_school(request, school_id):
    equipment_list = list(Equipment.objects.filter(equipment_school_id=school_id)
                          .values('id', 'equipment_tag', 'equipment_type', 'equipment_install_date', 
                                  'equipment_gas_btuh_demand', 'equipment_elec_kw_demand')[:50]
                        )
    return JsonResponse({'equipment': equipment_list})

def get_buildings_for_school(request, school_id):
    building_list = list(Building.objects.filter(building_school_id=school_id)
                          .values('id', 'building_name', 'building_area_sqft', 'building_type', 'building_age')[:50]
                        )
    return JsonResponse({'buildings': building_list})

