import random
from datetime import datetime, timedelta

# Function to generate a random date within a given range
def generate_random_date(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    time_between_dates = end_date - start_date
    random_number_of_days = random.randrange(time_between_dates.days)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.date()

# Function to generate SQL insert statements for Equipment
def generate_equipment_inserts(building_school_mappings, num_records):
    equipment_types = (
        'circuit_breaker', 'transformer', 'voltage_regulator', 'electric_meter', 'solar_panel', 
        'generator', 'surge_protector', 'ups', 'conduit_fittings', 'junction_box', 'hvac_unit', 
        'boiler', 'compressor', 'heat_exchanger', 'pump', 'fan_coil_unit', 'air_handling_unit', 
        'chiller', 'ductwork_components', 'cooling_tower', 'water_heater', 'pump', 'valve', 
        'pipe_fittings', 'pressure_reducing_valve', 'backflow_preventer', 'water_softener', 
        'drainage_system', 'faucet', 'toilet'
    )
    manufacturers = (
        'siemens', 'general_electric', 'honeywell', 'trane', 'carrier', 'bosch', 
        'abb', 'schneider_electric', 'mitsubishi_electric', 'johnson_controls', 'daikin', 
        'emerson', 'hitachi', 'toshiba', 'rheem', 'kohler', 'moen', 'delta', 'grohe', 
        'american_standard'
    )

    inserts = []
    for _ in range(num_records):
        # Randomly select a building and get the corresponding school
        building_id, school_id = random.choice(list(building_school_mappings.items()))

        # Generate other fields based on the provided specifications
        equipment_type = random.choice(equipment_types)
        manufacturer = random.choice(manufacturers)
        install_date = generate_random_date(1950, 2010)
        warranty_expiration = generate_random_date(1950, 2030)
        elec_kw_demand = random.randint(500, 4000) if random.random() < 0.5 else 0
        gas_btuh_demand = random.randint(30000, 70000) if random.random() < 0.5 else 0
        generates_elec_kw = random.randint(50, 250) if random.random() < 0.1 else 0
        storage_btu_kwh = random.randint(50000, 100000) if random.random() < 0.15 else 0

        insert_statement = f"INSERT INTO equipment (equipment_school_id, equipment_building_id, equipment_type, equipment_manufacturer, equipment_model, equipment_serial_number, equipment_install_date, equipment_warranty_expiration, equipment_location, equipment_notes, equipment_elec_kw_demand, equipment_gas_btuh_demand, equipment_generates_elec_kw, equipment_storage_btu_kwh, equipment_geo_lat, equipment_geo_long) VALUES ({school_id}, {building_id}, '{equipment_type}', '{manufacturer}', 'equipment_model', 'equipment_serial_number', '{install_date}', '{warranty_expiration}', 'equipment_location', 'equipment_notes', {elec_kw_demand}, {gas_btuh_demand}, {generates_elec_kw}, {storage_btu_kwh}, 0.0, 0.0);"
        inserts.append(insert_statement)
    
    return inserts

# Building-to-school mappings for the provided data
building_school_mappings = {
    2349: 66, 2350: 3, 2351: 90, 2352: 16, 2353: 53, 2354: 81, 2355: 7, 2356: 57, 2357: 72, 2358: 34,
    # ... other mappings ...
}

# Generate 10 practice SQL insert statements
practice_inserts = generate_equipment_inserts(building_school_mappings, 10)
practice_inserts

