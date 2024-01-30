from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def site_staff_home(request):
    context = {}
    return render(request, 'school_management/site_staff_home.html', context)

@login_required
def school_home(request):
    context = {}
    return render(request, 'school_management/school_home.html', context)