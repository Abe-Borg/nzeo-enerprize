from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from school_management.models import School, UtilityBill
from .forms import UtilityBillForm

UNITS_OF_MEASURE = (
    ('kwh', 'Kilowatt hours'),
    ('kw', 'Kilowatts'),
    ('therms', 'Therms'),
    ('gallons', 'Gallons'),
    ('BTUH', 'British Thermal Units per hour'),
    ('sqft', 'Square Feet'),
    ('CO2e', 'Carbon Dioxide Equivalent'),
    ('lbs', 'Pounds'),
    ('kWh/sqft', 'Kilowatt hours per square foot'),
    ('kBTU/sqft', 'kilo British Thermal Units per square foot'),
    ('kWh/student', 'Kilowatt hours per student'),
    ('kBTU/student', 'kilo British Thermal Units per student'),
    ('$/sqft', 'Dollars per square foot'),
    ('$/student', 'Dollars per student'),
    ('lbs CO2e/sqft', 'Pounds of CO2e per square foot'),
    ('lbs CO2e/student', 'Pounds of CO2e per student'),
)
UNIT_CONVERSIONS = (
    ('lbs/metric_ton', 2204.62),
    ('BTU/kWh', 0.00029307),
    ('kBTU/kWh', 0.29307),
    ('kWh/kBTU', 3.412),
    ('kWh/MMBTU', 0.03412),
    ('kBTU/therm', 99.976),
    ('MMBTU/therm', 0.100),
    ('kWh/MWh', 0.001),
    ('CO2/CO2e', 1.0),
    ('CH4/CO2e', 25.0),
    ('CAMX(lbs CO2e/MWh)', 531.7),
    ('CAMX(lbs CO2e/kWh)', 0.532),
    ('CAMX GHG Factor, kg CO2e/kWh', 0.276),
    ('Methane(kBTU/lbs) NH4 natural gas', 23.81),
    ('Methane (lbs/kBTU) NH4 natural gas', 0.042),
)

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
    utility_type_choices = UtilityBill.UTILITY_TYPE
    if request.method == 'POST':
        form = UtilityBillForm(request.POST)
        if form.is_valid():
            utility_bill = form.save(commit=False)
            utility_bill.save()
            if 'action' in request.POST:
                if request.POST['action'] == 'save_and_add_another':
                    return redirect('add_utility_bill')
                elif request.POST['action'] == 'save_and_return':
                    return redirect('nzeo_admin_home') 
    else:
        form = UtilityBillForm()
    return render(request, 'school_management/add_utility_bill.html', {'form': form, 'utility_type_choices': utility_type_choices})





