from django.db import models
from district_management.models import SchoolDistrict

UTILITY_TYPE = (
        ('natural_gas', 'Natural Gas'),
        ('electric', 'Electric'),
        ('solar', 'Solar'),
)
UTILITY_PROVIDERS = (
    ('pg_e', 'Pacific Gas & Electric'),
    ('sce', 'Souther CA Edison'),
)
INTERVAL_TIME_ZONES = (
    ('us_pacific', 'US/Pacific'),
)
BUILDING_TYPES = (
    ('classroom', 'Classroom Building'),
    ('laboratory', 'Laboratory'),
    ('library', 'Library'),
    ('restrooms', 'Restrooms'),
    ('cafeteria', 'Cafeteria'),
    ('gymnasium', 'Gymnasium'),
    ('auditorium', 'Auditorium'),
    ('administrative', 'Administrative'),
    ('maintenance', 'Maintenance'),
    ('storage', 'Storage'),
    ('parking', 'Parking'),
    ('sports', 'Sports'),
    ('playground', 'Playground'),
    ('outdoor', 'Outdoor'),
    ('other', 'Other'),
    ('arts', 'Arts'),
    ('music', 'Music'),
    ('theater', 'Theater'),
    ('workshop', 'Workshop'),
    ('kitchen', 'Kitchen'),
    ('health', 'Health'),
    ('counseling', 'Counseling'),
    ('security', 'Security'),
    ('energy_plant', 'Energy Plant'),
    ('commons', 'Student Commons/Common Area'),
    ('computer_lab', 'Computer Lab'),
    ('science_center', 'Science Center'),
    ('art_studio', 'Art Studio'),
    ('language_lab', 'Language Lab'),
    ('greenhouse', 'Greenhouse'),
    ('childcare', 'Childcare Center'),
    ('outdoor_classroom', 'Outdoor Classroom'),
    ('student_center', 'Student Center'),
    ('technology_hub', 'Technology Hub'),
    ('vocational_training', 'Vocational Training Center')
)
ELECTRICAL_EQUIPMENT_TYPES = (
    ('circuit_breaker', 'Circuit Breaker'),
    ('transformer', 'Transformer'),
    ('voltage_regulator', 'Voltage Regulator'),
    ('electric_meter', 'Electric Meter'),
    ('solar_panel', 'Solar Panel'),
    ('generator', 'Generator'),
    ('surge_protector', 'Surge Protector'),
    ('ups', 'UPS (Uninterruptible Power Supply)'),
    ('conduit_fittings', 'Conduit Fittings'),
    ('junction_box', 'Junction Box'),
    ('lighting_control', 'Lighting Control System'),
    ('battery_storage', 'Battery Storage'),
    ('inverter', 'Inverter'),
    ('power_distribution_unit', 'Power Distribution Unit'),
    ('energy_management_system', 'Energy Management System'),
    ('smart_meter', 'Smart Meter'),
    ('ev_charging_station', 'EV Charging Station'),
    ('security_camera', 'Security Camera'),
    ('network_switch', 'Network Switch'),
    ('fire_alarm_panel', 'Fire Alarm Panel')
)
MECHANICAL_EQUIPMENT_TYPES = (
    ('hvac_unit', 'HVAC Unit'),
    ('boiler', 'Boiler'),
    ('compressor', 'Compressor'),
    ('heat_exchanger', 'Heat Exchanger'),
    ('pump', 'Pump'),
    ('fan_coil_unit', 'Fan Coil Unit'),
    ('air_handling_unit', 'Air Handling Unit'),
    ('chiller', 'Chiller'),
    ('ductwork_components', 'Ductwork Components'),
    ('cooling_tower', 'Cooling Tower'),
    ('fire_suppression_system', 'Fire Suppression System'),
    ('gas_detection_system', 'Gas Detection System'),
    ('irrigation_system', 'Irrigation System'),
    ('exhaust_fan', 'Exhaust Fan'),
    ('vibration_isolator', 'Vibration Isolator'),
    ('filtration_system', 'Filtration System'),
    ('humidifier', 'Humidifier'),
    ('dehumidifier', 'Dehumidifier'),
    ('air_purifier', 'Air Purifier'),
    ('roof_top_unit', 'Rooftop Unit')
)
PLUMBING_EQUIPMENT_TYPES = (
    ('water_heater', 'Water Heater'),
    ('pump', 'Pump'),
    ('valve', 'Valve'),
    ('pipe_fittings', 'Pipe Fittings'),
    ('pressure_reducing_valve', 'Pressure Reducing Valve'),
    ('backflow_preventer', 'Backflow Preventer'),
    ('water_softener', 'Water Softener'),
    ('drainage_system', 'Drainage System'),
    ('faucet', 'Faucet'),
    ('toilet', 'Toilet'),
    ('irrigation_controller', 'Irrigation Controller'),
    ('sump_pump', 'Sump Pump'),
    ('greywater_system', 'Greywater System'),
    ('rainwater_harvesting_system', 'Rainwater Harvesting System'),
    ('sewage_pump', 'Sewage Pump'),
    ('water_recycling_system', 'Water Recycling System'),
    ('water_filtration', 'Water Filtration System'),
    ('sensor_faucet', 'Sensor Faucet'),
    ('emergency_shower', 'Emergency Shower'),
    ('eye_wash_station', 'Eye Wash Station')
)
MANUFACTURERS = (
    ('siemens', 'Siemens'),
    ('general_electric', 'General Electric'),
    ('honeywell', 'Honeywell'),
    ('trane', 'Trane'),
    ('carrier', 'Carrier'),
    ('bosch', 'Bosch'),
    ('abb', 'ABB'),
    ('schneider_electric', 'Schneider Electric'),
    ('mitsubishi_electric', 'Mitsubishi Electric'),
    ('johnson_controls', 'Johnson Controls'),
    ('daikin', 'Daikin'),
    ('emerson', 'Emerson'),
    ('hitachi', 'Hitachi'),
    ('toshiba', 'Toshiba'),
    ('rheem', 'Rheem'),
    ('kohler', 'Kohler'),
    ('moen', 'Moen'),
    ('delta', 'Delta'),
    ('grohe', 'Grohe'),
    ('american_standard', 'American Standard'),
    ('lennox', 'Lennox'),
    ('york', 'York'),
    ('goodman', 'Goodman'),
    ('lg', 'LG'),
    ('fujitsu', 'Fujitsu'),
    ('bryant', 'Bryant'),
    ('armstrong', 'Armstrong'),
    ('panasonic', 'Panasonic'),
    ('frigidaire', 'Frigidaire'),
    ('maytag', 'Maytag')
)


