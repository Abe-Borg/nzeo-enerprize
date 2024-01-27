from django.db import connection
FILE_NAME = 'insert_buildings_1.sql'

with connection.cursor() as cursor:
    with open(FILE_NAME, 'r') as file:
        sql_statements = file.read()
        cursor.executescript(sql_statements)