# mysite/views.py
from django.shortcuts import render
from . import settings

def enerprize_home(request):
    return render(request, f"{settings.BASE_DIR}/templates/enerprize_home_page.html")