# mysite/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def redirect_after_login(request):
    user = request.user
    if user.groups.filter(name='NZEO Staff').exists():
        return redirect('nzeo_admin_home')
    elif user.groups.filter(name='District Admin').exists():
        return redirect('district_admin_home')
    elif user.groups.filter(name='School Staff').exists():
        return redirect('school_staff_home')
    else:
        return redirect('enerprize_home_page')  # Fallback redirect