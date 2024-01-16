# api/views.py
# in views.py we can include functions and even classes.

from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, AccountSerializer
from django.http import HttpResponse
import json
import requests
from django.http import JsonResponse


# api call for green button data
# this api will call the green button data utility and serve to the dashboards
def fetch_green_button_data(request):
    # call green button data utility
    # return json data
    url = 'https://api.utilitycompany.com/greenbuttondata'  # placeholder url
    headers = {'Authorization': 'Bearer ' + 'token'}  # placeholder token

    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=500)



# api endpoint for user data
def list_all_users(request):
    # get all users from database
    # return json data
    return JsonResponse({'users': 'all users'})  # placeholder

def view_user(request, user_id):
    # get user from database
    # return json data
    return JsonResponse({'user': user_id})  # placeholder

def create_user(request):
    return 'placeholder'

def update_user(request, user_id):
    return 'placeholder'

def delete_user(request, user_id):
    return 'placeholder'