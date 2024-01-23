from django.db import models

class MapAnnotation(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    layer = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    ANNOTATION_TYPES = [('market', 'Marker'), ('line', 'Line'), ('polygon', 'Polygon')]
    annotation_type = models.CharField(max_length=255, choices=ANNOTATION_TYPES)
    # x = models.FloatField()
    # y = models.FloatField()
    # z = models.FloatField()
    coordinates = models.JSONField()
    metadata = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)