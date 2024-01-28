# Generated by Django 5.0 on 2024-01-28 01:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0005_alter_equipment_equipment_elec_kw_demand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='equipment_building',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_management.building', verbose_name='Associated Building'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_manufacturer',
            field=models.CharField(choices=[('siemens', 'Siemens'), ('general_electric', 'General Electric'), ('honeywell', 'Honeywell'), ('trane', 'Trane'), ('carrier', 'Carrier'), ('bosch', 'Bosch'), ('abb', 'ABB'), ('schneider_electric', 'Schneider Electric'), ('mitsubishi_electric', 'Mitsubishi Electric'), ('johnson_controls', 'Johnson Controls'), ('daikin', 'Daikin'), ('emerson', 'Emerson'), ('hitachi', 'Hitachi'), ('toshiba', 'Toshiba'), ('rheem', 'Rheem'), ('kohler', 'Kohler'), ('moen', 'Moen'), ('delta', 'Delta'), ('grohe', 'Grohe'), ('american_standard', 'American Standard'), ('lennox', 'Lennox'), ('york', 'York'), ('goodman', 'Goodman'), ('lg', 'LG'), ('fujitsu', 'Fujitsu'), ('bryant', 'Bryant'), ('armstrong', 'Armstrong'), ('panasonic', 'Panasonic'), ('frigidaire', 'Frigidaire'), ('maytag', 'Maytag')], max_length=100),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_type',
            field=models.CharField(choices=[('circuit_breaker', 'Circuit Breaker'), ('transformer', 'Transformer'), ('voltage_regulator', 'Voltage Regulator'), ('electric_meter', 'Electric Meter'), ('solar_panel', 'Solar Panel'), ('generator', 'Generator'), ('surge_protector', 'Surge Protector'), ('ups', 'UPS (Uninterruptible Power Supply)'), ('conduit_fittings', 'Conduit Fittings'), ('junction_box', 'Junction Box'), ('lighting_control', 'Lighting Control System'), ('battery_storage', 'Battery Storage'), ('inverter', 'Inverter'), ('power_distribution_unit', 'Power Distribution Unit'), ('energy_management_system', 'Energy Management System'), ('smart_meter', 'Smart Meter'), ('ev_charging_station', 'EV Charging Station'), ('security_camera', 'Security Camera'), ('network_switch', 'Network Switch'), ('fire_alarm_panel', 'Fire Alarm Panel'), ('hvac_unit', 'HVAC Unit'), ('boiler', 'Boiler'), ('compressor', 'Compressor'), ('heat_exchanger', 'Heat Exchanger'), ('pump', 'Pump'), ('fan_coil_unit', 'Fan Coil Unit'), ('air_handling_unit', 'Air Handling Unit'), ('chiller', 'Chiller'), ('ductwork_components', 'Ductwork Components'), ('cooling_tower', 'Cooling Tower'), ('fire_suppression_system', 'Fire Suppression System'), ('gas_detection_system', 'Gas Detection System'), ('irrigation_system', 'Irrigation System'), ('exhaust_fan', 'Exhaust Fan'), ('vibration_isolator', 'Vibration Isolator'), ('filtration_system', 'Filtration System'), ('humidifier', 'Humidifier'), ('dehumidifier', 'Dehumidifier'), ('air_purifier', 'Air Purifier'), ('roof_top_unit', 'Rooftop Unit'), ('water_heater', 'Water Heater'), ('pump', 'Pump'), ('valve', 'Valve'), ('pipe_fittings', 'Pipe Fittings'), ('pressure_reducing_valve', 'Pressure Reducing Valve'), ('backflow_preventer', 'Backflow Preventer'), ('water_softener', 'Water Softener'), ('drainage_system', 'Drainage System'), ('faucet', 'Faucet'), ('toilet', 'Toilet'), ('irrigation_controller', 'Irrigation Controller'), ('sump_pump', 'Sump Pump'), ('greywater_system', 'Greywater System'), ('rainwater_harvesting_system', 'Rainwater Harvesting System'), ('sewage_pump', 'Sewage Pump'), ('water_recycling_system', 'Water Recycling System'), ('water_filtration', 'Water Filtration System'), ('sensor_faucet', 'Sensor Faucet'), ('emergency_shower', 'Emergency Shower'), ('eye_wash_station', 'Eye Wash Station')], max_length=100),
        ),
    ]
