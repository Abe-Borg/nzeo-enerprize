from django.db import models

class SchoolDistrict(models.Model):
    district_name = models.CharField(max_length=100)
    district_city = models.CharField(max_length=100)
    district_geo_lat = models.FloatField()
    district_geo_long = models.FloatField()
    district_bb_southwest_lat = models.FloatField()
    district_bb_southwest_lng = models.FloatField()
    district_bb_northeast_lat = models.FloatField()
    district_bb_northeast_lng = models.FloatField()

    def save(serlf, *args, **kwargs):
        self.district_name = self.district_name.lower()
        self.district_city = self.district_city.lower()
        super(SchoolDistrict, self).save(*args, **kwargs)

    class Meta:
        unique_together = (('district_name', 'district_city'),)
