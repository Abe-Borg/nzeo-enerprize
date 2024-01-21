from django.shortcuts import render

def site_staff_home(request):
    context = {}
    return render(request, 'school_management/site_staff_home.html', context)

def school_home(request):
    context = {}
    return render(request, 'school_management/school_home.html', context)