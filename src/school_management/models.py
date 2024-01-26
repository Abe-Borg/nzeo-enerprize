from django.db import models
from district_management.models import SchoolDistrict


class School(models.Model):
    school_district = models.ForeignKey(SchoolDistrict, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    school_area_sqft = models.IntegerField()
    # school_geo_lat = models.FloatField() this will be dynamicall calculated
    # school_geo_long = models.FloatField()
    school_address = models.CharField(max_length=100) # geo coordinates are calculated form address.
    school_student_population = models.IntegerField()
    school_student_percent_disenfrachised = models.IntegerField()    




class Building(models.Model):
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
    )

    building_school = models.ForeignKey(School, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=100)
    building_type = models.CharField(max_length=100, choices=BUILDING_TYPES)
    building_area_sqft = models.IntegerField()
    building_geo_lat = models.FloatField()
    building_geo_long = models.FloatField()
    building_photo = models.ImageField(upload_to='images/', default='images/None/no-img.jpg')


# # school equipment represents, hvac, electrical, plumbing, etc.
class Equipment(models.Model):
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
    )

    equipment_school = models.ForeignKey(School, on_delete=models.CASCADE)
    equipment_building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True)
    equipment_tag = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=100, choices = ELECTRICAL_EQUIPMENT_TYPES + MECHANICAL_EQUIPMENT_TYPES + PLUMBING_EQUIPMENT_TYPES)
    equipment_manufacturer = models.CharField(max_length=100, choices = MANUFACTURERS)
    equipment_model = models.CharField(max_length=100)
    equipment_serial_number = models.CharField(max_length=100)
    equipment_install_date = models.DateField()
    equipment_warranty_expiration = models.DateField(auto_now=False, auto_now_add=False)
    equipment_location = models.CharField(max_length=100)
    equipment_notes = equipment_notes = models.TextField(max_length=200, blank=True)
    equipment_elec_kw_demand = models.IntegerField()
    equipment_gas_btuh_demand = models.IntegerField()
    equipment_generates_elec_kw = models.IntegerField()
    equipment_storage_btu_kwh = models.IntegerField()
    equipment_photo = models.ImageField(upload_to='images/', default='images/None/no-img.jpg')


class PerformanceMetrics(models.Model):
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


