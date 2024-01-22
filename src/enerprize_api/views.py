# api/views.py
from django.shortcuts import render
# from rest_framework import viewsets, permissions
# from .serializers import UserSerializer, GroupSerializer, AccountSerializer
# from django.http import HttpResponse
# import json
# import requests
# from django.http import JsonResponse
# import xml.etree.ElementTree as ET


# # api call for green button data
# # this api will call the green button data utility and serve to the dashboards
# def fetch_green_button_data(request):
#     # call green button data utility
#     # return json data
#     url = 'https://api.utilitycompany.com/greenbuttondata'  # placeholder url
#     headers = {'Authorization': 'Bearer ' + 'token'}  # placeholder token

#     response = requests.get(url, headers = headers)
#     if response.status_code == 200:
#         return JsonResponse(response.json())
#     else:
#         return JsonResponse({'error': 'Failed to fetch data'}, status=500)


# xml_data = '''<feed> ... </feed>''' # placeholder xml data
# root = ET.fromstring(xml_data)
# for entry in root.findall('entry'):
#     title = entry.find('title').text
#     if title == "Electricity Usage":
#         for interval_block in entry.findall('.//IntervalBlock'):
#             for interval_reading in interval_block.findall('IntervalReading'):
#                 value = interval_reading.find('value').text
#                 start = interval_reading.find('.//start').text
#                 print(f"Usage: {value}, Start Time: {start}")
#     elif title == "Customer Information":
#         customer = entry.find('.//Customer')
#         name = customer.find('name').text
#         id = customer.find('id').text
#         location = customer.find('serviceLocation').text
#         print(f"Customer: {name}, ID: {id}, Location: {location}")

# The XML data is parsed using ET.fromstring(xml_data).
# The findall() method is used to iterate over all entry elements.
# The if condition checks the title of each entry and processes the data accordingly.
# For the "Electricity Usage" entry, it iterates over each IntervalReading to extract the usage value and start time.
# For the "Customer Information" entry, it extracts the customer's name, ID, and location.


# # api endpoint for user data
# def list_all_users(request):
#     # get all users from database
#     # return json data
#     return JsonResponse({'users': 'all users'})  # placeholder

# def view_user(request, user_id):
#     # get user from database
#     # return json data
#     return JsonResponse({'user': user_id})  # placeholder

# def create_user(request):
#     return 'placeholder'

# def update_user(request, user_id):
#     return 'placeholder'

# def delete_user(request, user_id):
#     return 'placeholder'

def chatnzeo(request):
    return render(request, 'chatnzeo.html')