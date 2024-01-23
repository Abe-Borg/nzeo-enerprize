from django.db import models

class SchoolDistrict(models.Model):
    district_id = models.IntegerField()
    district_name = models.CharField(max_length=100, default="District")
    district_num_schools = models.IntegerField()
    district_geo_lat = models.FloatField()
    district_geo_long = models.FloatField()
    district_bounding_box_bottom_left = models.FloatField()
    district_bounding_box_top_right = models.FloatField()



    def __str__(self):
        return f"District: {self.district_name}, Number of Schools: {self.district_num_schools}" 