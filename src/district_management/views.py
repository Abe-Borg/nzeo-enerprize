from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# @login_required
def district_admin_home(request):
    # map_zoom_level = 16
    context = {}
    # # fetch assigned district
    # assigned_district = request.user.profile.assigned_district

    # # retrieve district data
    # district_info = SchoolDistrict.objects.get(district_id = assigned_district)

    # context = {
    #     'district_geo_lat': district_info.district_geo_lat,
    #     'district_geo_long': district_info.district_geo_long,
    #     'map_zoom_level': map_zoom_level
    #     'map_bounding_box': ???
    # }

    context = {
        'district_geo_lat': 37.00203947386811,
        'district_geo_long': -119.0093994140625,
        'map_zoom_level': 16
    }


    return render(request, 'district_admin_home.html', context)