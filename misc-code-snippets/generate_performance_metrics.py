import numpy as np
from decimal import Decimal
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from school_management.models import School, PerformanceMetrics  
import school_management.school_management_constants as smc 

# Constants for synthetic data generation
ELECTRIC_USAGE_VARIANCE = 0.25
GAS_USAGE_VARIANCE = 0.25
CO2E_PER_KWH = 531.7  # Scope 2 emissions factor
CO2E_PER_THERM = 25  # Scope 1 emissions factor
KWH_TO_KBTU = 0.29307107
THERMS_TO_KBTU = 99.976
THERMS_TO_LBS_NATURAL_GAS = 0.042

# sample data 
electric_usage_samples = [36404, 33111, 36041, 31493, 38290, 49598, 60906, 51895, 67620, 51757, 39964, 37815]
electric_cost_samples = [9942, 9599, 10150, 9097, 12273, 15905, 19537, 19920, 23110, 16974, 13329, 11713]
gas_usage_samples = [1929, 2210, 2288, 1798, 570, 143, 70, 44, 82, 174, 702, 312]
gas_cost_samples = [2745.31, 3164.58, 3291.52, 2659.81, 773.23, 226.29, 136.86, 399.93, 170.11, 313.18, 665.67, 3092.29]

def generate_synthetic_value(sample_value):
    deviation = np.random.uniform(-0.25, 0.25)
    return sample_value * (1 + deviation)

def generate_synthetic_data_for_month(sample_values):
    return [generate_synthetic_value(value) for value in sample_values]

