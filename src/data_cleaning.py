"""
HarborFlow Phase 2 – Data Cleaning & Preprocessing
Author: Michela Monteverde
Purpose: Clean and preprocess AIS, Weather, and Maintenance data
         for GIS and ML analysis.
         - Intermediate cleaned files → data/cleaned/
         - Final processed files → data/processed/
"""

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import os

print("⚓ HarborFlow Phase 2 – Data Cleaning Started\n")

# ------------------------
# File Paths
# ------------------------
RAW_AIS = "data/raw/ais/Livorno.csv"
RAW_WEATHER = "data/raw/weather/weather_openmeteo_livorno_oct2023.csv"
RAW_MAINT = "data/raw/maintenance/maintenance_proxy.csv"
PORTS_SHP = "data/raw/Natural_Earth_quick_start/ne_10m_ports.shp"

CLEANED_DIR = "data/cleaned/"
PROCESSED_DIR = "data/processed/"

os.makedirs(CLEANED_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

# ------------------------
# 1. Load AIS
# ------------------------
ais = pd.read_csv(RAW_AIS)
print(f"AIS rows: {len(ais)}")

# Keep only required columns
ais = ais[['MMSI', 'ShipName', 'Latitude', 'Longitude', 'timestamp', 'speed']].copy()
ais = ais.rename(columns={'Latitude':'latitude','Longitude':'longitude'})

# Convert timestamp to datetime
ais['timestamp'] = pd.to_datetime(ais['timestamp'], errors='coerce')

# Drop rows with invalid MMSI, ShipName, coordinates, or timestamp
ais = ais.dropna(subset=['MMSI','ShipName','latitude','longitude','timestamp'])

# Filter invalid speeds
ais = ais[(ais['speed'] > 0) & (ais['speed'] <= 50)]

# Round timestamp to nearest 15 minutes
ais['timestamp_rounded'] = ais['timestamp'].dt.round('15min')

# Save cleaned intermediate AIS
ais.to_csv(os.path.join(CLEANED_DIR, "AIS_cleaned_intermediate.csv"), index=False)

# Save final processed AIS
ais.to_csv(os.path.join(PROCESSED_DIR, "AIS_cleaned.csv"), index=False)

# ------------------------
# 2. Load Weather
# ------------------------
weather = pd.read_csv(RAW_WEATHER, parse_dates=['time'])

# Rename and standardize columns
weather = weather.rename(columns={
    'time':'timestamp',
    'temperature_2m':'temperature',
    'wind_speed_10m':'wind_speed'
})

# Drop missing key values
weather = weather.dropna(subset=['temperature','wind_speed','precipitation'])

# Round timestamp to nearest 15 min
weather['timestamp_rounded'] = weather['timestamp'].dt.round('15min')

# Save cleaned intermediate Weather
weather.to_csv(os.path.join(CLEANED_DIR, "Weather_cleaned_intermediate.csv"), index=False)

# Save final processed Weather
weather.to_csv(os.path.join(PROCESSED_DIR, "Weather_cleaned.csv"), index=False)

# ------------------------
# 3. Load Maintenance
# ------------------------
maint = pd.read_csv(RAW_MAINT, parse_dates=['last_maintenance'])

# Rename column
maint = maint.rename(columns={'last_maintenance':'date'})

# Save cleaned intermediate Maintenance
maint.to_csv(os.path.join(CLEANED_DIR, "Maintenance_cleaned_intermediate.csv"), index=False)

# Save final processed Maintenance
maint.to_csv(os.path.join(PROCESSED_DIR, "Maintenance_cleaned.csv"), index=False)

# ------------------------
# 4. Create AIS GeoDataFrame
# ------------------------
geometry = [Point(xy) for xy in zip(ais['longitude'], ais['latitude'])]
ais_gdf = gpd.GeoDataFrame(ais, geometry=geometry, crs="EPSG:4326")

# Export shapefile
ais_gdf.to_file(os.path.join(PROCESSED_DIR, "AIS_points.shp"))
print("AIS GeoDataFrame exported as shapefile")

# ------------------------
# 5. Traffic summary per port
# ------------------------
if os.path.exists(PORTS_SHP):
    ports = gpd.read_file(PORTS_SHP)
    ports = ports.to_crs(ais_gdf.crs)  # ensure CRS match

    # Spatial join
    ais_with_ports = gpd.sjoin(ais_gdf, ports, how="left", predicate="intersects")

    # Detect port name column automatically
    port_name_col = None
    for col in ['name','NAME','port_name']:
        if col in ais_with_ports.columns:
            port_name_col = col
            break

    if port_name_col is None:
        raise ValueError("No valid port name column found in ports shapefile!")

    traffic_summary = ais_with_ports.groupby(port_name_col).size().reset_index(name='vessel_count')
    traffic_summary.to_csv(os.path.join(PROCESSED_DIR, "AIS_VesselCount_PerPort.csv"), index=False)
    print("Traffic summary per port exported")
else:
    print("Ports shapefile not found – skipping traffic summary")

print("\n⚓ HarborFlow Phase 2 – Data Cleaning Completed Successfully")
