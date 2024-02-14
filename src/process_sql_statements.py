# import os
# import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# # Set up Django
# django.setup()

# from django.db import connection

# FILE_NAME = 'pge_electric_account_numbers.sql'

# with connection.cursor() as cursor:
#     with open(FILE_NAME, 'r') as file:
#         sql_statements = file.read()
#         cursor.executescript(sql_statements)


import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from django.db import connection

FILE_NAME = 'pge_electric_account_numbers.sql'

with connection.cursor() as cursor:
    with open(FILE_NAME, 'r') as file:
        sql_statements = file.read().split(';')        
        for statement in sql_statements:
            statement = statement.strip()
            if statement:
                cursor.execute(statement)
