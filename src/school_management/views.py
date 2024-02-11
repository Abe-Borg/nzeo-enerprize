from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from school_management.models import School
from .forms import UtilityBillForm


@login_required
def school_home(request):
    '''This view is used to render the school home page for school staff
    '''
    school_info = School.objects.get(school_name = request.user.profile.user_school)
    context = {
        'school_name': school_info.school_name,
        'school_district': school_info.school_district,
    }
    return render(request, 'school_management/school_home.html', context)



@login_required
def add_utility_bill(request):
    if request.method == 'POST':
        form = UtilityBillForm(request.POST)
        if form.is_valid():
            utility_bill = form.save(commit=False)
            if 'action' in request.POST:
                if request.POST['action'] == 'save_and_add_another':
                    utility_bill.save()
                    return redirect('add_utility_bill')
                elif request.POST['action'] == 'save_and_return':
                    utility_bill.save()
                    return redirect('nzeo_admin_home') 
    else:
        form = UtilityBillForm()
    return render(request, 'add_utility_bill.html', {'form': form})





