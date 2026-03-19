#!/usr/bin/env python
# coding: utf-8

# # ==============================
# # HarborFlow – Phase 3: SQL Integration & KPI Visualization
# # ==============================
# **Phase:** 3 – SQL Integration & KPI Visualization  
# **Date:** 2026-02-11 → 2026-02-18  
# **Status:** ✅ Completed (*SQL staging tables, CSV exports, Google Sheets KPI charts, screenshots*)  
# 
# ---
# 
# ## Overview
# 
# Phase 3 focused on integrating the cleaned datasets into **SQL staging tables**, generating **KPIs** for vessel traffic, vessel speed, weather impact, and maintenance gaps, and creating **portfolio-ready charts**.  
# 
# Staging tables were used for **fast KPI calculations and Google Sheets visualization**, while the normalized PostgreSQL schema was prepared for Phase 4 feature engineering and predictive modeling.
# 
# ---
# 
# ## Objectives Achieved
# 
# - **SQL Staging Tables**  
#   - Created staging tables for AIS, Weather, and Maintenance datasets.  
#   - Loaded CSV exports from `data/processed/` into PostgreSQL using `\copy`.  
#   - Prepared normalized PostgreSQL schema (`vessels`, `ports`, `ais_data`, `weather_data`, `maintenance_events`) for Phase 4.  
# 
# - **CSV Exports & KPI Preparation**  
#   - Generated KPI CSVs from SQL queries:
#     - *AIS Traffic* (`ais_traffic_export.csv`)  
#     - *Vessel Speed* (`ais_avg_speed_export.csv`)  
#     - *Weather Impact* (`weather_speed_export.csv`)  
#     - *Maintenance Gaps* (`maintenance_gaps_export.csv`) – simulated realistic intervals  
#   - Stored all CSVs in `data/processed/`.  
# 
# - **Google Sheets KPI Visualization**  
#   - Imported KPI CSVs into **Google Sheets**.  
#   - Cleaned headers and standardized column names.  
#   - Created charts (Column/Bar/Scatter) for each KPI.  
#   - Screenshots and downloaded PNG charts saved to:  
#     ```
#     docs/screens/phase3/
#     ```  
#   - Chart titles standardized for portfolio presentation:
#     - Vessel Traffic by Vessel  
#     - Average Vessel Speed  
#     - Weather Impact on Vessel Speed  
#     - Maintenance Gaps by Vessel  
# 
# - **Documentation & Reproducibility**  
#   - Added SQL scripts in `sql/` folder:
#     - `phase3_drop_tables.sql`  
#     - `phase3_create_staging_tables.sql`  
#     - `load_phase3_data.sql`  
#     - `schema_postgresql_fixed.sql`  
#   - Folder structure verified and ready for Phase 4.
# 
# ---
# 
# ## Tools & Technologies Used
# 
# - **Python 3.11** – CSV inspection and minor scripts for exporting SQL queries  
# - **PostgreSQL / pgAdmin4** – staging and normalized tables  
# - **Google Sheets** – KPI visualization, pivot tables, chart creation  
# - **NeoOffice / Excel** – optional validation and chart review  
# - **Git / GitHub / Git Bash** – version control, folder management, reproducibility  
# 
# ---
# 
# ## Data Sources & Outputs
# 
# | Dataset       | Source                               | Records | Processed Output                                    | Notes                                   |
# |---------------|-------------------------------------|--------|---------------------------------------------------|----------------------------------------|
# | AIS           | `data/processed/AIS_cleaned.csv`    | 19,700 | `ais_traffic_export.csv`, `ais_avg_speed_export.csv` | KPI preparation, traffic/speed charts |
# | Weather       | `data/processed/Weather_cleaned.csv`| 744    | `weather_speed_export.csv`                        | Weather impact on vessel speed         |
# | Maintenance   | `data/processed/Maintenance_cleaned.csv` | 5  | `maintenance_gaps_export.csv`                     | Simulated maintenance gaps             |
# 
# **Screenshots / Charts:**  
# 
# - `docs/screens/phase3/ais_traffic_google_chart.png`  
# - `docs/screens/phase3/ais_speed_google_chart.png`  
# - `docs/screens/phase3/weather_google_chart.png`  
# - `docs/screens/phase3/maintenance_google_chart.png`
# 
# 
#     

