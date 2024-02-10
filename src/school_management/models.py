from django.db import models
from district_management.models import SchoolDistrict


class School(models.Model):
    """
    Represents a school within the school management application.
    This model stores comprehensive information about a school, including its association with a school district, physical attributes, demographic data, and geo-location (dynamically calculated from the address). This information is foundational for various analyses and data visualization related to school performance and resource management.
    Fields:
    - school_district: The associated school district (ForeignKey).
    - school_name: The name of the school.
    - school_area_sqft: The total area of the school in square feet.
    - school_address: The physical address of the school.
    - school_student_population: The total number of students.
    - school_student_percent_disenfrachised: The percentage of disenfranchised students.
    The `__str__` method returns a string representation of the school, including key attributes.
    """
    school_district = models.ForeignKey(SchoolDistrict, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    school_area_sqft = models.IntegerField() # dynamically calculated
    school_address = models.CharField(max_length=100) # geo coordinates are calculated form address.
    school_student_population = models.IntegerField(default=0)
    school_student_percent_disadvantaged = models.IntegerField(default=0)
    school_student_percent_english_learners = models.IntegerField(default=0)

    def __str__(self):
        return str(self.school_name)
    

class Building(models.Model):
    """
    Represents a building within a school, as part of the school management application.
    This model captures detailed information about each building in a school, such as its name, type, size, geographical location, and a photo for visual reference. The variety of building types, from classrooms to energy plants, allows for comprehensive tracking and management of school facilities.
    Fields:
    - building_school: The school to which the building belongs (ForeignKey).
    - building_name: The name of the building.
    - building_type: The type/category of the building, chosen from a predefined set of options.
    - building_area_sqft: The total area of the building in square feet.
    - building_geo_lat: The latitude coordinate of the building's geographical location.
    - building_geo_long: The longitude coordinate of the building's geographical location.
    - building_photo: An image of the building, stored in the specified path.
    The `__str__` method returns a string representation of the building, including its association with a school, name, type, area, and geographical coordinates.
    """
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

    building_school = models.ForeignKey(School, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=100, default='building_name')
    building_type = models.CharField(max_length=100, choices=BUILDING_TYPES)
    building_area_sqft = models.IntegerField()
    building_geo_lat = models.FloatField(default=0.0)
    building_geo_long = models.FloatField(default=0.0)
    building_age = models.IntegerField(default=0)

    def __str__(self):
        # return everything
        return 'School: '+ str(self.building_school) + ' ' + 'Building Name: ' + str(self.building_name)
    

class Equipment(models.Model):
    """
    Represents equipment within a school's facilities, as part of the school management application.
    This model is designed to store and manage detailed information about various types of equipment used in school facilities, such as electrical, mechanical, and plumbing equipment. It includes comprehensive details like the type of equipment, manufacturer, model, serial number, installation date, warranty expiration, and specific attributes related to energy consumption and generation.
    Fields:
    - equipment_school: The school where the equipment is located (ForeignKey).
    - equipment_building: The specific building within the school where the equipment is housed (ForeignKey, nullable).
    - equipment_tag: A unique identifier or tag for the equipment.
    - equipment_type: The type of equipment, chosen from a predefined set of electrical, mechanical, and plumbing equipment types.
    - equipment_manufacturer: The manufacturer of the equipment, chosen from a predefined set of manufacturers.
    - equipment_model: The model of the equipment.
    - equipment_serial_number: The serial number of the equipment.
    - equipment_install_date: The date when the equipment was installed.
    - equipment_warranty_expiration: The expiration date of the equipment's warranty.
    - equipment_location: The specific location of the equipment within the building.
    - equipment_notes: Additional notes or comments about the equipment.
    - equipment_elec_kw_demand: The electrical demand of the equipment in kilowatts.
    - equipment_gas_btuh_demand: The gas demand of the equipment in British Thermal Units per hour.
    - equipment_generates_elec_kw: The electrical generation capacity of the equipment in kilowatts, if applicable.
    - equipment_storage_btu_kwh: The energy storage capacity of the equipment in British Thermal Units or kilowatt-hours.
    - equipment_photo: An image of the equipment, stored in the specified path.
    The `__str__` method returns a string representation of the equipment, including its association with a school, building, tag, type, manufacturer, model, and serial number.
    """
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
    """
    Represents various performance metrics related to energy usage and sustainability for a school, as part of the school management application.
    This model is crucial for tracking and analyzing the school's environmental impact and energy efficiency. It encompasses a wide range of metrics including CO2 emissions, energy use intensity (EUI), cost of energy intensity (ECI), renewable energy usage, and more. These metrics are essential for assessing the school's performance in terms of energy consumption, cost, and environmental sustainability.
    Fields:
    - school: The school to which these performance metrics are related (ForeignKey).
    - emmissions_co2: The amount of CO2 emissions in a specified unit.
    - CUI_co2_sqft: Carbon Usage Intensity per square foot.
    - EUI_kbtu_sqft: Energy Use Intensity in kBTU per square foot.
    - EUI_kbtu_student: Energy Use Intensity in kBTU per student.
    - renewables_kwh: Renewable energy usage in kilowatt-hours.
    - peak_demand_kw: Peak electrical demand in kilowatts.
    - elec_consumption_kwh: Total electrical consumption in kilowatt-hours.
    - gas_consumption_mmbtu: Total gas consumption in million British Thermal Units (MMBTU).
    - total_consumption_mmbtu: Total energy consumption in MMBTU.
    - ECI_dollar_sqft: Energy Cost Intensity per square foot.
    - ECI_dollar_student: Energy Cost Intensity per student.
    - total_cost_dollar: Total energy cost in dollars.
    - year_to_date_kbtu_savings: Year-to-date savings in kBTU.
    - year_to_date_co2_savings: Year-to-date CO2 savings.
    The `__str__` method returns a string representation of the performance metrics, encompassing key data points for easy identification and analysis.
    """
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    emmissions_co2 = models.IntegerField()
    CUI_co2_sqft = models.IntegerField()
    EUI_kbtu_sqft = models.IntegerField()
    EUI_kbtu_student = models.IntegerField()
    renewables_kwh = models.IntegerField()
    peak_demand_kw = models.IntegerField()
    elec_consumption_kwh = models.IntegerField()
    gas_consumption_mmbtu = models.IntegerField()
    total_consumption_mmbtu = models.IntegerField()
    ECI_dollar_sqft = models.IntegerField()
    ECI_dollar_student = models.IntegerField()
    total_cost_dollar = models.IntegerField()
    year_to_date_kbtu_savings = models.IntegerField()
    year_to_date_co2_savings = models.IntegerField()

    def __str__(self):
        return str(self.school) + ' ' + str(self.emmissions_co2) + ' ' + str(self.CUI_co2_sqft) + ' ' + str(self.EUI_kbtu_sqft) + ' ' + str(self.EUI_kbtu_student) + ' ' + str(self.renewables_kwh) + ' ' + str(self.peak_demand_kw) + ' ' + str(self.elec_consumption_kwh) + ' ' + str(self.gas_consumption_mmbtu) + ' ' + str(self.total_consumption_mmbtu) + ' ' + str(self.ECI_dollar_sqft) + ' ' + str(self.ECI_dollar_student) + ' ' + str(self.total_cost_dollar) + ' ' + str(self.year_to_date_kbtu_savings) + ' ' + str(self.year_to_date_co2_savings)


class Meter(models.Model):
    """ 
    a model that stores the data returned from the UtilityAPI call.
    """
    METER_TYPE = (
        ('natural_gas', 'Natural Gas'),
        ('electric', 'Electric'),
        ('water', 'Water'),
        ('steam', 'Steam'),
        ('chilled_water', 'Chilled Water'),
        ('hot_water', 'Hot Water'),
        ('fuel_oil', 'Fuel Oil'),
        ('other', 'Other'),
    )
    UTILITY_PROVIDERS = (
        ('pg_e', 'PG&E'),
    )
    INTERVAL_TIME_ZONES = (
        ('us_pacific', 'US/Pacific'),
    )
    UNITS_OF_MEASURE = (
        ('kwh', 'Kilowatt hours (e.g. usage)'),
        ('kw', 'Kilowatts (e.g. demand)'),
        ('kva', 'Kilovolt-amperes (e.g. apparent power)'),
        ('kvah', 'Kilovolt-amperes-hour (e.g. apparent energy)'),
        ('kvar', 'Kilovolt-amperes-reactive (e.g. reactive power)'),
        ('kvarh', 'Kilovolt-amperes-reactive-hour (e.g. reactive energy)'),
        ('therms', 'Therms (e.g. natural gas energy)'),
        ('ccf', 'ccf, Hundreds of cubic feet (e.g. natural gas volume)'),
        ('mcf', 'mcf, Thousands of cubic feet (e.g. natural gas volume)'),
        ('hcf', 'hcf, Water volume in hundreds of cubic feet'),
        ('gallons', 'Gallons (e.g. water volume)'),
        ('m3', 'Cubic meters (e.g. water volume)'),
        ('days', 'Days'),
        ('months', 'Months'),
        ('percent', 'Percent'),
        ('poles', 'Number of lamp poles (used in certain Outdoor Lighting Tariffs)'),
        ('lamps', 'Number of lamps (used in certain Outdoor Lighting Tariffs)'),
        ('metering_devices', 'Number of metering devices (e.g. electric meters)'),
        ('currency', 'Currency, USD'),
    )
    SOURCE_TYPES = (
        ('pdf', 'PDF usually containing one or more utility bills or intervals'),
        ('pdf_other', 'A PDF document other than a utility bill, for example a monthly summary'),
        ('raw_pdf', 'A un-parsed PDF document from the utility website'),
        ('website', 'The HTML of a page on the utility website.'),
        ('greenbutton_dmd', 'Green Button DOWNLOAD My Data xml files.'),
        ('greenbutton_cmd', 'Green Button CONNECT My Data xml files.'),
        ('greenbutton_other', 'Another form of Green Button xml files.'),
        ('spreadsheet', 'A spreadsheet download or report.'),
        ('edi', 'EDI format files'),
        ('other', 'another format not listed here.'),
    )
    SOURCE = (
        ('type', 'SOURCE_TYPES'),
        ('raw_url', 'The URL of the source data.'),
        ('...', 'additional attributes (for some SOURCE_TYPES)')
    )
    SUPPLIER_TYPE = (
        ('cca', 'Energy is supplied by a Community Choice Aggregator (CCA)'),
        ('direct_access', 'Energy is purchased directly from an ESP'),
        ('third_party', 'Energy is provided by some other third party supplier')
    )

    meter_uid = models.IntegerField(primary_key=True)
    meter_utility_provider = models.CharField(max_length=100, choices = UTILITY_PROVIDERS)
    meter_utility_service_id = models.IntegerField()
    meter_utility_billing_account = models.IntegerField()
    meter_utility_service_address = models.CharField(max_length=100)
    meter_utility_meter_number = models.IntegerField() # not sure if this is a duplicate of meter_uid
    meter_utility_tariff_name = models.CharField(max_length=100)
    meter_interval_start = models.DateTimeField()
    meter_interval_end = models.DateTimeField()
    meter_interval_kwh_usage = models.FloatField(default=0.0)
    meter_fwd_kwh_usage = models.FloatField(default=0.0)
    meter_net_kwh_usage = models.FloatField(default=0.0)
    meter_rev_kwh_usage = models.FloatField(default=0.0)
    meter_source = models.CharField(max_length=100) # unclear what this is. might be source of data, (e.g. UtilityAPI, manual entry, PDFs, etc.)
    meter_updated = models.DateTimeField()
    meter_interval_timezone = models.CharField(max_length=100, choices = INTERVAL_TIME_ZONES, default = 'us_pacific')
    meter_type = models.CharField(max_length=100, choices = METER_TYPE, default = 'meter_type')
    meter_building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Associated Building")


class UtilityBill(models.Model):
    """
    Represents utility bills for a school, as part of the school management application.
    This model is designed to store and manage detailed information about utility bills, including the billing period, total cost, and consumption of electricity, gas, water, and other utilities. It is essential for tracking and analyzing the school's utility expenses and consumption patterns over time, which is crucial for budgeting, cost management, and sustainability efforts.
    Fields:
    - school: The school to which the utility bills are related (ForeignKey).
    - meter_uid: The unique identifier of the meter associated with the utility bill (ForeignKey).
    - bill_start_date: The start date of the billing period.
    - bill_end_date: The end date of the billing period.
    - bill_total_cost: The total cost of the utility bill in dollars.
    - bill_elec_consumption_kwh: The total electrical consumption in kilowatt-hours.
    - bill_gas_consumption_mmbtu: The total gas consumption in million British Thermal Units (MMBTU).
    - bill_water_consumption_gallons: The total water consumption in gallons.
    - bill_other_consumption: The total consumption of other utilities.
    """
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    meter_uid = models.ForeignKey(Meter, on_delete=models.CASCADE)
    bill_start_date = models.DateField()
    bill_end_date = models.DateField()
    bill_total_cost = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    bill_elec_consumption_kwh = models.DecimalField(max_digits = 10, decimal_places = 2,  default=0.00)
    bill_gas_consumption_mmbtu = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    bill_water_consumption_gallons = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.00)
    
    def __str__(self):
        return str(self.school) + ' ' + str(self.bill_elec_consumption_kwh) + ' ' + str(self.bill_gas_consumption_mmbtu) + ' ' + str(self.bill_water_consumption_gallons) + ' ' + str(self.bill_total_cost)
