# Generated by Django 5.0 on 2024-01-26 01:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('district_management', '0002_rename_district_bb_bottom_left_lat_schooldistrict_district_bb_northeast_lat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_name', models.CharField(max_length=100)),
                ('building_type', models.CharField(choices=[('classroom', 'Classroom Building'), ('laboratory', 'Laboratory'), ('library', 'Library'), ('restrooms', 'Restrooms'), ('cafeteria', 'Cafeteria'), ('gymnasium', 'Gymnasium'), ('auditorium', 'Auditorium'), ('administrative', 'Administrative'), ('maintenance', 'Maintenance'), ('storage', 'Storage'), ('parking', 'Parking'), ('sports', 'Sports'), ('playground', 'Playground'), ('outdoor', 'Outdoor'), ('other', 'Other'), ('arts', 'Arts'), ('music', 'Music'), ('theater', 'Theater'), ('workshop', 'Workshop'), ('kitchen', 'Kitchen'), ('health', 'Health'), ('counseling', 'Counseling'), ('security', 'Security'), ('energy_plant', 'Energy Plant'), ('commons', 'Student Commons/Common Area')], max_length=100)),
                ('building_area_sqft', models.IntegerField()),
                ('building_geo_lat', models.FloatField()),
                ('building_geo_long', models.FloatField()),
                ('building_photo', models.ImageField(default='images/None/no-img.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('school_area_sqft', models.IntegerField()),
                ('school_address', models.CharField(max_length=100)),
                ('school_student_population', models.IntegerField()),
                ('school_student_percent_disenfrachised', models.IntegerField()),
                ('school_district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district_management.schooldistrict')),
            ],
        ),
        migrations.CreateModel(
            name='PerformanceMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emmissions_co2', models.IntegerField()),
                ('CUI_co2_sqft', models.IntegerField()),
                ('EUI_kbtu_sqft', models.IntegerField()),
                ('EUI_kbtu_student', models.IntegerField()),
                ('renewables_kwh', models.IntegerField()),
                ('peak_demand_kw', models.IntegerField()),
                ('elec_consumption_kwh', models.IntegerField()),
                ('gas_consumption_mmbtu', models.IntegerField()),
                ('total_consumption_mmbtu', models.IntegerField()),
                ('ECI_dollar_sqft', models.IntegerField()),
                ('ECI_dollar_student', models.IntegerField()),
                ('total_cost_dollar', models.IntegerField()),
                ('year_to_date_kbtu_savings', models.IntegerField()),
                ('year_to_date_co2_savings', models.IntegerField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management.school')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_tag', models.CharField(max_length=100)),
                ('equipment_type', models.CharField(choices=[('circuit_breaker', 'Circuit Breaker'), ('transformer', 'Transformer'), ('voltage_regulator', 'Voltage Regulator'), ('electric_meter', 'Electric Meter'), ('solar_panel', 'Solar Panel'), ('generator', 'Generator'), ('surge_protector', 'Surge Protector'), ('ups', 'UPS (Uninterruptible Power Supply)'), ('conduit_fittings', 'Conduit Fittings'), ('junction_box', 'Junction Box'), ('hvac_unit', 'HVAC Unit'), ('boiler', 'Boiler'), ('compressor', 'Compressor'), ('heat_exchanger', 'Heat Exchanger'), ('pump', 'Pump'), ('fan_coil_unit', 'Fan Coil Unit'), ('air_handling_unit', 'Air Handling Unit'), ('chiller', 'Chiller'), ('ductwork_components', 'Ductwork Components'), ('cooling_tower', 'Cooling Tower'), ('water_heater', 'Water Heater'), ('pump', 'Pump'), ('valve', 'Valve'), ('pipe_fittings', 'Pipe Fittings'), ('pressure_reducing_valve', 'Pressure Reducing Valve'), ('backflow_preventer', 'Backflow Preventer'), ('water_softener', 'Water Softener'), ('drainage_system', 'Drainage System'), ('faucet', 'Faucet'), ('toilet', 'Toilet')], max_length=100)),
                ('equipment_manufacturer', models.CharField(choices=[('siemens', 'Siemens'), ('general_electric', 'General Electric'), ('honeywell', 'Honeywell'), ('trane', 'Trane'), ('carrier', 'Carrier'), ('bosch', 'Bosch'), ('abb', 'ABB'), ('schneider_electric', 'Schneider Electric'), ('mitsubishi_electric', 'Mitsubishi Electric'), ('johnson_controls', 'Johnson Controls'), ('daikin', 'Daikin'), ('emerson', 'Emerson'), ('hitachi', 'Hitachi'), ('toshiba', 'Toshiba'), ('rheem', 'Rheem'), ('kohler', 'Kohler'), ('moen', 'Moen'), ('delta', 'Delta'), ('grohe', 'Grohe'), ('american_standard', 'American Standard')], max_length=100)),
                ('equipment_model', models.CharField(max_length=100)),
                ('equipment_serial_number', models.CharField(max_length=100)),
                ('equipment_install_date', models.DateField()),
                ('equipment_warranty_expiration', models.DateField()),
                ('equipment_location', models.CharField(max_length=100)),
                ('equipment_notes', models.TextField(blank=True, max_length=200)),
                ('equipment_elec_kw_demand', models.IntegerField()),
                ('equipment_gas_btuh_demand', models.IntegerField()),
                ('equipment_generates_elec_kw', models.IntegerField()),
                ('equipment_storage_btu_kwh', models.IntegerField()),
                ('equipment_photo', models.ImageField(default='images/None/no-img.jpg', upload_to='images/')),
                ('equipment_building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_management.building')),
                ('equipment_school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management.school')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='building_school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management.school'),
        ),
    ]
