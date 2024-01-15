from django.db import models

# Create your models here.
class Site_Staff(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, default="Site Staff")
    first_name = models.CharField(max_length=20, default="Site Staff first name")
    last_name = models.CharField(max_length=20, default="Site Staff last name")
    # email = models.EmailField(max_length=50, default="Site Staff email")
    phone = models.CharField(max_length=20, default="Site Staff phone number")
    assigned_district = models.CharField(max_length=20, default="Site Staff district")
    assigned_site = models.CharField(max_length=20, default="Site Staff site")

    def __str__(self):
        return f"Site Staff: {self.first_name} {self.last_name}, Title: {self.title}, Email: {self.email}, Phone: {self.phone}, District: {self.district}, Site: {self.site}"



#define a model for a school's information
class School(models.Model):
    school_name = models.CharField(max_length=50)
    school_district = models.CharField(max_length=50)
    school_address = models.CharField(max_length=50)
    school_phone = models.CharField(max_length=50)
    school_email = models.CharField(max_length=50)
    student_population = models.IntegerField()

    def __str__(self):
        return f"School: {self.school_name}, District: {self.school_district}, Address: {self.school_address}, Phone: {self.school_phone}, Email: {self.school_email}, Student Population: {self.student_population}"

