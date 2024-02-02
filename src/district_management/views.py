from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import googlemaps
from district_management.models import SchoolDistrict
from school_management.models import School
gmaps = googlemaps.Client(key='AIzaSyANW4JtLihHDKEiBkkknOHOn6CCX-WwthA')


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
        'district_name': district_info.district_name,
        'map_zoom_level': 12,
        'API_KEY': 'AIzaSyANW4JtLihHDKEiBkkknOHOn6CCX-WwthA'
    }

    district_schools_list = School.objects.filter(school_district = assigned_district)
    named_locations = [{'name': school.school_name, 'address': school.school_address} for school in district_schools_list]
    district_schools_coordinates = get_coordinates_for_named_locations(named_locations)
    context['district_schools_coordinates'] = district_schools_coordinates
    return render(request, 'district_management/district_admin_home.html', context)


def get_geo_coordinates(address):
    """
    Retrieve the geographical coordinates (latitude and longitude) for a given address.
    This function uses the Google Maps Geocoding API to convert an address into a set of 
    geographical coordinates. It extracts the latitude and longitude from the geocoding 
    result and returns them.
    Parameters:
    address (str): The address for which the geographical coordinates are to be obtained.
    Returns:
    tuple: A tuple containing the latitude and longitude of the given address.
    Raises:
    IndexError: If the geocode result is empty, indicating the address was not found.
    """
    geocode_result = gmaps.geocode(address)
    latitude = geocode_result[0]['geometry']['location']['lat']
    longitude = geocode_result[0]['geometry']['location']['lng']
    return latitude, longitude


def get_coordinates_for_named_locations(named_locations):
    """
    Get geographical coordinates for a list of named locations.
    This function iterates through a list of named locations, each with a name and an address.
    It uses the `get_geo_coordinates` function to retrieve latitude and longitude for each address.
    The resulting coordinates, along with the name, are stored in a list of dictionaries. If the
    geocoding for an address fails (due to an IndexError), it prints a message and continues with
    the next location.
    Parameters:
    named_locations (list of dict): A list of dictionaries, each containing the 'name' and 'address'
                                    of a location.
    Returns:
    list of dict: A list of dictionaries, each containing the 'name', 'lat' (latitude), and 'lng' 
                  (longitude) for each successfully geocoded location.
    Note:
    The function will print a message for each location where geocoding fails and will not include
    these locations in the returned list.
    """
    marker_data = []
    for location in named_locations:
        name, address = location['name'], location['address']
        try:
            lat, lng = get_geo_coordinates(address)
            marker_data.append({'name': name, 'lat': lat, 'lng': lng})
        except IndexError:
            print(f"Geocoding failed for address: {address}")
            continue 
    return marker_data

