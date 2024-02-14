from django import forms
from .models import UtilityBill

class UtilityBillForm(forms.ModelForm):
    class Meta:
        model = UtilityBill
        fields = [
            'utility_type', 'district', 'school', 'service_agreement_id', 'bill_statement_date', 
            'bill_start_date', 'bill_end_date', 'total_electric_usage_kwh', 
            'total_electric_charges', 'total_gas_usage_therms',  
            'total_gas_charges', 'solar_energy_credits', 'total_demand_charge_kw', 
            'total_solar_generation_kwh',   
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
