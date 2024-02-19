from django.db import models
from district_management.models import SchoolDistrict
import school_management.school_management_constants as smc

class School(models.Model):
    school_district = models.ForeignKey(SchoolDistrict, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    school_address = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    school_student_population = models.IntegerField(default=0)
    school_student_percent_disadvantaged = models.IntegerField(default=0) 
    school_student_percent_english_learners = models.IntegerField(default=0)

    def calculate_school_area_sqft(self):
        # Summing the area of all related buildings, dynamic cals so that it is always up to date
        # area will change when schools are loaded up with real data.
        return self.building_set.aggregate(models.Sum('building_area_sqft'))['building_area_sqft__sum'] or 0

    def __str__(self):
        return str(self.school_name)
    

class UtilityProviderAccountNumber(models.Model):
    # per district, per utility. a district can have multiple account numbers. 1 account number per utility per district
    account_number = models.CharField(max_length = 100, primary_key=True)
    utility_provider = models.CharField(max_length=100, choices = smc.UTILITY_PROVIDERS)
    utility_type = models.CharField(max_length = 100, choices = smc.UTILITY_TYPE)
    account_district = models.ForeignKey(SchoolDistrict, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    

class ServiceAgreement(models.Model):
    # per school, per utility
    service_agreement_id = models.CharField(max_length = 100 , primary_key=True)
    utility_type = models.CharField(max_length = 100, choices = smc.UTILITY_TYPE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    utility_provider_account_number = models.ForeignKey(UtilityProviderAccountNumber, on_delete=models.SET_NULL, null=True, blank=True, default=None, verbose_name="Associated Utility Provider Account Number")


class Building(models.Model):
    building_school = models.ForeignKey(School, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=100, default='building_name')
    building_type = models.CharField(max_length=100, choices=smc.BUILDING_TYPES)
    building_area_sqft = models.IntegerField()
    building_coordinates = models.JSONField() # coordinates dynamically set by nzeo staff
    building_age = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the building instance first

        # Now calculate the sum of all building areas for the related school
        total_area = Building.objects.filter(
            building_school=self.building_school
        ).aggregate(sum=models.Sum('building_area_sqft'))['sum'] or 0

        # Update the school_area_sqft field of the related School instance
        self.building_school.school_area_sqft = total_area
        self.building_school.save()

    def __str__(self):
        # return everything
        return 'School: '+ str(self.building_school) + ' ' + 'Building Name: ' + str(self.building_name)
    

class Equipment(models.Model):
    equipment_school = models.ForeignKey(School, on_delete=models.CASCADE)
    equipment_building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True, default = None, verbose_name="Associated Building")
    equipment_tag = models.CharField(max_length=100, default='equipment_tag')
    equipment_type = models.CharField(max_length=100, choices = smc.ELECTRICAL_EQUIPMENT_TYPES + smc.MECHANICAL_EQUIPMENT_TYPES + smc.PLUMBING_EQUIPMENT_TYPES)
    equipment_manufacturer = models.CharField(max_length=100, choices = smc.MANUFACTURERS)
    equipment_model = models.CharField(max_length=100, default='equipment_model')
    equipment_serial_number = models.CharField(max_length=100, default='equipment_serial_number')
    equipment_install_date = models.DateField()
    equipment_warranty_expiration = models.DateField(auto_now=False, auto_now_add=False)
    equipment_coordinates = models.JSONField() # location will be dynamically set by user by placing markup on a map.
    equipment_notes = equipment_notes = models.TextField(max_length=200, blank=True, default='equipment_notes')
    equipment_elec_kw_demand = models.IntegerField(default = 0)
    equipment_gas_btuh_demand = models.IntegerField(default = 0)
    equipment_generates_elec_kw = models.IntegerField(default = 0)
    equipment_storage_kwh = models.IntegerField(default = 0)
    equipment_storage_kbtu = models.IntegerField(default = 0)
    equipment_location = models.CharField(max_length=100, default='equipment_location')


    def __str__(self):
        return str(self.equipment_tag)
    
    def save(self, *args, **kwargs):
        if self.equipment_building and self.equipment_building.school != self.equipment_school:
            raise ValueError("The building is not part of the assigned school.")
        super().save(*args, **kwargs)


class Meter(models.Model):
    # multiple meters can be associated with a single service agreement
    meter_id = models.IntegerField(primary_key=True)
    meter_school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    meter_building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True)
    meter_service_agreement_id = models.ForeignKey(ServiceAgreement, on_delete=models.SET_NULL, null=True, blank=True)


class UtilityBill(models.Model):
    # each utility bill is associated with one service agreement
    utility_type = models.CharField(max_length=100, choices = smc.UTILITY_TYPE)
    district = models.ForeignKey(SchoolDistrict, on_delete=models.SET_NULL, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    service_agreement_id = models.ForeignKey(ServiceAgreement, on_delete=models.SET_NULL, null= True, default=0)
    bill_statement_date = models.DateField()
    bill_start_date = models.DateField()
    bill_end_date = models.DateField()
    total_electric_usage_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    total_electric_charges = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    total_gas_usage_therms = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    total_gas_charges = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    solar_energy_credits = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    total_demand_charge_kw = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    total_solar_generation_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    total_off_peak_consumption_kwh = models.IntegerField(default=0)
    total_peak_consumption_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    total_part_peak_consumption_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    solar_energy_credits = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)


class MeterReading(models.Model):
    meter_id = models.ForeignKey(Meter, on_delete=models.CASCADE)
    utility_bill = models.ForeignKey(UtilityBill, on_delete=models.CASCADE)
    elec_consumption_kwh = models.DecimalField(max_digits = 10, decimal_places = 2,  default=0.00)
    gas_consumption_therms = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    peak_consumption_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    off_peak_consumption_kwh = models.IntegerField(default=0)
    part_peak_consumption_kwh = models.IntegerField(default=0)
    demand_charge_kw = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    solar_generation_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    

class PerformanceMetrics(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    gas_bill_id = models.ForeignKey(UtilityBill, on_delete=models.SET_NULL, null=True, default=None, related_name='gas_bill_id')
    elec_bill_id = models.ForeignKey(UtilityBill, on_delete=models.SET_NULL, null=True, default=None, related_name='elec_bill_id')
    assigned_month = models.CharField(max_length=100, choices = smc.MONTHS, default='January')

    elec_energy_intensity_kwh_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    gas_energy_intensity_kbtu_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    energy_use_intensity_combined_kbtu_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sum of energy use and gross area (gas and electric)
    
    elec_energy_intensity_kwh_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    gas_energy_intensity_kbtu_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    energy_use_intensity_combined_kbtu_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sum of energy use and student population (gas and electric)
    
    elec_energy_cost_index_dollar_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    gas_energy_cost_index_dollar_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    energy_cost_index_combined_dollar_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sum of energy cost and gross area (gas and electric)
    
    elec_energy_cost_index_dollar_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    gas_energy_cost_index_dollar_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    energy_cost_index_combined_dollar_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sum of energy cost and student population (gas and electric)

    lbs_natural_gas_nh4 = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    lbs_co2_per_lb_nh4 = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    
    scope1_co2e_gas_lbs = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # Lbs of CO2e from Energy Use Gas (methane - CH4)
    scope2_co2e_elec_lbs = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # Lbs of CO2e from Energy Use Elec (CAMX grid)

    cui_scope1_gas_lbs_co2e_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    cui_scope2_elec_lbs_co2e_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    cui_total_lbs_co2e_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)

    cui_scope1_gas_lbs_co2e_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    cui_scope2_elec_lbs_co2e_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    cui_total_lbs_co2e_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    
    # solar energy metrics
    net_elec_consumption_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # Electric consumption (from utility bills) - Solar generation
    net_cost_dollars = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # Electric cost (from utility bills) - Solar energy credits
