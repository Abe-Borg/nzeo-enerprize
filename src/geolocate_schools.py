import googlemaps
from district_management.models import SchoolDistrict
from school_management.models import School

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from django.db import connection

def geolocate_schools():
    gmaps = googlemaps.Client(key='AIzaSyANW4JtLihHDKEiBkkknOHOn6CCX-WwthA')
    schools = School.objects.all()
    
    for school in schools:
        if school.latitude is None or school.longitude is None:
            # Geolocate the school
            geocode_result = gmaps.geocode(school.address)
            if geocode_result:
                # Assume the first result is the most relevant
                latitude = geocode_result[0]['geometry']['location']['lat']
                longitude = geocode_result[0]['geometry']['location']['lng']
                
                # Save the coordinates to the school object
                school.latitude = latitude
                school.longitude = longitude
                school.save()
                print(f"Coordinates saved for {school.name}")
            else:
                print(f"Geolocation failed for {school.address}")
        else:
            print(f"Coordinates already stored for {school.name}")


geolocate_schools()