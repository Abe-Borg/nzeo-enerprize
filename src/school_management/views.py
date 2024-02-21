from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from school_management.models import School, UtilityBill, PerformanceMetrics, MeterReading
from .forms import UtilityBillForm, MeterReadingForm
import school_management.school_management_constants as smc
from district_management.models import SchoolDistrict
from django.forms import inlineformset_factory
from django.contrib import messages
from django.db import transaction


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
@transaction.atomic
def add_utility_bill(request):
    utility_type_choices = smc.UTILITY_TYPE
    districts = SchoolDistrict.objects.none()
    user = request.user

    # Determine the districts available to the user
    if user.groups.filter(name='NZEO-Staff').exists():
        districts = SchoolDistrict.objects.all()
    elif user.groups.filter(name='District-Staff').exists():
        districts = SchoolDistrict.objects.filter(district_name=user.profile.user_district)

    # Setup the MeterReadingFormSet
    MeterReadingFormSet = inlineformset_factory(
        UtilityBill,
        MeterReading,
        form=MeterReadingForm,
        extra=1,
        can_delete=True
    )

    if request.method == 'POST':
        form = UtilityBillForm(request.POST)
        formset = MeterReadingFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            utility_bill = form.save(commit=False)
            utility_bill.save()

            # Now save the formset with the newly created UtilityBill instance
            formset.instance = utility_bill
            formset.save()

            if 'action' in request.POST:
                if request.POST['action'] == 'save_and_add_another':
                    messages.success(request, 'Utility bill has been added successfully, please add another.')
                    return redirect('add_utility_bill')
    else:
        form = UtilityBillForm()
        formset = MeterReadingFormSet()

    return render(request, 'school_management/add_utility_bill.html', {
        'form': form,
        'formset': formset,
        'utility_type_choices': utility_type_choices,
        'districts': districts
    })


@login_required
def check_calculations(request):
    context = {smc.UNIT_CONVERSIONS}

    return render(request, 'school_management/check_calculations.html', context)

