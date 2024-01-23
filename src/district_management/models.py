from django.db import models

class SchoolDistrict(models.Model):
    district_id = models.IntegerField()
    district_name = models.CharField(max_length=100, default="District")
    district_num_schools = models.IntegerField()
    district_geo_lat = models.FloatField()
    district_geo_long = models.FloatField()
    district_bb_bottom_left_lat = models.FloatField() # bottom left corner of bounding box, southwest corner lat, 
    district_bb_bottom_left_lng = models.FloatField() # southwest corner lng
    district_bb_top_right_lat = models.FloatField() # top right corner of bounding box, northeast corner lat
    district_bb_top_right_lng = models.FloatField() # northeast corner lng



    def __str__(self):
        return f"District: {self.district_name}, Number of Schools: {self.district_num_schools}" 