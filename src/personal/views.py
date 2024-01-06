from operator import attrgetter
from django.shortcuts import render
from account.models import Account

# Create your views here.
def home_screen_view(request):
    context = {}
    return render(request, 'personal/home.html', context)