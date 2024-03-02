from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def nzeo_admin_home(request):
    context = {}
    return render(request, 'nzeo_management/nzeo_admin_home.html', context)


@login_required
def all_districts_leaderboards(request):
    context = {}
    return render(request, 'nzeo_management/all_districts_leaderboards.html', context)