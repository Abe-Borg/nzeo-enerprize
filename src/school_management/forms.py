from django import forms
from .models import UtilityBill, School

class UtilityBillForm(forms.ModelForm):
    class Meta:
        model = UtilityBill
        fields = [
            'school', 'service_agreement_id', 'meter_id', 'utility_type', 
            'bill_start_date', 'bill_end_date', 'total_electric_charges', 
            'total_gas_charges', 'elec_consumption_kwh', 'gas_consumption_therms', 
            'peak_demand_kwh', 'off_peak_demand_kwh', 'solar_generation_kwh', 
            'solar_energy_credits'
        ]
        widgets = {
            'bill_start_date': forms.DateInput(attrs={'type': 'date'}),
            'bill_end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