class School(models.Model):
    school_district = models.ForeignKey(SchoolDistrict, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    school_area_sqft = models.IntegerField() # dynamically calculated
    school_address = models.CharField(max_length=100) # geo coordinates are calculated form address.
    school_student_population = models.IntegerField(default=0)
    school_student_percent_disadvantaged = models.IntegerField(default=0) 
    school_student_percent_english_learners = models.IntegerField(default=0)

    def __str__(self):
        return str(self.school_name)
    

class UtilityProviderAccountNumber(models.Model):
    # per district, per utility. a district can have multiple account numbers. 1 account number per utility per district
    account_number = models.CharField(max_length = 100, primary_key=True)
    utility_provider = models.CharField(max_length=100, choices = UTILITY_PROVIDERS)
    utility_type = models.CharField(max_length = 100, choices = UTILITY_TYPE)
    account_district = models.ForeignKey(SchoolDistrict, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    

class ServiceAgreement(models.Model):
    # per school, per utility
    service_agreement_id = models.CharField(max_length = 100 , primary_key=True)
    utility_type = models.CharField(max_length = 100, choices = UTILITY_TYPE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    utility_provider_account_number = models.ForeignKey(UtilityProviderAccountNumber, on_delete=models.SET_NULL, null=True, blank=True, default=None, verbose_name="Associated Utility Provider Account Number")


class Building(models.Model):
    building_school = models.ForeignKey(School, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=100, default='building_name')
    building_type = models.CharField(max_length=100, choices=BUILDING_TYPES)
    building_area_sqft = models.IntegerField()
    building_geo_lat = models.FloatField(default=0.0)
    building_geo_long = models.FloatField(default=0.0)
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
    equipment_type = models.CharField(max_length=100, choices = ELECTRICAL_EQUIPMENT_TYPES + MECHANICAL_EQUIPMENT_TYPES + PLUMBING_EQUIPMENT_TYPES)
    equipment_manufacturer = models.CharField(max_length=100, choices = MANUFACTURERS)
    equipment_model = models.CharField(max_length=100, default='equipment_model')
    equipment_serial_number = models.CharField(max_length=100, default='equipment_serial_number')
    equipment_install_date = models.DateField()
    equipment_warranty_expiration = models.DateField(auto_now=False, auto_now_add=False)
    equipment_location = models.CharField(max_length=100, default='equipment_location')
    equipment_notes = equipment_notes = models.TextField(max_length=200, blank=True, default='equipment_notes')
    equipment_elec_kw_demand = models.IntegerField(default = 0)
    equipment_gas_btuh_demand = models.IntegerField(default = 0)
    equipment_generates_elec_kw = models.IntegerField(default = 0)
    equipment_storage_kwh = models.IntegerField(default = 0)
    equipment_storage_kbtu = models.IntegerField(default = 0)
    equipment_geo_lat = models.FloatField(default=0.0)
    equipment_geo_long = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.equipment_tag)
    
    def save(self, *args, **kwargs):
        if self.equipment_building and self.equipment_building.school != self.equipment_school:
            raise ValueError("The building is not part of the assigned school.")
        super().save(*args, **kwargs)


class PerformanceMetrics(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE) # school associated with the performance metrics
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


class Meter(models.Model):
    meter_id = models.IntegerField(primary_key=True)
    meter_type = models.CharField(max_length=100, choices = UTILITY_TYPE)
    meter_building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True)
    meter_school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)


class UtilityBill(models.Model):
    utility_type = models.CharField(max_length=100, choices = UTILITY_TYPE)
    bill_statement_date = models.DateField()
    bill_start_date = models.DateField()
    bill_end_date = models.DateField()
    total_usage_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    total_electric_charges = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    total_gas_charges = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    solar_energy_credits = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    # FOREIGN KEYS
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    district = models.ForeignKey(SchoolDistrict, on_delete=models.SET_NULL, null=True)
    account_number = models.ForeignKey(UtilityProviderAccountNumber, on_delete=models.SET_NULL, null=True)
    service_agreement_id = models.ForeignKey(ServiceAgreement, on_delete=models.SET_NULL, default=0)
    meter_id = models.ForeignKey(Meter, on_delete=models.SET_NULL, null=True, blank=True, default=None)


class MeterReading(models.Model):
    # per utility bill, per utility type
    elec_consumption_kwh = models.DecimalField(max_digits = 10, decimal_places = 2,  default=0.00)
    gas_consumption_therms = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    peak_demand_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    off_peak_demand_kwh = models.IntegerField(default=0)
    part_peak_demand_kwh = models.IntegerField(default=0)
    demand_charge_kw = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    solar_generation_kwh = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    # FOREIGN KEYS
    meter_id = models.ForeignKey(Meter, on_delete=models.CASCADE)
    utility_bill = models.ForeignKey(UtilityBill, on_delete=models.CASCADE)
