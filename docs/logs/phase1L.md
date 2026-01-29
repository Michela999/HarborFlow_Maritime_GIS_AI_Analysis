# Phase 1 – Data Import & Exploratory Data Analysis (EDA)

**Date:** 2026-01-23  
**Status:** Python EDA completed | ArcGIS visualizations in progress

## Overview

Phase 1 focuses on importing AIS, weather, and maintenance datasets and performing exploratory data analysis to assess data quality, structure, and analytical potential.

This phase ensures datasets are **ready for GIS import and spatial analysis**, before cleaning, preprocessing, and layer integration in ArcGIS.

---

## AIS Data

**Description:**  
Automatic Identification System (AIS) vessel traffic data for the **Port of Livorno**.

**File:**  
`data/raw/ais/Livorno.csv`

**Records:** ~19,700

### Data Quality Checks
- No missing values detected
- No duplicate records identified
- Timestamp and positional data validated

### EDA Performed
- Vessel count over time
- Speed distribution analysis
- Vessel type frequency
- Spatial plotting of vessel positions

### Outputs
- `ais_ship_count_time.png`
- `ais_speed_distribution.png`
- `ais_vessel_type_frequency.png`
- `ais_positions.png`
- `ais_summary_statistics_before_cleaning.csv`

---

## Weather Data

**Source:** Open-Meteo API  
**Location:** Livorno  
**Period:** October 2023

**File:**  
`data/raw/weather/weather_openmeteo_livorno_oct2023.csv`

### Data Validation
- Dataset structure and datatypes verified
- No missing values detected
- Latitude and longitude fixed (single weather station reference)

### Variables Analyzed
- Temperature
- Wind speed
- Wind direction
- Surface pressure
- Precipitation
- Weather codes

### Outputs
- `01_weather_download_livorno.png`
- `02_weather_download_livorno.png`

---

## Maintenance Data (Proxy Dataset)

**Description:**  
A simulated maintenance dataset created to represent realistic vessel maintenance scenarios, due to limited availability of public maritime maintenance data.

**File:**  
`data/raw/maintenance/maintenance_proxy.csv`

### Dataset Structure
- `vessel_id`
- `vessel_type`
- `last_maintenance`
- `maintenance_type`
- `hours_since_last`
- `next_due_hours`
- `port`

### EDA Results
- No missing values
- Vessel types: Cargo, Tanker, Passenger
- Maintenance types: Engine, Hull, Navigation
- Hours since last maintenance: 50–300
- Next maintenance due: 400–600 hours

---

## GIS Status

- Base GIS layers prepared during Phase 0
- Python EDA confirmed that datasets have consistent coordinates and formats suitable for ArcGIS import
- **ArcGIS visualizations, spatial joins, and advanced layer integrations are ongoing**

---

## Outputs

- Python EDA notebooks
- Summary statistics and visualizations
- Screenshots saved in:

`docs/screens/phase1/`

---

## Notes

- Phase 1 confirms dataset readiness for GIS import

- No transformations applied yet; cleaning and preprocessing will occur in Phase 2