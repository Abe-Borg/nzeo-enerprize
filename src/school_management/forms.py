from django import forms
from .models import UtilityBill

class UtilityBillForm(forms.ModelForm):
    class Meta:
        model = UtilityBill
        fields = [
            'district','school', 'service_agreement_id', 'meter_id', 'utility_type', 'bill_statement_date', 
            'bill_start_date', 'bill_end_date', 'total_electric_charges', 
            'total_gas_charges', 'solar_energy_credits', 'total_usage_kwh', 'account_number',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
