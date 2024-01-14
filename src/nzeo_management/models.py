from django.db import models
from django.contrib.auth.models import User

# create model for NZEO Admin
class NZEO_Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, default="NZEO team member")
    first_name = models.CharField(max_length=20, default="NZEO staff first name")
    last_name = models.CharField(max_length=20, default="NZEO staff last name")
    email = models.EmailField(max_length=50, default="NZEO staff email")
    phone = models.CharField(max_length=20, default="NZEO staff phone number")

    def __str__(self):
        return f"NZEO Admin: {self.first_name} {self.last_name}, Title: {self.title}, Email: {self.email}, Phone: {self.phone}"
    
# create model for District Admin
class District_Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, default="District Admin")
    first_name = models.CharField(max_length=20, default="District Admin first name")
    last_name = models.CharField(max_length=20, default="District Admin last name")
    email = models.EmailField(max_length=50, default="District Admin email")
    phone = models.CharField(max_length=20, default="District Admin phone number")
    district = models.CharField(max_length=20, default="District Admin district")

    def __str__(self):
        return f"District Admin: {self.first_name} {self.last_name}, Title: {self.title}, Email: {self.email}, Phone: {self.phone}, District: {self.district}"

class Site_Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, default="Site Staff")
    first_name = models.CharField(max_length=20, default="Site Staff first name")
    last_name = models.CharField(max_length=20, default="Site Staff last name")
    email = models.EmailField(max_length=50, default="Site Staff email")
    phone = models.CharField(max_length=20, default="Site Staff phone number")
    district = models.CharField(max_length=20, default="Site Staff district")
    site = models.CharField(max_length=20, default="Site Staff site")

    def __str__(self):
        return f"Site Staff: {self.first_name} {self.last_name}, Title: {self.title}, Email: {self.email}, Phone: {self.phone}, District: {self.district}, Site: {self.site}"