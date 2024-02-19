from django import forms
from .models import UtilityBill, PerformanceMetrics, MeterReading

class UtilityBillForm(forms.ModelForm):
    class Meta:
        model = UtilityBill
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MeterReadingForm(forms.ModelForm):
    class Meta:
        model = MeterReading
        fields=('elec_consumption_kwh', 'gas_consumption_therms', 'peak_consumption_kwh', 
                'off_peak_consumption_kwh', 'part_peak_consumption_kwh', 'demand_charge_kw', 
                'solar_generation_kwh')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


