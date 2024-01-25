from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyANW4JtLihHDKEiBkkknOHOn6CCX-WwthA')

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
        'map_zoom_level': 12,
        'southwest_lat': 36.620203,
        'southwest_lng': -119.721710,
        'northeast_lat': 36.879697,
        'northeast_lng': -119.295908,
        'district_name': 'Sanger Unified School District',
        'API_KEY': 'AIzaSyANW4JtLihHDKEiBkkknOHOn6CCX-WwthA'
    }

    district_schools_list = [
        {"name": 'Centerville Elementary', "address": "48 S Smith Ave, Sanger, CA 93657"},
        {'name': 'Del Rey Elementary', 'address': "10620 Morro Ave, Del Rey, CA 93616"},
        {'name': 'Fairmont Elementary', 'address': "3095 N Greenwood Ave, Sanger, CA 93657"},
        {'name': 'Jackson Elementary', 'address': "1810 3rd St, Sanger, CA 93657"},
        {'name': 'Hallmark Academy', 'address': "2445 9th St, Sanger, CA 93657"},
        {'name': 'Jefferson Elementary', 'address': "1110 Tucker, Sanger, CA 93657"},
        {'name': 'Lincoln Elementary', 'address': "1700 14th St, Sanger, CA 93657"},
        {'name': 'John Wash Elementary', 'address': "6350 E Lane Ave, Fresno, CA 93727"},
        {'name': 'Lone Stary Elementary', 'address': "2617 S Fowler Ave, Fresno, CA 93725"},
        {'name': 'Reagan Elementary', 'address': "1586 S Indianola Ave, Sanger, CA 93657"},
        {'name': 'Madison Elementary', 'address': "2324 Cherry Ave, Sanger, CA 93657"},
        {'name': 'Quail Lake Environmental Charter S chool', 'address': "4087 N Quail Lake Dr, Clovis, CA 93619"},
        {'name': 'Sequoia', 'address': "1820 S Armstrong Ave, Fresno, CA 93727"},
        {'name': 'Sanger Academy Charter School', 'address': "2207 9th St, Sanger, CA 93657"},
        {'name': 'Wilson Elementary', 'address': "610 Faller Ave, Sanger, CA 93657"},
        {'name': 'Centerville Middle', 'address': '48 S Smith Ave, Sanger, CA 93657' },
        {'name': 'Community Day School', 'address': '818 L St, Sanger, CA 93657'},
        {'name': 'Washington Academic', 'address': '1705 10th St, Sanger, CA 93657'},
        {'name': 'Kings River High School', 'address': '1801 7th St, Sanger, CA 93657'},
        {'name': 'Sanger High School', 'address': '1045 Bethel Ave, Sanger, CA 93657'},
        {'name': 'Sanger West High School', 'address': '1850 S Fowler Ave, Fresno, CA 93727'},
        {'name': 'Sanger Adult School', 'address': '1020 N St, Sanger, CA 93657'}
    ]

    

    district_schools_coordinates = get_coordinates_for_named_locations(district_schools_list)
    context['district_schools_coordinates'] = district_schools_coordinates

    return render(request, 'district_management/district_admin_home.html', context)


def get_geo_coordinates(address):
    geocode_result = gmaps.geocode(address)
    latitude = geocode_result[0]['geometry']['location']['lat']
    longitude = geocode_result[0]['geometry']['location']['lng']
    return latitude, longitude


# This function takes a list of named locations and their addresses, 
# geocodes the addresses, and returns a list of dictionaries with names and coordinates.
def get_coordinates_for_named_locations(named_locations):
    marker_data = []
    for location in named_locations:
        name, address = location['name'], location['address']
        try:
            lat, lng = get_geo_coordinates(address)
            marker_data.append({'name': name, 'lat': lat, 'lng': lng})
        except IndexError:
            print(f"Geocoding failed for address: {address}")
            continue  # Skip addresses for which geocoding fails
    return marker_data

