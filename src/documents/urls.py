from django.urls import path
from . import views

urlpatterns = [
    path('download-document', views.download_document, name = 'download_document'),
    path('upload-document,', views.upload_document, name = 'upload_document'),
    path('upload-green-button-data', views.upload_green_button_data, name = 'upload_green_button_data'),
    path('upload-utility-bill', views.upload_utility_bill, name = 'upload_utility_bill'),
]