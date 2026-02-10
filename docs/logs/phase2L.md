
# Phase 2 – Data Cleaning & Preprocessing

**Date:** 2026-02-02 → 2026-02-10
**Status:** ✅ Completed (Python data cleaning + GeoPandas + CSV & shapefile exports)

---

## Overview

Phase 2 focused on **cleaning and preprocessing AIS, weather, and maintenance datasets** to prepare them for GIS mapping, predictive analytics, and Phase 3 SQL/ML integration.

The main objectives achieved:

* Filtered invalid or extreme values in AIS (missing MMSI/ShipName, speed = 0, speed > 50 knots)
* Converted and rounded timestamps for AIS and weather data
* Cleaned maintenance dataset and standardized date format
* Exported GIS-ready AIS points as shapefile
* Calculated traffic summary per port
* Exported cleaned datasets to `processed` and `cleaned` folders

---

## Project Notebook / Script

Located in:

```
notebooks/phase2_data_cleaning.py
```

This script includes:

* Data cleaning and filtering (AIS, weather, maintenance)
* Timestamp conversion and rounding
* GIS export of AIS points as shapefile
* Port traffic summary calculation
* CSV exports of cleaned datasets

---

## AIS Data

**File**

```
data/raw/ais/Livorno.csv
```

**Records:** 19,700

### Cleaning Steps

* Dropped rows with missing MMSI, ShipName, latitude, or longitude
* Removed extreme speeds (>50 knots or =0)
* Converted `timestamp` to datetime
* Rounded timestamp to 15-minute intervals

### Outputs

**Processed folder:**

```
data/processed/AIS_cleaned.csv
data/processed/AIS_points.* (shapefile)
data/processed/ais_summary_statistics_before_cleaning.csv
data/processed/AIS_VesselCount_PerPort.csv
```

**Cleaned folder:**

```
data/cleaned/AIS_cleaned_intermediate.csv
```

---

## Weather Data

**File**

```
data/raw/weather/weather_openmeteo_livorno_oct2023.csv
```

**Records:** 744

### Cleaning Steps

* Converted `time` column to datetime
* Rounded timestamps to match AIS intervals
* Exported cleaned dataset

### Outputs

**Processed folder:**

```
data/processed/Weather_cleaned.csv
```

**Cleaned folder:**

```
data/cleaned/Weather_cleaned_intermediate.csv
```

---

## Maintenance Proxy Dataset

**File**

```
data/raw/maintenance/maintenance_proxy.csv
```

**Records:** 5

### Cleaning Steps

* Converted `last_maintenance` to datetime
* Verified vessel IDs, maintenance types, and ports
* Exported cleaned dataset

### Outputs

**Processed folder:**

```
data/processed/Maintenance_cleaned.csv
```

**Cleaned folder:**

```
data/cleaned/Maintenance_cleaned_intermediate.csv
```

---

## GIS Spatial Analysis

* Created AIS GeoDataFrame
* Exported shapefile:

```
data/processed/AIS_points.*
```

* Calculated traffic summary per port:

```
data/processed/AIS_VesselCount_PerPort.csv
```

---

## Phase 2 Results

* AIS, weather, and maintenance datasets cleaned and validated
* AIS GeoDataFrame created and exported as shapefile
* Traffic summary per port calculated and exported
* Intermediate cleaned datasets stored in `cleaned` folder for reproducibility
* Ready for Phase 3 SQL/ML integration

---

## Tools Used

* Python 3.11 (Pandas, GeoPandas, Shapely)
* Pyogrio (shapefile export)
* Jupyter Notebook / Python scripts
* Git / GitHub (version control)

