# from django.db import models

# # school_management/models.py
# from django.db import models
# from district_management.models import SchoolDistrict

# # district level staff can choose to create site staff, even though the site staff may not be registered with NZEO 
# class SiteStaff(models.Model):
#     staff_id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     job_title = models.CharField(max_length=20)
#     email = models.EmailField(verbose_name = "email", max_length = 60, unique=True)
#     phone = models.CharField(max_length=20)
#     district_id = models.ForeignKey(SchoolDistrict, on_delete=models.CASCADE)
#     school_id = models.ForeignKey('school_management.School', on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Staff ID: {self.staff_id}, Name: {self.first_name} {self.last_name}, Job Title: {self.job_title}, Email: {self.email}, Phone: {self.phone}, District: {self.district_id}, School: {self.school_id}"

# class School(models.Model):
#     school_id = models.AutoField(primary_key=True)
#     school_name = models.CharField(max_length=50)
#     school_district = models.CharField(max_length=50)
#     school_area_sqft = models.IntegerField()
#     school_geo_lat = models.FloatField()
#     school_geo_long = models.FloatField()
#     school_address = models.CharField(max_length=50)
#     school_phone = models.CharField(max_length=50)
#     school_email = models.CharField(max_length=50)
#     student_population = models.IntegerField()
#     student_percent_disenfrachised = models.IntegerField()    
#     district_id = models.ForeignKey(SchoolDistrict, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"School: {self.school_name}, District: {self.school_district}, Address: {self.school_address}, Phone: {self.school_phone}, Email: {self.school_email}, Student Population: {self.student_population}, Percent Disenfranchised: {self.student_percent_disenfrachised}"

# class Building(models.Model):
#     school_id = models.IntegerField()
#     building_id = models.IntegerField()
#     building_name = models.CharField(max_length=20, default="Building name")
#     building_type = models.CharField(max_length=20, default="Building type")
#     building_area_sqft = models.IntegerField()
#     building_geo_lat = models.FloatField()
#     building_geo_long = models.FloatField()
#     building_photo = models.ImageField(upload_to='images/', default='images/None/no-img.jpg')

#     def __str__(self):
#         return f"Building ID: {self.building_id}, Name: {self.building_name}, Type: {self.building_type}, Area: {self.building_area_sqft}, Address: {self.building_address}, Phone: {self.building_phone}, Email: {self.building_email}, Photo: {self.building_photo}"

# # school equipment represents, hvac, electrical, plumbing, etc.
# class Equipment(models.Model):
#     school_id = models.IntegerField()
#     equipment_id = models.IntegerField()
#     assigned_school = models.CharField(max_length=20, default="Equipment assigned school")
#     assigned_building = models.CharField(max_length=20, default="Equipment assigned building")
#     equipment_name = models.CharField(max_length=20, default="Equipment name")
#     equipment_type = models.CharField(max_length=20, default="Equipment type")
#     equipment_manufacturer = models.CharField(max_length=20, default="Equipment manufacturer")
#     equipment_model = models.CharField(max_length=20, default="Equipment model")
#     equipment_serial_number = models.CharField(max_length=20, default="Equipment serial number")
#     equipment_install_date = models.DateField(auto_now=False, auto_now_add=False)
#     equipment_warranty_expiration = models.DateField(auto_now=False, auto_now_add=False)
#     equipment_location = models.CharField(max_length=20, default="Equipment location")
#     equipment_notes = models.CharField(max_length=20, default="Equipment notes")
#     equipment_elec_kw_demand = models.IntegerField()
#     equipment_gas_btuh_demand = models.IntegerField()
#     equipment_generates_elec_kw = models.IntegerField()
#     equipment_storage_btu_kwh = models.IntegerField()
#     equipment_photo = models.ImageField(upload_to='images/', default='images/None/no-img.jpg')

#     def __str__(self):
#         return f"Equipment ID: {self.equipment_id}, School: {self.assigned_school}, District: {self.assigned_district}, Name: {self.equipment_name}, Type: {self.equipment_type}, Manufacturer: {self.equipment_manufacturer}, Model: {self.equipment_model}, Serial Number: {self.equipment_serial_number}, Install Date: {self.equipment_install_date}, Warranty Expiration: {self.equipment_warranty_expiration}, Location: {self.equipment_location}, Notes: {self.equipment_notes}, Photo: {self.equipment_photo}"


# class PerformanceMetrics(models.Model):
#     school_id = models.IntegerField()
#     emmissions_co2 = models.IntegerField()
#     CUI_co2_sqft = models.IntegerField()
#     EUI_kbtu_sqft = models.IntegerField()
#     EUI_kbtu_student = models.IntegerField()
#     renewables_kwh = models.IntegerField()
#     peak_demand_kw = models.IntegerField()
#     elec_consumption_kwh = models.IntegerField()
#     gas_consumption_mmbtu = models.IntegerField()
#     total_consumption_mmbtu = models.IntegerField()
#     ECI_dollar_sqft = models.IntegerField()
#     ECI_dollar_student = models.IntegerField()
#     total_cost_dollar = models.IntegerField()
#     year_to_date_kbtu_savings = models.IntegerField()
#     year_to_date_co2_savings = models.IntegerField()


