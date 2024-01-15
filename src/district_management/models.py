from django.db import models

class District_Admin(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, default="District Admin")
    first_name = models.CharField(max_length=20, default="District Admin first name")
    last_name = models.CharField(max_length=20, default="District Admin last name")
    # email = models.EmailField(max_length=50, default="District Admin email")
    phone = models.CharField(max_length=20, default="District Admin phone number")
    assigned_district = models.CharField(max_length=20, default="District Admin district")

    def __str__(self):
        return f"District Admin: {self.first_name} {self.last_name}, Title: {self.title}, Email: {self.email}, Phone: {self.phone}, District: {self.district}"
    
