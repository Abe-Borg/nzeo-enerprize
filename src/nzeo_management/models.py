from django.db import models
from django.contrib.auth.models import User


class NZEO_Admin(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, default="NZEO team member")
    first_name = models.CharField(max_length=20, default="NZEO staff first name")
    last_name = models.CharField(max_length=20, default="NZEO staff last name")
    # email = models.EmailField(max_length=50, default="NZEO staff email")
    phone = models.CharField(max_length=20, default="NZEO staff phone number")

    def __str__(self):
        return f"NZEO Admin: {self.first_name} {self.last_name}, Title: {self.title}, Email: {self.email}, Phone: {self.phone}"
    

