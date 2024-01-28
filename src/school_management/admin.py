from django.contrib import admin
from .models import School, Building, Equipment, PerformanceMetrics, Meter
from django.utils.translation import gettext_lazy as _


admin.site.register(School)

class AreaRangeFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the right admin sidebar just above the filter options.
    title = _('building area (sqft)')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'area'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each tuple is the coded value for the option that will
        appear in the URL query. The second element is the human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('500-1000', _('500 - 1000 sqft')),
            ('1001-1500', _('1001 - 1500 sqft')),
            ('1501-2000', _('1501 - 2000 sqft')),
            ('2001-2500', _('2001 - 2500 sqft')),
            ('2501-3000', _('2501 - 3000 sqft')),
            ('3001-3500', _('3001 - 3500 sqft')),
            ('3501-4000', _('3501 - 4000 sqft')),
            ('4001-4500', _('4001 - 4500 sqft')),
            ('4501-5000', _('4501 - 5000 sqft')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value():
            if '-' in self.value():
                low, high = self.value().split('-')
                return queryset.filter(building_area_sqft__gte=int(low), building_area_sqft__lte=int(high))
        return queryset


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('get_school_name', 'building_type', 'building_area_sqft')

    def get_school_name(self, obj):
        return obj.building_school.school_name

    get_school_name.short_description = 'School Name'
    
    list_filter = ('building_school', 'building_type', AreaRangeFilter)
    ordering = ('building_type', 'building_area_sqft')  # Sort by school and then by name

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('get_school_name', 'get_building_name', 'equipment_model', 'equipment_type', 'equipment_manufacturer','equipment_install_date')
    def get_school_name(self, obj):
        return obj.equipment_school.school_name
    get_school_name.short_description = 'School Name'

    def get_building_name(self, obj):
        return obj.equipment_building.building_name
    get_building_name.short_description = 'Building Name'
    
    list_filter = ('equipment_school', 'equipment_building', 'equipment_type', 'equipment_manufacturer', 'equipment_install_date', 'equipment_warranty_expiration', 'equipment_elec_kw_demand', 'equipment_gas_btuh_demand', 'equipment_generates_elec_kw', 'equipment_storage_btu_kwh')
    ordering = ('building_type', 'building_area_sqft')

admin.site.register(PerformanceMetrics)
admin.site.register(Meter)


