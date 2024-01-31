# documents.models.py
from django.db import models
from django.conf import settings
from school_management.models import Building, Equipment, School

class Document(models.Model):
    """
        Represents a document within a Django application for managing document operations such as upload, download, and deletion.
        This model stores information about the document, including its name, type, format, description, file path, and upload date. It also maintains relationships with entities like the document owner, associated school, building, and equipment. Historical information about these associations is preserved in separate fields.
        Fields:
        - document_name: The name of the document.
        - document_type: The type of the document, chosen from a predefined set of types.
        - document_format: The format of the document, chosen from a predefined set of formats.
        - document_description: A textual description of the document.
        - document_filepath: The file path where the document is stored.
        - document_upload_date: The date and time when the document was uploaded.
        - [Other Foreign Key Relationships]
        - historical_owner/school/equipment: Fields to store historical association data.
        The `save` method is overridden to update historical fields when current associations are null.
        The `__str__` method returns a string representation of the document and its key details.
    """
    DOCUMENT_TYPES = (
        ('report', 'Report'),
        ('invoice', 'Invoice'),
        ('contract', 'Contract'),
        ('letter', 'Letter'),
        ('manual', 'Manual'),
        ('policy_document', 'Policy Document'),
        ('presentation', 'Presentation'),
        ('spreadsheet', 'Spreadsheet'),
        ('diagram', 'Diagram'),
        ('memo', 'Memo'),
    )
    DOCUMENT_FORMATS = (
        ('pdf', 'PDF'),
        ('doc', 'DOC/DOCX (Word Document)'),
        ('xls', 'XLS/XLSX (Excel Spreadsheet)'),
        ('ppt', 'PPT/PPTX (PowerPoint Presentation)'),
        ('txt', 'TXT (Text File)'),
        ('csv', 'CSV (Comma-Separated Values)'),
        ('jpeg', 'JPEG/JPG (Image File)'),
        ('png', 'PNG (Image File)'),
        ('gif', 'GIF (Image File)'),
        ('zip', 'ZIP (Compressed File)'),
    )

    document_name = models.CharField(max_length=100)
    document_type = models.CharField(max_length=100, choices=DOCUMENT_TYPES)
    document_format = models.CharField(max_length=50, choices=DOCUMENT_FORMATS)
    document_description = models.TextField(max_length=250, default='document_description')
    document_filepath = models.FileField(upload_to='documents/')
    document_upload_date = models.DateTimeField(auto_now_add=True)
    
    document_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True
    )
    document_district = models.ForeignKey(
        'school_management.District', 
        on_delete=models.SET_NULL, 
        null=True
    )
    document_school = models.ForeignKey(
        School, on_delete=models.SET_NULL, 
        null=True
    )
    document_building = models.ForeignKey(
        Building, 
        on_delete=models.SET_NULL, 
        null=True,
        blank = True 
    )
    document_equipment = models.ForeignKey(
        Equipment, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank = True
    )

    historical_owner = models.CharField(max_length=100, blank=True, null=True)
    historical_school = models.CharField(max_length=100, blank=True, null=True)
    historical_equipment = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.document_owner_id:
            self.historical_owner = self.historical_owner or 'Former User ID or Name'
        if not self.document_school_id:
            self.historical_school = self.historical_school or 'Former School ID or Name'
        if not self.document_equipment_id:
            self.historical_equipment = self.historical_equipment or 'Former Equipment ID or Name'
        super(Document, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.document_name)
    



# class GreenButtonData(models.Model):
    #

# class UtilityBill(models.Model):
#     #