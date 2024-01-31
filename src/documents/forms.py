from django import forms

from school_management.models import Building, Equipment, School
from .models import Document

class DocumentUploadForm(forms.ModelForm):
    document_school = forms.ModelChoiceField(queryset=School.objects.none(), required=True, label='Building (Required)')
    document_building = forms.ModelChoiceField(queryset=Building.objects.none(), required=False, label='Building (Optional)')
    document_equipment = forms.ModelChoiceField(queryset=Equipment.objects.none(), required=False, label='Building (Optional)')

    class Meta:
        model = Document
        exclude = ['document_filepath', 'document_owner', 'document_upload_date']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DocumentUploadForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['document_school'].queryset = School.objects.filter(district=user.get_assigned_district())
        


class DocumentDownloadForm(forms.Form):
    document_name = forms.CharField(max_length=100, required=False)
    document_type = forms.ChoiceField(choices=Document.DOCUMENT_TYPES, required=False)
    document_format = forms.ChoiceField(choices=Document.DOCUMENT_FORMATS, required=False)
    document_description = forms.CharField(max_length=250, required=False)
    document_building = forms.CharField(max_length=100, required=False)
    document_school = forms.CharField(max_length=100, required=False)
    document_equipment = forms.CharField(max_length=100, required=False)
    upload_date = forms.DateField(required=False)

    def search(self):
        queryset = Document.objects.all()
        if self.cleaned_data['document_name']:
            queryset = queryset.filter(document_name__icontains=self.cleaned_data['document_name'])
        if self.cleaned_data['document_type']:
            queryset = queryset.filter(document_type=self.cleaned_data['document_type'])
        if self.cleaned_data['document_format']:
            queryset = queryset.filter(document_format=self.cleaned_data['document_format'])
        if self.cleaned_data['document_description']:
            queryset = queryset.filter(document_description__icontains=self.cleaned_data['document_description'])
        if self.cleaned_data['document_building']:
            queryset = queryset.filter(document_building=self.cleaned_data['document_building'])
        if self.cleaned_data['document_school']:
            queryset = queryset.filter(document_school=self.cleaned_data['document_school'])
        if self.cleaned_data['document_equipment']:
            queryset = queryset.filter(document_equipment=self.cleaned_data['document_equipment'])
        if self.cleaned_data['upload_date']:
            queryset = queryset.filter(upload_date=self.cleaned_data['upload_date'])

        return queryset
