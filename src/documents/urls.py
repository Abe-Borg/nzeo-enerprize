from django.urls import path
from . import views

urlpatterns = [
    path('download-file', views.download_file, name = 'download_file'),
    path('upload-file', views.upload_file, name = 'upload_file'),
    path('upload-green-button-data', views.upload_green_button_data, name = 'upload_green_button_data'),
    path('upload-utility-bill', views.upload_utility_bill, name = 'upload_utility_bill'),
]