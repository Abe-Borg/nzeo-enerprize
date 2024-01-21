from django.urls import path
from . import views

urlpatterns = [
    path('delete-file', views.delete_file, name = 'delete_file'),
    path('download-file', views.download_file, name = 'download_file'),
    path('upload-file', views.upload_file, name = 'upload_file'),
]