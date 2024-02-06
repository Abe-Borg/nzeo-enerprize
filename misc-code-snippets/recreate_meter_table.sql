DROP TABLE IF EXISTS school_management_meter;

CREATE TABLE school_management_meter (
    meter_uid INTEGER PRIMARY KEY,
    meter_utility_provider VARCHAR(100),
    meter_utility_service_id INTEGER,
    meter_utility_billing_account INTEGER,
    meter_utility_service_address VARCHAR(100),
    meter_utility_meter_number INTEGER,
    meter_utility_tariff_name VARCHAR(100),
    meter_interval_start DATETIME,
    meter_interval_end DATETIME,
    meter_interval_kwh_usage FLOAT DEFAULT 0.0,
    meter_fwd_kwh_usage FLOAT DEFAULT 0.0,
    meter_net_kwh_usage FLOAT DEFAULT 0.0,
    meter_rev_kwh_usage FLOAT DEFAULT 0.0,
    meter_source VARCHAR(100),
    meter_updated DATETIME,
    meter_interval_timezone VARCHAR(100) DEFAULT 'us_pacific',
    meter_type VARCHAR(100) DEFAULT 'meter_type',
    meter_building_id INTEGER,
    FOREIGN KEY (meter_building_id) REFERENCES school_management_building(id) ON DELETE SET NULL
);
