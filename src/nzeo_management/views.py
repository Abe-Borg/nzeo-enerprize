from operator import attrgetter
from django.shortcuts import render
from account.models import Account

# Create your views here.
def nzeo_admin_home(request):
    context = {}
    return render(request, 'templates/nzeo_admin_home.html', context)
