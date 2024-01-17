from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def site_staff_home(request):
    context = {}
    return render(request, 'templates/site_staff_home.html', context)