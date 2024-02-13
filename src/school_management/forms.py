from django import forms
from .models import UtilityBill

class UtilityBillForm(forms.ModelForm):
    class Meta:
        model = UtilityBill
        fields = [
            'utility_type', 'bill_statement_date', 'bill_start_date', 
            'bill_end_date', 'total_usage_kwh', 'total_usage_therms', 'total_electric_charges', 
            'total_gas_charges', 'solar_energy_credits', 'total_demand_charge_kw', 
            'total_solar_generation_kwh', 'school', 'district', 'account_number', 'service_agreement_id', 
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
