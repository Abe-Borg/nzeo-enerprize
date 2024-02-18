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
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


