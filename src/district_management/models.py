from django.db import models

class SchoolDistrict(models.Model):
    """
    Represents a school district within a Django application for district management.
    This model stores essential information about each school district, including 
    its name, city, geographical coordinates, and bounding box coordinates. 
    These details are crucial for district administrators to view and manage 
    data about the schools in their district and annotate maps using Google Maps integration.
    Fields:
    - district_name (CharField): The name of the school district.
    - district_city (CharField): The city where the school district is located.
    - district_geo_lat (FloatField): The latitude of the geographical center of the district.
    - district_geo_long (FloatField): The longitude of the geographical center of the district.
    - district_bb_southwest_lat (FloatField): The latitude of the southwest corner of the district's bounding box.
    - district_bb_southwest_lng (FloatField): The longitude of the southwest corner of the district's bounding box.
    - district_bb_northeast_lat (FloatField): The latitude of the northeast corner of the district's bounding box.
    - district_bb_northeast_lng (FloatField): The longitude of the northeast corner of the district's bounding box.
    The `save` method overrides the default to ensure `district_name` and `district_city` 
    are stored in lowercase for consistency. The model includes a unique constraint 
    on the combination of `district_name` and `district_city` to prevent duplicate entries.
    """
    district_name = models.CharField(max_length=100)
    district_city = models.CharField(max_length=100)
    district_geo_lat = models.FloatField()
    district_geo_long = models.FloatField()
    district_bb_southwest_lat = models.FloatField()
    district_bb_southwest_lng = models.FloatField()
    district_bb_northeast_lat = models.FloatField()
    district_bb_northeast_lng = models.FloatField()

    def save(self, *args, **kwargs):
        self.district_name = self.district_name.lower()
        self.district_city = self.district_city.lower()
        super(SchoolDistrict, self).save(*args, **kwargs)

    class Meta:
        unique_together = (('district_name', 'district_city'),)

    def __str__(self):
        return str(self.district_name) + ' ' + str(self.district_city) + ' ' + str(self.district_geo_lat) + ' ' + str(self.district_geo_long) + ' ' + str(self.district_bb_southwest_lat) + ' ' + str(self.district_bb_southwest_lng) + ' ' + str(self.district_bb_northeast_lat) + ' ' + str(self.district_bb_northeast_lng)
