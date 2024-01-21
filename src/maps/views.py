from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin


# @login_required
def overall_map(request, *args, **kwargs):
    return render(request, 'maps/overall_map.html')

def district_map(request, *args, **kwargs):
    return render(request, 'maps/district_map.html')

def school_map(request, *args, **kwargs):
    return render(request, 'maps/school_map.html')

def building_map(request, *args, **kwargs):
    return render(request, 'maps/building_map.html')