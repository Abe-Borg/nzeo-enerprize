from django.shortcuts import render

# Create your views here.
def district_admin_home(request):
    context = {}
    return render(request, 'templates/district_admin_home.html', context)