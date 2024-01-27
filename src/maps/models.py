from django.conf import settings
from django.db import models

class MapAnnotation(models.Model):
    """
    Represents an annotation on a map within a Django application for managing maps and annotations.
    This model handles various types of annotations that can be placed on maps, such as markers, lines, polygons, and labels, among others. It is designed to work with the Google Maps API for displaying and managing these annotations.
    Fields:
    - annotation_author: The user who created the annotation.
    - annotation_layer: The category of the annotation, chosen from predefined layers like HVAC, lighting, plumbing, etc.
    - annotation_description: An optional description of the annotation.
    - annotation_type: The type of the annotation, chosen from predefined types.
    - annotation_coordinates: The coordinates of the annotation stored in JSON format.
    The `__str__` method returns a string representation of the annotation, including the author, layer, description, type, and coordinates.
    """
    ANNOTATION_TYPES = (
        ('market', 'Marker'), 
        ('line', 'Line'), 
        ('polygon', 'Polygon'),
        ('mechanical', 'Mechanical'),
        ('electrical', 'Electrical'),
        ('plumbing', 'Plumbing'),
        ('meter', 'Meter'),
        ('label', 'Label'),
        ('sticky_note', 'Sticky Note')
    )
    ANNOTATION_LAYERS = (
        ('hvac', 'HVAC'),
        ('ahu', 'Air Handling Unit'),
        ('electrical_distribution', 'Electrical Distribution'),
        ('lighting', 'Lighting'),
        ('plumbing', 'Plumbing'),
        ('sanitary_system', 'Sanitary System'),
        ('water_supply', 'Water Supply'),
        ('fire_protection', 'Fire Protection'),
        ('security_system', 'Security System'),
        ('data_network', 'Data Network'),
        ('telecommunications', 'Telecommunications'),
        ('mechanical_ventilation', 'Mechanical Ventilation'),
        ('escalators_elevators', 'Escalators & Elevators'),
        ('renewable_energy', 'Renewable Energy'),
        ('existing_conditions', 'Existing Conditions'),
        ('proposed_development', 'Proposed Development'),
        ('demolition_plan', 'Demolition Plan'),
        ('construction_phase', 'Construction Phase'),
        ('future_expansion', 'Future Expansion'),
        ('landscaping', 'Landscaping'),
        ('site_utilities', 'Site Utilities'),
        ('parking_layout', 'Parking Layout'),
    )

    annotation_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # filled dynamically
    annotation_layer = models.CharField(max_length=100, choices=ANNOTATION_LAYERS)
    annotation_description = models.TextField(max_length = 100, null = True, blank = True, default = 'annotation_description')
    annotation_type = models.CharField(max_length=100, choices=ANNOTATION_TYPES)
    annotation_coordinates = models.JSONField() # filled dynamically

    def __str__(self):
        return str(self.annotation_author) + ' ' + str(self.annotation_layer) + ' ' + str(self.annotation_description)
