from django.shortcuts import render

def site_staff_home(request):
    context = {}
    return render(request, 'templates/site_staff_home.html', context)