# ## 1️⃣ Python: Inspect CSV Headers & Row Counts
# 
# Python was used to confirm the CSV files match the planned SQL table schemas.

# In[17]:


import pandas as pd
import os

data_path = "C:/Users/miche/Documents/HarborFlow_Fresh/data/processed/"

# AIS data
ais_file = os.path.join(data_path, "AIS_cleaned.csv")
ais_df = pd.read_csv(ais_file)
print("AIS_cleaned.csv Columns:", ais_df.columns.tolist())
print("Number of rows:", len(ais_df))
ais_df.head(3)

# Weather data
weather_file = os.path.join(data_path, "Weather_cleaned.csv")
weather_df = pd.read_csv(weather_file)
print("Weather_cleaned.csv Columns:", weather_df.columns.tolist())
print("Number of rows:", len(weather_df))
weather_df.head(3)

# Maintenance data
maintenance_file = os.path.join(data_path, "Maintenance_cleaned.csv")
maintenance_df = pd.read_csv(maintenance_file)
print("Maintenance_cleaned.csv Columns:", maintenance_df.columns.tolist())
print("Number of rows:", len(maintenance_df))
maintenance_df.head(3)


# # 2️⃣ SQL Staging Tables (Reference)
# 
# > **Note:** SQL scripts were run externally via `psql` or `pgAdmin`.
# 
# ---
# 
# ## ⚡ Drop Existing Staging Tables
# 
# ```sql
# -- Drop existing staging tables
# DROP TABLE IF EXISTS ais_data;
# DROP TABLE IF EXISTS weather_data;
# DROP TABLE IF EXISTS maintenance_data;

# ## 🛳 Create AIS Staging Table
# 
# ```sql
# CREATE TABLE ais_data (
#     MMSI TEXT,
#     ShipName TEXT,
#     latitude DOUBLE PRECISION,
#     longitude DOUBLE PRECISION,
#     timestamp TIMESTAMP,
#     speed DOUBLE PRECISION,
#     timestamp_rounded TIMESTAMP
# );
# 

# ## 🌤 Create Weather Staging Table 

# ```sql
# CREATE TABLE weather_data (
#     timestamp TIMESTAMP,
#     temperature DOUBLE PRECISION,
#     wind_speed DOUBLE PRECISION,
#     wind_direction_10m DOUBLE PRECISION,
#     surface_pressure DOUBLE PRECISION,
#     precipitation DOUBLE PRECISION,
#     weather_code INTEGER,
#     latitude DOUBLE PRECISION,
#     longitude DOUBLE PRECISION,
#     timestamp_rounded TIMESTAMP
# );

# 
# ## 🛠 Create Maintenance Staging Table

# ```sql
# CREATE TABLE maintenance_data (
#     vessel_id TEXT,
#     vessel_type TEXT,
#     date DATE,
#     maintenance_type TEXT,
#     hours_since_last INTEGER,
#     next_due_hours INTEGER,
#     port TEXT
# );

# ## Note: These scripts are stored in the repository as:
# sql/phase3_drop_tables.sql and sql/phase3_create_staging_tables.sql

# ## 3️⃣ CSV Import into PostgreSQL
# ## 🛳 AIS Data Import

# ```sql
# \copy ais_data(MMSI, ShipName, latitude, longitude, timestamp, speed, timestamp_rounded)
# FROM 'C:/Users/miche/Documents/HarborFlow_Fresh/data/processed/AIS_cleaned.csv'
# DELIMITER ',' CSV HEADER;

# ## 🌤 Weather Data Import
# 

# ```sql
# \copy weather_data(timestamp, temperature, wind_speed, wind_direction_10m, surface_pressure,
#                    precipitation, weather_code, latitude, longitude, timestamp_rounded)
# FROM 'C:/Users/miche/Documents/HarborFlow_Fresh/data/processed/Weather_cleaned.csv'
# DELIMITER ',' CSV HEADER;

# ## 🛠 Maintenance Data Import

# ```sql
# \copy maintenance_data(vessel_id, vessel_type, date, maintenance_type, hours_since_last, 
#                        next_due_hours, port)
# FROM 'C:/Users/miche/Documents/HarborFlow_Fresh/data/processed/Maintenance_cleaned.csv'
# DELIMITER ',' CSV HEADER;

