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
    school_type = models.CharField(max_length=100, choices = smc.SCHOOL_TYPE)

    def calculate_school_area_sqft(self):
        # Summing the area of all related buildings, dynamic cals so that it is always up to date
        # area will change when schools are loaded up with real data.
        return self.building_set.aggregate(models.Sum('building_area_sqft'))['building_area_sqft__sum'] or 0

    def calculate_electricity_usage(self):
        equipment = self.equipment_set.all()
        total_electricity_demand = sum(equipment.values_list('equipment_elec_kw_demand', flat=True))        
        return total_electricity_demand
    
    def calculate_natural_gas_usage(self):
        equipment = self.equipment_set.all()
        total_gas_demand = sum(equipment.values_list('equipment_gas_btuh_demand', flat=True))
        return total_gas_demand

    def __str__(self):
        return str(self.school_name)
    

class UtilityProviderAccountNumber(models.Model):
    # per district, per utility. a district can have multiple account numbers. 1 account number per utility per district
    account_number = models.CharField(max_length = 100, primary_key=True)
    utility_provider = models.CharField(max_length=100, choices = smc.UTILITY_PROVIDERS)
    utility_type = models.CharField(max_length = 100, choices = smc.UTILITY_TYPE)
    account_district = models.ForeignKey(SchoolDistrict, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    

class ServiceAgreement(models.Model):
    # per school, per utility, multiple service agrements can be associated with a single utility.
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
    meter_building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True)
    meter_service_agreement_id = models.ForeignKey(ServiceAgreement, on_delete=models.SET_NULL, null=True, blank=True)
    
    def get_utility_type(self):
        return self.meter_service_agreement_id.utility_type if self.meter_service_agreement_id else None

    def get_meter_school(self):
        return self.meter_service_agreement_id.school if self.meter_service_agreement_id else None


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
    total_electric_charges_dollars = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    total_demand_charge_kw = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    total_off_peak_consumption_kwh = models.IntegerField(default=0)
    total_peak_consumption_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    total_part_peak_consumption_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    
    total_gas_usage_therms = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    total_gas_charges_dollars = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)

    # all solar related fields
    total_solar_generation_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    solar_energy_credits_dollars = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    electric_net_peak_usage_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    electric_net_part_peak_usage_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    electric_net_off_peak_usage_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    electric_net_usage_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    estimated_total_net_energy_meter_charges_dollars = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    electric_net_energy_meter_charges_dollars = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    solar_imports_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    solar_exports_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    electric_net_usage_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)


class MeterReading(models.Model):
    meter_id = models.ForeignKey(Meter, on_delete=models.CASCADE)
    utility_bill  = models.ForeignKey(UtilityBill, on_delete=models.CASCADE)
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
    assigned_month = models.CharField(max_length=100, choices = smc.MONTHS, default='January') # each performance metric will need to be manually assigned to a month even though the gas and electricity bills may not come in at the same time.
    assigned_year = models.IntegerField(default=2021)

    elec_energy_use_intensity_kwh_per_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sourced from elect energy use (which comes from utility bills) and school area
    elec_energy_use_intensity_kbtu_per_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # this is derived through a conversion factor, multiply elec_energy_use_intensity_kwh_per_sqft by 0.29307107
    natural_gas_energy_use_intensity_kbtu_per_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sourced from gas energy use (which comes from utility bills) and school area
    combined_energy_use_intensity_kbtu_per_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sum of energy use per gross area (gas and electric)
    
    elec_energy_use_intensity_kwh_per_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sourced from elect energy use (which comes from utility bills) and student count
    elec_energy_use_intensity_kbtu_per_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # this is derived through a conversion factor, multiply elec_energy_use_intensity_kwh_per_student by 0.29307107
    natural_gas_energy_use_intensity_kbtu_per_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sourced from gas energy use (which comes from utility bills) and student count
    combined_energy_use_intensity_kbtu_per_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sum of energy use per student population (gas and electric)
    
    elec_energy_use_cost_index_dollar_per_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sourced from elect energy use cost (which comes from utility bills) and school area
    natural_gas_energy_use_cost_index_dollar_per_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sourced from gas energy use cost (which comes from utility bills) and school area
    combined_energy_use_cost_index_dollar_per_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sum of energy cost per gross area (gas and electric)
    
    elec_energy_use_cost_index_dollar_per_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sourced from elect energy use cost (which comes from utility bills) and student count
    natural_gas_energy_use_cost_index_dollar_per_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sourced from gas energy use cost (which comes from utility bills) and student count 
    combined_energy_use_cost_index_dollar_per_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sum of energy cost per student population (gas and electric)

    lbs_natural_gas_from_therms = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # input is gas energy use in therms (this is shown on gas utility bills), this value is then converted to kBTUs (multiply by 99.976) and then the kBTUs value is converted to lbs Natural GAs (CH4) (multiply by 0.042)
    
    scope1_lbs_co2e_from_lbs_natural_gas = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # input is lbs_natural_gas_from_therms, then this value is converted to lbs CO2e (multiply by 25)
    scope2_lbs_co2e_from_kwh_elec_camx_grid = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # first convert kwh to mwh (divid by 1000), then convert mwh to lbs co2e (multiply by 531.7)

    cui_scope1_lbs_co2e_per_sqft_from_natural_gas_use = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sourced from scope1_lbs_co2e_from_lbs_natural_gas and school area 
    cui_scope2_lbs_co2e_per_sqft_from_elec_use = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sourced from scope2_lbs_co2e_from_kwh_elec_camx_grid and school area
    cui_total_lbs_co2e_per_sqft = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sum of cui_scope1_lbs_co2e_per_sqft_from_natural_gas_use and cui_scope2_elec_lbs_co2e_per_sqft

    cui_scope1_lbs_co2e_per_student_from_natural_gas_use = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sourced from scope1_lbs_co2e_from_lbs_natural_gas and student count
    cui_scope2_lbs_co2e_per_student_from_elec_use = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sourced from scope2_lbs_co2e_from_kwh_elec_camx_grid and student count
    cui_total_lbs_co2e_per_student = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # sum of cui_scope1_lbs_co2e_per_student_from_natural_gas_use and cui_scope2_elec_lbs_co2e_per_student
    
    # solar energy metrics
    net_elec_consumption_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # Electric consumption (from utility bills) - Solar generation
    net_cost_dollars = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00) # Electric cost (from utility bills) - Solar energy credits
