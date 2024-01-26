from django.conf import settings
from django.db import models

class MapAnnotation(models.Model):

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
    annotation_description = models.TextField(max_length = 100, null = True, blank = True)
    annotation_type = models.CharField(max_length=100, choices=ANNOTATION_TYPES)
    annotation_coordinates = models.JSONField() # filled dynamically
