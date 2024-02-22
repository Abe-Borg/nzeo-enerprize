from django.contrib import admin
from django.db.models import Sum
from district_management.models import SchoolDistrict
from .models import School, Building, Equipment, PerformanceMetrics, Meter, MeterReading, UtilityBill, UtilityProviderAccountNumber, ServiceAgreement
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.db.models import F

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

class StorageKBtuFilter(admin.SimpleListFilter):
    title = _('Storage kBTU')
    parameter_name = 'storage_kbtu'

    def lookups(self, request, model_admin):
        ranges = [(i, f"{i} - {i+4999} kBTU") for i in range(50000, 100000, 5000)]
        return ranges

    def queryset(self, request, queryset):
        if self.value():
            low = int(self.value())
            high = low + 4999
            return queryset.filter(storage_kbtu__gte=low, storage_kbtu__lte=high)
        return queryset

class StorageKWhFilter(admin.SimpleListFilter):
    title = _('Storage kWh')
    parameter_name = 'storage_kwh'

    def lookups(self, request, model_admin):
        ranges = [(i, f"{i} - {i+4999} kWh") for i in range(50000, 100000, 5000)]
        return ranges

    def queryset(self, request, queryset):
        if self.value():
            low = int(self.value())
            high = low + 4999
            return queryset.filter(storage_kwh__gte=low, storage_kwh__lte=high)
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
    
class BuildingAgeRangeFilter(admin.SimpleListFilter):
    title = _('Building Age')
    parameter_name = 'building_age_range'

    def lookups(self, request, model_admin):
        # Generate ranges in the format ('0-9', '0 - 9 years'), ('10-19', '10 - 19 years') etc.
        date_ranges = [(f"{start_year}-{start_year + 10}", f"{start_year} - {start_year + 10} years")
                       for start_year in range(0, 100, 10)]  # Adjusted for ranges starting from 0
        return date_ranges

    def queryset(self, request, queryset):
        if self.value():
            start_year, end_year = [int(year) for year in self.value().split('-')]
            # Filter the queryset based on the building age range
            return queryset.filter(building_age__gte=start_year,
                                   building_age__lte=end_year)
        return queryset

class DistrictFilter(admin.SimpleListFilter):
    title = _('School District')
    parameter_name = 'district'

    def lookups(self, request, model_admin):
        districts = SchoolDistrict.objects.all()
        return [(district.id, district.district_name) for district in districts]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(school_district__id=self.value())
        return queryset


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('building_name', 'building_type', 'building_area_sqft', 'building_age', 'building_school')
    list_filter = ('building_school', 'building_type', AreaRangeFilter, BuildingAgeRangeFilter)
    ordering = ('building_type', 'building_area_sqft', 'building_age', 'building_school') 

    def get_school_name(self, obj):
        return obj.building_school.school_name
    get_school_name.short_description = 'School Name'

    def changelist_view(self, request, extra_context=None):
        # Aggregate the sum of building_area_sqft for the current queryset
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            # response.context_data can be None in case of an invalid request (e.g., a bad search query),
            # so we need to check if it is not None before we try to access it.
            if response.context_data:
                qs = response.context_data['cl'].queryset
                total_area = qs.aggregate(Sum('building_area_sqft'))['building_area_sqft__sum']
                # Add the total_area to the context.
                response.context_data['total_area'] = total_area
        except (AttributeError, KeyError):
            # In case of an exception, we just ignore it and the total area won't be shown.
            pass
        return response
    

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        'equipment_tag','equipment_type', 'equipment_model', 'equipment_manufacturer', 
        'install_date', 'warranty_expiration',  'serial_number', 'geo_coordinates', 
        'elec_kw_demand','gas_btuh_demand',
    )

    def install_date(self, obj):
        return obj.equipment_install_date
    install_date.short_description = 'Install Date'
    install_date.admin_order_field = 'equipment_install_date'

    def warranty_expiration(self, obj):
        return obj.equipment_warranty_expiration
    warranty_expiration.short_description = 'Warranty Expiration'
    warranty_expiration.admin_order_field = 'equipment_warranty_expiration'

    def serial_number(self, obj):
        return obj.equipment_serial_number
    serial_number.short_description = 'Serial Number'
    serial_number.admin_order_field = 'equipment_serial_number'

    def geo_coordinates(self, obj):
        return obj.equipment_coordinates
    geo_coordinates.short_description = 'Geo Coordinates'
    geo_coordinates.admin_order_field = 'equipment_coordinates' 

    def elec_kw_demand(self, obj):
        return obj.equipment_elec_kw_demand
    elec_kw_demand.short_description = 'Elec KW Demand'
    elec_kw_demand.admin_order_field = 'equipment_elec_kw_demand'

    def gas_btuh_demand(self, obj):
        return obj.equipment_gas_btuh_demand
    gas_btuh_demand.short_description = 'Gas BTUH Demand'
    gas_btuh_demand.admin_order_field = 'equipment_gas_btuh_demand'
        
    list_filter = (
        'equipment_school', 'equipment_building', 'equipment_type', 'equipment_manufacturer', 
        InstallDateRangeFilter, WarrantyExpirationDateRangeFilter, ElecKwDemandFilter, 
        GasBtuhDemandFilter, GeneratesElecKwFilter, StorageKBtuFilter, StorageKWhFilter
    )
    ordering = (
        'equipment_tag', 'equipment_type', 'equipment_model', 'equipment_manufacturer',
    )


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        'school_name','display_school_district', 'display_calculated_school_area', 
        'display_school_student_population', 'display_school_student_percent_disadvantaged', 
        'display_school_student_percent_english_learners')
    list_filter = (DistrictFilter,)

    def display_school_district(self, obj):
        return format_html("<span>{}</span>", obj.school_district)
    
    def display_calculated_school_area(self, obj):
        calculated_area = obj.calculate_school_area_sqft()
        return format_html("<span>{}</span>", calculated_area)
    
    def display_school_student_population(self, obj):
        return format_html("<span>{}</span>", obj.school_student_population)
    
    def display_school_student_percent_disadvantaged(self, obj):
        return format_html("<span>{}</span>", obj.school_student_percent_disadvantaged)
    
    def display_school_student_percent_english_learners(self, obj):
        return format_html("<span>{}</span>", obj.school_student_percent_english_learners)
        
    display_calculated_school_area.short_description = "AREA (sqft)"
    display_school_district.short_description = "DISTRICT"
    display_school_student_population.short_description = "STUDENT POPULATION"
    display_school_student_percent_disadvantaged.short_description = "% DISADVANTAGED"
    display_school_student_percent_english_learners.short_description = "% ENGLISH LEARNERS"

    display_school_student_population.admin_order_field = 'school_student_population'
    display_school_student_percent_disadvantaged.admin_order_field = 'school_student_percent_disadvantaged'
    display_school_student_percent_english_learners.admin_order_field = 'school_student_percent_english_learners'


class UtilityProviderAccountNumberAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'utility_provider', 'utility_type', 'account_district')
    list_filter = ('utility_provider', 'utility_type', 'account_district')
    search_fields = ('account_number', 'utility_provider', 'utility_type') 

admin.site.register(UtilityProviderAccountNumber, UtilityProviderAccountNumberAdmin)


#################### Service Agreement Admin ####################
# Custom filter for the district
class DistrictListFilter(admin.SimpleListFilter):
    title = 'district'  # or use _('district') for i18n
    parameter_name = 'district'

    def lookups(self, request, model_admin):
        # Return a list of tuples. The first element in each tuple is the coded value for the option that will appear in the URL query. 
        # The second element is the human-readable name for the option that will appear in the right sidebar.
        districts = School.objects.order_by('school_district__district_name').distinct().values_list('school_district__district_name', flat=True)
        return [(district, district) for district in districts]

    def queryset(self, request, queryset):
        # Filter the queryset based on the value provided in the query string and retrievable via `self.value()`.
        if self.value():
            return queryset.filter(school__school_district__district_name=self.value())
        return queryset


@admin.register(ServiceAgreement)
class ServiceAgreementAdmin(admin.ModelAdmin):
    list_display = ('service_agreement_id', 'utility_type', 'school', 'utility_provider_account_number', 'get_school_district', 'has_meter', 'meter_count', 'assigned_meters')
    list_filter = ('utility_type', 'school', DistrictListFilter)

    def get_school_district(self, obj):
        return obj.school.school_district.district_name

    def has_meter(self, obj):
        return Meter.objects.filter(meter_service_agreement_id=obj).exists()

    def meter_count(self, obj):
        # Counts the number of meters associated with the service agreement
        return Meter.objects.filter(meter_service_agreement_id=obj).count()

    def assigned_meters(self, obj):
        meters = Meter.objects.filter(meter_service_agreement_id=obj)
        return ", ".join([str(meter.meter_id) for meter in meters])

    has_meter.boolean = True
    has_meter.short_description = 'Has Meter?'
    meter_count.short_description = 'Number of Assigned Meters'
    assigned_meters.short_description = 'Assigned Meters'
    get_school_district.admin_order_field = 'school__school_district__district_name' 
    get_school_district.short_description = 'School District' 

    search_fields = ['school__school_name', 'utility_provider_account_number__account_number']


@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    list_display = ('meter_id', 'get_utility_type', 'get_meter_school', 'meter_building', 'meter_service_agreement_id')
    list_filter = ('meter_service_agreement_id__utility_type', 'meter_service_agreement_id__school', 'meter_building', 'meter_service_agreement_id')

    def get_utility_type(self, obj):
        # Check if the meter has an associated service agreement
        if obj.meter_service_agreement_id:
            return obj.meter_service_agreement_id.utility_type
        else:
            return "No Service Agreement"

    
    def get_meter_school(self, obj):
        if obj.meter_service_agreement_id:
            return obj.meter_service_agreement_id.school.school_name
        else:
            return "No Service Agreement"
    
    get_meter_school.admin_order_field = 'meter_service_agreement_id__school'  # Allows column order sorting
    get_meter_school.short_description = 'School'
    get_utility_type.admin_order_field = 'meter_service_agreement_id__utility_type'  # Allows column order sorting
    get_utility_type.short_description = 'Utility Type'

admin.site.register(MeterReading)
admin.site.register(PerformanceMetrics)
admin.site.register(UtilityBill)

