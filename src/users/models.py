from django.contrib.auth.models import User
from django.db import models
from district_management.models import SchoolDistrict
from school_management.models import School



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_district = models.ForeignKey(SchoolDistrict, on_delete=models.SET_NULL, null=True, blank=False)
    user_school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True)
    job_title = models.CharField(max_length=100, blank=True)

    def get_assigned_district(self):
        return self.assigned_district
