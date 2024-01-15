from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, AccountSerializer
from django.http import HttpResponse
import json
import requests

# api call for green button data
# this api will call the green button data utility and serve to the dashboards


def fetch_green_button_data(request):
    # call green button data utility
    # return json data
    url = 'https://api.utilitycompany.com/greenbuttondata'  # placeholder url
    params = {'param1': 'value1', 'param2': 'value2'}  # placeholder params

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return HttpResponse(json.dumps(data), content_type="application/json")





