from django.contrib import admin
from .models import School, Building, Equipment, PerformanceMetrics

admin.site.register(School)
admin.site.register(Building)
admin.site.register(Equipment)
admin.site.register(PerformanceMetrics)


