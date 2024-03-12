from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import googlemaps
from district_management.models import SchoolDistrict
from school_management.models import School
gmaps = googlemaps.Client(key='AIzaSyANW4JtLihHDKEiBkkknOHOn6CCX-WwthA')
from plots.forms import UploadXMLForm


@login_required
def district_admin_home(request): 
    context = {}
    assigned_district = request.user.profile.user_district    
    district_info = SchoolDistrict.objects.get(district_name = assigned_district)
    context = {
        'district_geo_lat': district_info.district_geo_lat,
        'district_geo_long': district_info.district_geo_long,
        'southwest_lat': district_info.district_bb_southwest_lat,
        'southwest_lng': district_info.district_bb_southwest_lng,
        'northeast_lat': district_info.district_bb_northeast_lat,
        'northeast_lng': district_info.district_bb_northeast_lng,
        'district_name': district_info.district_name.upper(),
        'map_zoom_level': 12,
        'API_KEY': 'AIzaSyANW4JtLihHDKEiBkkknOHOn6CCX-WwthA'
    }
    
    district_schools_list = School.objects.filter(school_district=assigned_district)
    district_schools_information = [
        {
            'school_id': school.id,
            'name': school.school_name,
            'lat': float(school.latitude),
            'lng': float(school.longitude),
            'population': school.school_student_population,
            'percent_disadvantaged': school.school_student_percent_disadvantaged, 
            'percent_english_learners': school.school_student_percent_english_learners,
            'school_area': school.calculate_school_area_sqft(),
            'school_equipment_electricity_demand': school.calculate_electricity_usage(),
            'school_equipment_natural_gas_demand': school.calculate_natural_gas_usage(),
            'school_has_solar': school.school_has_solar,
        } for school in district_schools_list
    ]
    context['district_schools_information'] = district_schools_information
    return render(request, 'district_management/district_admin_home.html', context)

@login_required
def district_analytics(request):    
    # one district analytics page for all users, changes based on user role
    return render(request, 'district_management/district_analytics.html')

@login_required
def district_overview(request):
    return render(request, 'district_management/district_overview.html')

@login_required
def district_leaderboards(request):
    # one district leaderboard dashboard for each user, this one is specific to district users.
    return render(request, 'district_management/district_leaderboards.html') 