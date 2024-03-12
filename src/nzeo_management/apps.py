from django.apps import AppConfig
from django.contrib import admin


class NzeoManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nzeo_management'

    def ready(self):
        admin.site.site_header = "NZEO-Climapp"
        admin.site.site_title = "NZEO-Climapp"
