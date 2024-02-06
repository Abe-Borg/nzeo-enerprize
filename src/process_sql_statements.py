import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# Set up Django
django.setup()

from django.db import connection

FILE_NAME = 'recreate_meter_table.sql'

with connection.cursor() as cursor:
    with open(FILE_NAME, 'r') as file:
        sql_statements = file.read()
        cursor.executescript(sql_statements)
