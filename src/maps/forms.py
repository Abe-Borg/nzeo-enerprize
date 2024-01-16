from django import forms

# create form to save markup model data to database
class MarkupForm(forms.Form):
    layer = forms.CharField(max_length=255)
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    geo_longitude = forms.FloatField()
    geo_latitude = forms.FloatField()
    created_at = forms.DateTimeField()
    updated_at = forms.DateTimeField()
    created_by = forms.CharField(max_length=255)

