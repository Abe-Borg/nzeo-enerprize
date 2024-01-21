from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin

# @login_required
def nzeo_admin_home(request):
    context = {}
    return render(request, 'nzeo_management/nzeo_admin_home.html', context)
