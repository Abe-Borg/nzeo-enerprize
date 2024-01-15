from django.db import models

class Annotation(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    layer = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    x = models.FloatField()
    y = models.FloatField()
    # z = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)