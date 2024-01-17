# account/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.utils import timezone
from datetime import timedelta
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


def account_view(request):
    """
    Handles the account view for a user. 
    - If the user is not authenticated, they are redirected to the login page. 
    - If the request method is POST, it attempts to update the user's account 
    with the submitted form data. If the form is valid and has changes, it 
    saves the changes and displays a success message. If the form is valid 
    but has no changes, it displays an info message. 
    - If the request method is not POST, it initializes the form with the 
    current user's email and username.
    - Finally, it renders the 'account/account.html' template with the form.

    Parameters:
    request (HttpRequest): The HTTP request object.
    Returns:
    HttpResponse: The HTTP response object.
    """
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


class CustomLoginView(LoginView):
    """
    Custom Login View that extends the built-in LoginView class.
    This view handles the login form submission and sets the session expiry based on the 'remember_me' field value.
    If 'remember_me' is checked, the session will expire after 2 weeks. Otherwise, the session will expire at browser close.
    """
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if remember_me:
            # Set session to expire after 2 weeks
            self.request.session.set_expiry(1209600)  # 2 weeks in seconds
        else:
            # Session expires at browser close
            self.request.session.set_expiry(0)

        return super(CustomLoginView, self).form_valid(form)