from account import forms
from documents.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document_name', 'document_type', 'document_description', 'document_filepath', 'document_author', 'document_owner', 'document_district', 'document_school', 'document_tags', 'document_is_public', 'document_is_active', 'document_is_deleted')



class DownloadFileForm(forms.Form):
    file_path = forms.CharField(max_length=255)


    