# ## 📊 Row Counts After Import

# ## ais_data: 
# 4,970
# 
# ## weather_data: 
# 744
# 
# ## maintenance_data: 
# 5

# ## 4️⃣ KPI Queries
# ## 4.1 🚢 Vessel Traffic per Ship

# ```sql
# SELECT ShipName, COUNT(*) AS visits
# FROM ais_data
# GROUP BY ShipName
# ORDER BY visits DESC;

# ## 4.2 ⚡ Average Vessel Speed

# ```sql
# SELECT ShipName, ROUND(AVG(speed)::numeric, 2) AS avg_speed_knots
# FROM ais_data
# GROUP BY ShipName
# ORDER BY avg_speed_knots DESC;

# ## 4.3 🌤 Weather Impact on Speed

# ```sql
# SELECT a.ShipName,
#        ROUND(AVG(a.speed)::numeric, 2) AS avg_speed_knots,
#        ROUND(AVG(w.wind_speed)::numeric, 2) AS avg_wind_speed,
#        ROUND(AVG(w.precipitation)::numeric, 2) AS avg_precipitation
# FROM ais_data a
# JOIN weather_data w
#   ON DATE(a.timestamp) = DATE(w.timestamp)
#   AND ABS(a.latitude - w.latitude) < 0.01
#   AND ABS(a.longitude - w.longitude) < 0.01
# GROUP BY a.ShipName
# ORDER BY avg_speed_knots DESC;

# ## 4.4 🛠 Maintenance Gaps

# ```sql
# SELECT vessel_id,
#        vessel_type,
#        MIN(date) AS first_maintenance,
#        MAX(date) AS last_maintenance,
#        (MAX(date) - MIN(date)) AS maintenance_gap_days
# FROM maintenance_data
# GROUP BY vessel_id, vessel_type
# ORDER BY maintenance_gap_days DESC;

# ## 5️⃣ KPI CSV Exports
# ## 📊 Vessel Traffic Export

# ```sql
# \copy (SELECT ShipName, COUNT(*) AS visits
#        FROM ais_data
#        GROUP BY ShipName
#        ORDER BY visits DESC)
# TO 'C:/Users/miche/Documents/HarborFlow_Fresh/data/processed/ais_traffic_export.csv' CSV HEADER;

# ## ⚡ Average Vessel Speed Export

# ```sql
# \copy (SELECT ShipName, ROUND(AVG(speed)::numeric, 2) AS avg_speed_knots
#        FROM ais_data
#        GROUP BY ShipName
#        ORDER BY avg_speed_knots DESC)
# TO 'C:/Users/miche/Documents/HarborFlow_Fresh/data/processed/ais_avg_speed_export.csv' CSV HEADER;

# ## 🌤 Weather Impact Export

# ```sql
# \copy (SELECT a.ShipName,
#              ROUND(AVG(a.speed)::numeric, 2) AS avg_speed_knots,
#              ROUND(AVG(w.wind_speed)::numeric, 2) AS avg_wind_speed,
#              ROUND(AVG(w.precipitation)::numeric, 2) AS avg_precipitation
#        FROM ais_data a
#        JOIN weather_data w
#          ON DATE(a.timestamp) = DATE(w.timestamp)
#          AND ABS(a.latitude - w.latitude) < 0.01
#          AND ABS(a.longitude - w.longitude) < 0.01
#        GROUP BY a.ShipName
#        ORDER BY avg_speed_knots DESC)
# TO 'C:/Users/miche/Documents/HarborFlow_Fresh/data/processed/weather_speed_export.csv' CSV HEADER;

# ## 🛠 Maintenance Gaps Export

# ```sql
# \copy (SELECT vessel_id,
#              vessel_type,
#              MIN(date) AS first_maintenance,
#              MAX(date) AS last_maintenance,
#              (MAX(date) - MIN(date)) AS maintenance_gap_days
#        FROM maintenance_data
#        GROUP BY vessel_id, vessel_type
#        ORDER BY maintenance_gap_days DESC)
# TO 'C:/Users/miche/Documents/HarborFlow_Fresh/data/processed/maintenance_gaps_export.csv' CSV HEADER;

# ## Note: 
# CSV outputs are used for Google Sheets / NeoOffice charts.
# Screenshots saved in: docs/screens/phase3/

# In[ ]:




