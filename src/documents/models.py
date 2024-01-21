# from django.db import models

# # model for a document and all of its metadata
# class Document(models.Model):
#     # document_id = models.AutoField(primary_key=True)
#     document_name = models.CharField(max_length=255)
#     document_type = models.CharField(max_length=255)
#     document_description = models.TextField()
#     document_filepath = models.FileField(upload_to='documents/')
#     document_upload_date = models.DateTimeField(auto_now_add=True)
#     document_last_modified_date = models.DateTimeField(auto_now=True)
#     document_author = models.CharField(max_length=255)
#     document_owner = models.CharField(max_length=255)
#     document_district = models.CharField(max_length=255)
#     document_school = models.CharField(max_length=255)
#     document_tags = models.CharField(max_length=255)
#     document_is_public = models.BooleanField(default=False)
#     document_is_active = models.BooleanField(default=True) 
#     document_is_deleted = models.BooleanField(default=False)
