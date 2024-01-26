from django.db import models
from django.conf import settings

from school_management.models import Building, Equipment, School

class Document(models.Model):

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
    document_description = models.TextField(max_length=250)
    document_filepath = models.FileField(upload_to='documents/')
    document_upload_date = models.DateTimeField(auto_now_add=True)
    
    document_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
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
    )
    document_equipment = models.ForeignKey(
        Equipment, 
        on_delete=models.SET_NULL, 
        null=True, 
    )

    historical_owner = models.CharField(max_length=255, blank=True, null=True)
    historical_school = models.CharField(max_length=255, blank=True, null=True)
    historical_equipment = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.document_owner_id:
            self.historical_owner = self.historical_owner or 'Former User ID or Name'
        if not self.document_school_id:
            self.historical_school = self.historical_school or 'Former School ID or Name'
        if not self.document_equipment_id:
            self.historical_equipment = self.historical_equipment or 'Former Equipment ID or Name'
        super(Document, self).save(*args, **kwargs)