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
    district_schools_coordinates = [
        {
            'name': school.school_name,
            'lat': float(school.latitude),  # Convert Decimal to float
            'lng': float(school.longitude),  # Convert Decimal to float
        } for school in district_schools_list
    ]

    context['district_schools_coordinates'] = district_schools_coordinates
    # print(context)
    return render(request, 'district_management/district_admin_home.html', context)

@login_required
def district_analytics(request):    
    return render(request, 'district_management/district_analytics.html')

@login_required
def district_overview(request):
    return render(request, 'district_management/district_overview.html')

@login_required
def district_leaderboards(request):
    return render(request, 'district_management/district_leaderboards.html')