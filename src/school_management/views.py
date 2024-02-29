from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from school_management.models import (
    School, UtilityBill, PerformanceMetrics, 
    MeterReading, Equipment, Building
)
from .forms import UtilityBillForm, MeterReadingForm
import school_management.school_management_constants as smc
from district_management.models import SchoolDistrict
from django.forms import inlineformset_factory
from django.contrib import messages
from django.db import transaction


def user_is_NZEO_staff(user):
    return user.groups.filter(name='NZEO-Staff').exists()

@login_required
def school_home(request, school_id):
    # get school data based on what school was selected
    school = get_object_or_404(School, id=school_id)
    context = {
        'school': school,
    }
    return render(request, 'school_management/school_home.html', context)

@login_required
def building_home(request, building_id):
    # get building data based on what building was selected
    building = get_object_or_404(Building, id=building_id)
    context = {
        'building': building,
    }
    return render(request, 'school_management/building_home.html', context)

@login_required
def equipment_home(request, equipment_id):
    # get equipment data based on what equipment specific equipment was selected
    equipment = get_object_or_404(Equipment, id=equipment_id)
    context = {
        'equipment': equipment,
    }
    return render(request, 'school_management/equipment_home.html', context)

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
@user_passes_test(user_is_NZEO_staff)
def check_calculations(request):
    districts = SchoolDistrict.objects.all()
    context = {
        'districts': districts
    }
    return render(request, 'school_management/check_calculations.html', context)

@login_required
def school_analytics(request, school_id):
    # get school data based on what school was selected
    school = get_object_or_404(School, id=school_id)
    context = {
        'school': school,
    }
    return render(request, 'school_management/school_analytics.html', context)

