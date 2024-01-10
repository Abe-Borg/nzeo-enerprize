from django.shortcuts import render

# Create your views here.
def sanger_high_school(request, *args, **kwargs):
    return render(request, 'sanger_high_school.html')