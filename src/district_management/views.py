from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin

# @login_required
def district_admin_home(request):
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
        'district_geo_lat': 36.746841,
        'district_geo_long': -119.772591,
        'map_zoom_level': 13,
        'southwest_lat': 36.620203,
        'southwest_lng': -119.721710,
        'northeast_lat': 36.879697,
        'northeast_lng': -119.295908
    }

    return render(request, 'district_management/district_admin_home.html', context)