def generate_synthetic_data(school_id, year):
    try:
        school = School.objects.get(pk=school_id)
    except School.DoesNotExist:
        print(f"School with ID {school_id} not found.")
        return

    synthetic_electric_usage = generate_synthetic_data_for_month(electric_usage_samples)
    synthetic_electric_cost = generate_synthetic_data_for_month(electric_cost_samples)
    synthetic_gas_usage = generate_synthetic_data_for_month(gas_usage_samples) 
    synthetic_gas_cost = generate_synthetic_data_for_month(gas_cost_samples) 

    months = [month[0] for month in smc.MONTHS]


    for month_index in range(1, 13):
        elec_energy_use_intensity_kwh_per_sqft = synthetic_electric_usage[month_index - 1] / school.calculate_school_area_sqft() 
        elec_energy_use_intensity_kbtu_per_sqft = elec_energy_use_intensity_kwh_per_sqft * KWH_TO_KBTU 
        natural_gas_energy_use_intensity_kbtu_per_sqft = synthetic_gas_usage[month_index - 1] * THERMS_TO_KBTU / school.calculate_school_area_sqft() 
        combined_energy_use_intensity_kbtu_per_sqft = elec_energy_use_intensity_kbtu_per_sqft + natural_gas_energy_use_intensity_kbtu_per_sqft

        elec_energy_use_intensity_kwh_per_student = synthetic_electric_usage[month_index - 1] / school.school_student_population 
        elec_energy_use_intensity_kbtu_per_student = elec_energy_use_intensity_kwh_per_student * KWH_TO_KBTU 
        natural_gas_energy_use_intensity_kbtu_per_student = synthetic_gas_usage[month_index - 1] * THERMS_TO_KBTU / school.school_student_population  
        combined_energy_use_intensity_kbtu_per_student = elec_energy_use_intensity_kbtu_per_student + natural_gas_energy_use_intensity_kbtu_per_student 

        elec_energy_use_cost_index_dollar_per_sqft = synthetic_electric_cost[month_index - 1] / school.calculate_school_area_sqft() 
        natural_gas_energy_use_cost_index_dollar_per_sqft = synthetic_gas_cost[month_index - 1] / school.calculate_school_area_sqft() 
        combined_energy_use_cost_index_dollar_per_sqft = elec_energy_use_cost_index_dollar_per_sqft + natural_gas_energy_use_cost_index_dollar_per_sqft 

        elec_energy_use_cost_index_dollar_per_student = synthetic_electric_cost[month_index - 1] / school.school_student_population 
        natural_gas_energy_use_cost_index_dollar_per_student = synthetic_gas_cost[month_index - 1] / school.school_student_population 
        combined_energy_use_cost_index_dollar_per_student = elec_energy_use_cost_index_dollar_per_student + natural_gas_energy_use_cost_index_dollar_per_student 

        lbs_natural_gas_from_therms = synthetic_gas_usage[month_index - 1] * THERMS_TO_KBTU * THERMS_TO_LBS_NATURAL_GAS
        scope1_lbs_co2e_from_lbs_natural_gas = lbs_natural_gas_from_therms * CO2E_PER_THERM
        scope2_lbs_co2e_from_kwh_elec_camx_grid = (synthetic_electric_usage[month_index - 1] / 1000) * CO2E_PER_KWH

        cui_scope1_lbs_co2e_per_sqft_from_natural_gas_use = scope1_lbs_co2e_from_lbs_natural_gas / school.calculate_school_area_sqft()
        cui_scope2_lbs_co2e_per_sqft_from_elec_use = scope2_lbs_co2e_from_kwh_elec_camx_grid / school.calculate_school_area_sqft()
        cui_total_lbs_co2e_per_sqft = cui_scope1_lbs_co2e_per_sqft_from_natural_gas_use + cui_scope2_lbs_co2e_per_sqft_from_elec_use

        cui_scope1_lbs_co2e_per_student_from_natural_gas_use = scope1_lbs_co2e_from_lbs_natural_gas / school.school_student_population
        cui_scope2_lbs_co2e_per_student_from_elec_use = scope2_lbs_co2e_from_kwh_elec_camx_grid / school.school_student_population
        cui_total_lbs_co2e_per_student = cui_scope1_lbs_co2e_per_student_from_natural_gas_use + cui_scope2_lbs_co2e_per_student_from_elec_use

        # Convert float results to Decimal, suitable for DecimalField in Django model
        elec_energy_use_intensity_kwh_per_sqft = Decimal(str(elec_energy_use_intensity_kwh_per_sqft))
        elec_energy_use_intensity_kbtu_per_sqft = Decimal(str(elec_energy_use_intensity_kbtu_per_sqft))
        natural_gas_energy_use_intensity_kbtu_per_sqft = Decimal(str(natural_gas_energy_use_intensity_kbtu_per_sqft))
        combined_energy_use_intensity_kbtu_per_sqft = Decimal(str(combined_energy_use_intensity_kbtu_per_sqft))
        elec_energy_use_intensity_kwh_per_student = Decimal(str(elec_energy_use_intensity_kwh_per_student))
        elec_energy_use_intensity_kbtu_per_student = Decimal(str(elec_energy_use_intensity_kbtu_per_student))
        natural_gas_energy_use_intensity_kbtu_per_student = Decimal(str(natural_gas_energy_use_intensity_kbtu_per_student))
        combined_energy_use_intensity_kbtu_per_student = Decimal(str(combined_energy_use_intensity_kbtu_per_student))
        elec_energy_use_cost_index_dollar_per_sqft = Decimal(str(elec_energy_use_cost_index_dollar_per_sqft))
        natural_gas_energy_use_cost_index_dollar_per_sqft = Decimal(str(natural_gas_energy_use_cost_index_dollar_per_sqft))
        combined_energy_use_cost_index_dollar_per_sqft = Decimal(str(combined_energy_use_cost_index_dollar_per_sqft))
        elec_energy_use_cost_index_dollar_per_student = Decimal(str(elec_energy_use_cost_index_dollar_per_student))
        natural_gas_energy_use_cost_index_dollar_per_student = Decimal(str(natural_gas_energy_use_cost_index_dollar_per_student))
        combined_energy_use_cost_index_dollar_per_student = Decimal(str(combined_energy_use_cost_index_dollar_per_student))
        lbs_natural_gas_from_therms = Decimal(str(lbs_natural_gas_from_therms))
        scope1_lbs_co2e_from_lbs_natural_gas = Decimal(str(scope1_lbs_co2e_from_lbs_natural_gas))
        scope2_lbs_co2e_from_kwh_elec_camx_grid = Decimal(str(scope2_lbs_co2e_from_kwh_elec_camx_grid))
        cui_scope1_lbs_co2e_per_sqft_from_natural_gas_use = Decimal(str(cui_scope1_lbs_co2e_per_sqft_from_natural_gas_use))
        cui_scope2_lbs_co2e_per_sqft_from_elec_use = Decimal(str(cui_scope2_lbs_co2e_per_sqft_from_elec_use))
        cui_total_lbs_co2e_per_sqft = Decimal(str(cui_total_lbs_co2e_per_sqft))
        cui_scope1_lbs_co2e_per_student_from_natural_gas_use = Decimal(str(cui_scope1_lbs_co2e_per_student_from_natural_gas_use))
        cui_scope2_lbs_co2e_per_student_from_elec_use = Decimal(str(cui_scope2_lbs_co2e_per_student_from_elec_use))
        cui_total_lbs_co2e_per_student = Decimal(str(cui_total_lbs_co2e_per_student))



        # create a PerformanceMetrics record and populate it with the calculated values, and save
        performance_metric = PerformanceMetrics(
            school=school,
            gas_bill_id = None,
            elec_bill_id = None,
            assigned_month=months[month_index - 1],
            assigned_year=year,
            elec_energy_use_intensity_kwh_per_sqft=elec_energy_use_intensity_kwh_per_sqft,
            elec_energy_use_intensity_kbtu_per_sqft=elec_energy_use_intensity_kbtu_per_sqft,
            natural_gas_energy_use_intensity_kbtu_per_sqft=natural_gas_energy_use_intensity_kbtu_per_sqft,
            combined_energy_use_intensity_kbtu_per_sqft=combined_energy_use_intensity_kbtu_per_sqft,
            elec_energy_use_intensity_kwh_per_student=elec_energy_use_intensity_kwh_per_student,
            elec_energy_use_intensity_kbtu_per_student=elec_energy_use_intensity_kbtu_per_student,
            natural_gas_energy_use_intensity_kbtu_per_student=natural_gas_energy_use_intensity_kbtu_per_student,
            combined_energy_use_intensity_kbtu_per_student=combined_energy_use_intensity_kbtu_per_student,
            elec_energy_use_cost_index_dollar_per_sqft=elec_energy_use_cost_index_dollar_per_sqft,
            natural_gas_energy_use_cost_index_dollar_per_sqft=natural_gas_energy_use_cost_index_dollar_per_sqft,
            combined_energy_use_cost_index_dollar_per_sqft=combined_energy_use_cost_index_dollar_per_sqft,
            elec_energy_use_cost_index_dollar_per_student=elec_energy_use_cost_index_dollar_per_student,
            natural_gas_energy_use_cost_index_dollar_per_student=natural_gas_energy_use_cost_index_dollar_per_student,
            combined_energy_use_cost_index_dollar_per_student=combined_energy_use_cost_index_dollar_per_student,
            lbs_natural_gas_from_therms=lbs_natural_gas_from_therms,
            scope1_lbs_co2e_from_lbs_natural_gas=scope1_lbs_co2e_from_lbs_natural_gas,
            scope2_lbs_co2e_from_kwh_elec_camx_grid=scope2_lbs_co2e_from_kwh_elec_camx_grid,
            cui_scope1_lbs_co2e_per_sqft_from_natural_gas_use=cui_scope1_lbs_co2e_per_sqft_from_natural_gas_use,
            cui_scope2_lbs_co2e_per_sqft_from_elec_use=cui_scope2_lbs_co2e_per_sqft_from_elec_use,
            cui_total_lbs_co2e_per_sqft=cui_total_lbs_co2e_per_sqft,
            cui_scope1_lbs_co2e_per_student_from_natural_gas_use=cui_scope1_lbs_co2e_per_student_from_natural_gas_use,
            cui_scope2_lbs_co2e_per_student_from_elec_use=cui_scope2_lbs_co2e_per_student_from_elec_use,
            cui_total_lbs_co2e_per_student=cui_total_lbs_co2e_per_student,
        )
        performance_metric.save()

# Generate synthetic data for all schools
for school in School.objects.all():
    generate_synthetic_data(school.id, 2021)
    generate_synthetic_data(school.id, 2022)
    generate_synthetic_data(school.id, 2023)