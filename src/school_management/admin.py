from django.contrib import admin
from .models import School, Building, Equipment, PerformanceMetrics, Meter

admin.site.register(School)

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('get_school_name', 'building_type', 'building_area_sqft')
    def get_school_name(self, obj):
        return obj.building_school.school_name
    get_school_name.short_description = 'School Name'
    
    list_filter = ('building_school', 'building_type', 'building_area_sqft')
    ordering = ('building_school', 'building_type', 'building_area_sqft')  # Sort by school and then by name

admin.site.register(Equipment)
admin.site.register(PerformanceMetrics)
admin.site.register(Meter)


