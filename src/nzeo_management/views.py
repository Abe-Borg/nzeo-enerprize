from operator import attrgetter
from django.shortcuts import render
from account.models import Account

# Create your views here.
def nzeo_admin_home(request):
    context = {}
    return render(request, 'templates/nzeo_admin_home.html', context)

def district_admin_home(request):
    context = {}
    return render(request, 'templates/district_admin_home.html', context)

def site_staff_home(request):
    context = {}
    return render(request, 'templates/site_staff_home.html', context)