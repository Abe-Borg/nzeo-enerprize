
import random
from datetime import datetime, timedelta

NUM_RECORDS = 1000
file_path = 'equipment_sql_inserts.sql'

# Function to generate a random date within a given range
def generate_random_date(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    time_between_dates = end_date - start_date
    random_number_of_days = random.randrange(time_between_dates.days)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.date()

# Function to generate a weighted random date
def generate_weighted_random_date(early_start, early_end, late_start, late_end, early_weight):
    if random.random() < early_weight:
        return generate_random_date(early_start, early_end).strftime('%Y-%m-%d')
    else:
        return generate_random_date(late_start, late_end).strftime('%Y-%m-%d')

# Equipment types and manufacturers
equipment_types = [
    'circuit_breaker', 'transformer', 'voltage_regulator', 'electric_meter', 'solar_panel',
    'generator', 'surge_protector', 'ups', 'conduit_fittings', 'junction_box', 'hvac_unit',
    'boiler', 'compressor', 'heat_exchanger', 'pump', 'fan_coil_unit', 'air_handling_unit',
    'chiller', 'ductwork_components', 'cooling_tower', 'water_heater', 'valve', 'pipe_fittings',
    'pressure_reducing_valve', 'backflow_preventer', 'water_softener', 'drainage_system',
    'faucet', 'toilet', 'lighting_control', 'battery_storage', 'inverter', 'power_distribution_unit',
    'energy_management_system', 'smart_meter', 'ev_charging_station', 'security_camera',
    'network_switch', 'fire_alarm_panel', 'fire_suppression_system', 'gas_detection_system',
    'irrigation_system', 'exhaust_fan', 'vibration_isolator', 'filtration_system', 'humidifier',
    'dehumidifier', 'air_purifier', 'roof_top_unit', 'irrigation_controller', 'sump_pump',
    'greywater_system', 'rainwater_harvesting_system', 'sewage_pump', 'water_recycling_system',
    'water_filtration', 'sensor_faucet', 'emergency_shower', 'eye_wash_station'
]
manufacturers = [
    'siemens', 'general_electric', 'honeywell', 'trane', 'carrier', 'bosch', 'abb',
    'schneider_electric', 'mitsubishi_electric', 'johnson_controls', 'daikin', 'emerson',
    'hitachi', 'toshiba', 'rheem', 'kohler', 'moen', 'delta', 'grohe', 'american_standard',
    'lennox', 'york', 'goodman', 'lg', 'fujitsu', 'bryant', 'armstrong', 'panasonic',
    'frigidaire', 'maytag'
]


sql_insert_statements = []
for _ in range(NUM_RECORDS):
    school_id = random.randint(1, 95)  # Random school ID from 1 to 95
    equipment_type = random.choice(equipment_types)
    manufacturer = random.choice(manufacturers)
    install_date = generate_weighted_random_date(1950, 1970, 1971, 2010, 0.3)
    warranty_expiration = generate_weighted_random_date(1960, 1980, 1981, 2030, 0.3)
    elec_kw_demand = random.randint(500, 4000) if random.random() < 0.5 else 0
    gas_btuh_demand = random.randint(30000, 70000) if random.random() < 0.5 else 0
    generates_elec_kw = random.randint(50, 250) if random.random() < 0.1 else 0
    storage_btu_kwh = random.randint(50000, 100000) if random.random() < 0.15 else 0

    sql_insert_statements.append(
        f"INSERT INTO school_management_equipment (equipment_school_id, equipment_building_id, equipment_type, "
        f"equipment_manufacturer, equipment_model, equipment_serial_number, equipment_install_date, "
        f"equipment_warranty_expiration, equipment_location, equipment_notes, equipment_elec_kw_demand, "
        f"equipment_gas_btuh_demand, equipment_generates_elec_kw, equipment_storage_btu_kwh, "
        f"equipment_geo_lat, equipment_geo_long) VALUES "
        f"({school_id}, NULL, '{equipment_type}', '{manufacturer}', 'equipment_model', 'equipment_serial_number', "
        f"'{install_date}', '{warranty_expiration}', 'equipment_location', 'equipment_notes', {elec_kw_demand}, "
        f"{gas_btuh_demand}, {generates_elec_kw}, {storage_btu_kwh}, 0.0, 0.0);"
    )

with open(file_path, 'a') as file:
    for insert_statement in sql_insert_statements:
        file.write(insert_statement + "\n")
