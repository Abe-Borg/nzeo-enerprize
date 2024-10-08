# mysite/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserEmailForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from district_management.models import SchoolDistrict

@login_required
def redirect_after_login(request):
    user = request.user
    if user.groups.filter(name='NZEO-Staff').exists():
        return redirect('nzeo_admin_home')
    elif user.groups.filter(name='District-Staff').exists():
        return redirect('district_admin_home')
    elif user.groups.filter(name='School-Staff').exists():
        return redirect('school_home')
    else:
        return redirect('error_page')


def create_account(request):
    districts = SchoolDistrict.objects.all()
    if request.method == 'POST':    
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
        'districts': districts,
    }
    return render(request, 'create_account.html', context)


def error_page(request):
    return render(request, 'error_page.html')

@login_required
def change_email(request):
    if request.method == 'POST':
        email_form = UserEmailForm(request.POST, instance=request.user)
        if email_form.is_valid():
            email_form.save()
            # Redirect to some success page or add a success message
            return redirect('account_settings')
    else:
        email_form = UserEmailForm(instance=request.user)
    return render(request, 'account_settings.html', {'email_form': email_form})


@login_required
def change_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important for keeping the user logged in
            return redirect('account_settings') 
    else:
        password_form = PasswordChangeForm(request.user)

    return render(request, 'account_settings.html', {
        'password_form': password_form
    })