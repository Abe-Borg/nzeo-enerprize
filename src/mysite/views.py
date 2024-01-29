# mysite/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

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



def create_account(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            # later, I need to add additional logic here for sending a confirmation email, logging the user in, redirecting to a specific page, etc.)
            # Redirect to login page.
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'create_account.html', {'form': form})