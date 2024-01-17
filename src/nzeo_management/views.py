from operator import attrgetter
from django.shortcuts import render
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required(login_url = 'login')
def nzeo_admin_home(request):
    context = {}
    return render(request, 'templates/nzeo_admin_home.html', context)
