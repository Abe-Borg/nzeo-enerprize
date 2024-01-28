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

class ElecKwDemandFilter(admin.SimpleListFilter):
    title = _('Electrical KW Demand')
    parameter_name = 'elec_kw_demand'

    def lookups(self, request, model_admin):
        return (
            ('500-999', _('500 - 999 KW')),
            ('1000-1499', _('1000 - 1499 KW')),
            ('1500-1999', _('1500 - 1999 KW')),
            ('2000-2499', _('2000 - 2499 KW')),
            ('2500-2999', _('2500 - 2999 KW')),
            ('3000-3499', _('3000 - 3499 KW')),
            ('3500-4000', _('3500 - 4000 KW')),
        )

    def queryset(self, request, queryset):
        if self.value():
            low, high = [int(x) for x in self.value().split('-')]
            return queryset.filter(equipment_elec_kw_demand__gte=low, equipment_elec_kw_demand__lte=high)
        return queryset

class GasBtuhDemandFilter(admin.SimpleListFilter):
    title = _('Gas BTUH Demand')
    parameter_name = 'gas_btuh_demand'

    def lookups(self, request, model_admin):
        return (
            ('30000-34999', _('30000 - 34999 BTUH')),
            ('35000-39999', _('35000 - 39999 BTUH')),
            ('40000-44999', _('40000 - 44999 BTUH')),
            ('45000-49999', _('45000 - 49999 BTUH')),
            ('50000-54999', _('50000 - 54999 BTUH')),
            ('55000-59999', _('55000 - 59999 BTUH')),
            ('60000-64999', _('60000 - 64999 BTUH')),
            ('65000-70000', _('65000 - 70000 BTUH')),
        )

    def queryset(self, request, queryset):
        if self.value():
            low, high = [int(x) for x in self.value().split('-')]
            return queryset.filter(gas_btuh_demand__gte=low, gas_btuh_demand__lte=high)
        return queryset

class GeneratesElecKwFilter(admin.SimpleListFilter):
    title = _('Generates Electric KW')
    parameter_name = 'generates_elec_kw'

    def lookups(self, request, model_admin):
        return (
            ('50-99', _('50 - 99 KW')),
            ('100-149', _('100 - 149 KW')),
            ('150-199', _('150 - 199 KW')),
            ('200-249', _('200 - 249 KW')),
            ('250', _('250 KW')),
        )

    def queryset(self, request, queryset):
        if self.value():
            if '-' in self.value():
                low, high = [int(x) for x in self.value().split('-')]
                return queryset.filter(generates_elec_kw__gte=low, generates_elec_kw__lte=high)
            elif self.value() == '250':  # Handle the single value case
                return queryset.filter(generates_elec_kw=250)
        return queryset

class StorageBtuKwhFilter(admin.SimpleListFilter):
    title = _('Storage BTU/KWh')
    parameter_name = 'storage_btu_kwh'

    def lookups(self, request, model_admin):
        ranges = [(i, f"{i} - {i+4999} BTU/KWh") for i in range(50000, 100000, 5000)]
        return ranges

    def queryset(self, request, queryset):
        if self.value():
            low = int(self.value())
            high = low + 4999
            return queryset.filter(storage_btu_kwh__gte=low, storage_btu_kwh__lte=high)
        return queryset

class InstallDateRangeFilter(admin.SimpleListFilter):
    title = _('Installation Date')
    parameter_name = 'install_date_range'

    def lookups(self, request, model_admin):
        # Creating date ranges from 1950 to 2010 in increments of 10 years
        date_ranges = [(f"{start_year}-{start_year + 9}", f"{start_year} - {start_year + 9}")
                       for start_year in range(1950, 2011, 10)]
        return date_ranges

    def queryset(self, request, queryset):
        if self.value():
            start_year, end_year = [int(year) for year in self.value().split('-')]
            return queryset.filter(equipment_install_date__year__gte=start_year,
                                   equipment_install_date__year__lte=end_year)
        return queryset

class WarrantyExpirationDateRangeFilter(admin.SimpleListFilter):
    title = _('Warranty Expiration Date')
    parameter_name = 'warranty_expiration_range'

    def lookups(self, request, model_admin):
        # Creating date ranges from 1960 to 2020 in increments of 10 years
        date_ranges = [(f"{start_year}-{start_year + 9}", f"{start_year} - {start_year + 9}")
                       for start_year in range(1960, 2021, 10)]
        return date_ranges

    def queryset(self, request, queryset):
        if self.value():
            start_year, end_year = [int(year) for year in self.value().split('-')]
            return queryset.filter(equipment_warranty_expiration__year__gte=start_year,
                                   equipment_warranty_expiration__year__lte=end_year)
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
        if obj.equipment_building:
            return obj.equipment_building.building_name
        return "No Building"
    
    get_building_name.short_description = 'Building Name'
    
    list_filter = ('equipment_school', 'equipment_building', 'equipment_type', 'equipment_manufacturer', InstallDateRangeFilter, WarrantyExpirationDateRangeFilter, ElecKwDemandFilter, GasBtuhDemandFilter, GeneratesElecKwFilter, StorageBtuKwhFilter)
    ordering = ('equipment_model', 'equipment_type', 'equipment_manufacturer', 'equipment_install_date', 'equipment_warranty_expiration', 'equipment_elec_kw_demand', 'equipment_gas_btuh_demand', 'equipment_generates_elec_kw', 'equipment_storage_btu_kwh')


admin.site.register(PerformanceMetrics)
admin.site.register(Meter)


