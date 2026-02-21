-- Load AIS data
\copy ais_data(MMSI, ShipName, latitude, longitude, timestamp, speed, timestamp_rounded)
FROM 'data/processed/AIS_cleaned.csv'
DELIMITER ',' CSV HEADER;

-- Load Weather data
\copy weather_data(timestamp, temperature, wind_speed, wind_direction_10m, surface_pressure, precipitation, weather_code, latitude, longitude, timestamp_rounded)
FROM 'data/processed/Weather_cleaned.csv'
DELIMITER ',' CSV HEADER;

-- Load Maintenance data
\copy maintenance_data(vessel_id, vessel_type, date, maintenance_type, hours_since_last, next_due_hours, port)
FROM 'data/processed/Maintenance_cleaned.csv'
DELIMITER ',' CSV HEADER;
