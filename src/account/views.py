# account/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from account.forms import AccountUpdateForm, RegistrationForm, AccountAuthenticationForm


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=email, password=raw_password)
            login(request, account)
            return HttpResponseRedirect(reverse('enerprize_home'))
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('enerprize_home'))


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return HttpResponseRedirect(reverse('enerprize_home'))
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('enerprize_home'))
    else:
        form = AccountAuthenticationForm()
    
    context['login_form'] = form
    return render(request, 'account/login.html', context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            if form.has_changed():
                form.save()
                messages.success(request, 'Updated')
            else:
                messages.info(request, 'No changes were made.')
            return redirect('account')
    else:
        form = AccountUpdateForm(
            initial={
                'email': request.user.email,
                'username': request.user.username,
            }
        )    
    return render(request, 'account/account.html', {'account_form': form})


def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.html', {})