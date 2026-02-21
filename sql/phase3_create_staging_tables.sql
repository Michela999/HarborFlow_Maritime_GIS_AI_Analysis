-- AIS table
CREATE TABLE ais_data (
    MMSI TEXT,
    ShipName TEXT,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    timestamp TIMESTAMP,
    speed DOUBLE PRECISION,
    timestamp_rounded TIMESTAMP
);

-- Weather table
CREATE TABLE weather_data (
    timestamp TIMESTAMP,
    temperature DOUBLE PRECISION,
    wind_speed DOUBLE PRECISION,
    wind_direction_10m DOUBLE PRECISION,
    surface_pressure DOUBLE PRECISION,
    precipitation DOUBLE PRECISION,
    weather_code INTEGER,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    timestamp_rounded TIMESTAMP
);

-- Maintenance table
CREATE TABLE maintenance_data (
    vessel_id TEXT,
    vessel_type TEXT,
    date DATE,
    maintenance_type TEXT,
    hours_since_last INTEGER,
    next_due_hours INTEGER,
    port TEXT
);
