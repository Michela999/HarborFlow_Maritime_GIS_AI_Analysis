
# Phase 1 – Data Import, GIS Integration & Exploratory Data Analysis (EDA)

**Date:** 2026-01-23 → 2026-02-01
**Status:** ✅ Completed (Python EDA + ArcGIS Spatial Analysis + Thematic Mapping)

---

## Overview

Phase 1 focused on importing AIS, weather, and maintenance datasets, validating structure and spatial integrity, and performing exploratory analysis using:

* Python (EDA + visualization)
* ArcGIS Pro (GIS integration + spatial analysis)

The objective was to:

* Confirm data readiness
* Build spatial layers
* Associate AIS data with ports
* Produce initial thematic maps and documentation outputs

---

## Project Notebooks

Located in:

```
notebooks/
```

### AIS Analysis

* `phase1_ais_eda.ipynb`

### Weather Analysis

* `phase1_weather_eda.ipynb`

### Maintenance Analysis

* `phase1_maintenance_eda.ipynb`
* `maintenance_proxy.ipynb`

These notebooks include:

* data validation
* exploratory statistics
* initial visualizations
* temporal and categorical analysis

---

## AIS Data

**File**

```
data/raw/ais/Livorno.csv
```

**Records:** ~19,700

### Python EDA Outputs

Located in:

```
docs/screens/phase1/
```

* ais_ship_count_time.png
* ais_speed_distribution.png
* ais_vessel_type_frequency.png
* ais_positions.png
* ais_summary_statistics_before_cleaning.csv

### GIS Processing

1. XY Table To Point → `AIS_points`
2. Spatial Join with Natural Earth Ports →

```
AIS_points_with_Port_final
```

Outputs:

* PortName association
* distance-to-port field
* spatial validation of vessel traffic

---

## Weather Data

**File**

```
data/raw/weather/weather_openmeteo_livorno_oct2023.csv
```

### Python Outputs

* 01_weather_download_livorno.png
* 02_weather_download_livorno.png
* weather_temperature_2m_timeseries.png
* weather_wind_speed_10m_timeseries.png
* weather_wind_direction_10m_histogram.png
* weather_surface_pressure_timeseries.png
* weather_precipitation_timeseries.png

### GIS Processing

* XY conversion → `weather_points`
* spatial validation near Livorno port

---

## Maintenance Proxy Dataset

**File**

```
data/raw/maintenance/maintenance_proxy.csv
```

### EDA Outputs

* maintenance_hours_since_last.png
* maintenance_next_due_hours.png
* maintenance_type_count.png
* maintenance_vessel_type_count.png

---

## GIS Spatial Analysis

### Base Layers

* ne_10m_ports
* ne_10m_coastline
* ne_10m_land_scale_rank

### Spatial Operations Completed

#### AIS Spatial Join

Created:

```
AIS_points_with_Port_final
```

#### Port Traffic Summary

Frequency analysis generated:

```
AIS_VesselCount_PerPort
```

Exported to:

```
data/processed/AIS_VesselCount_PerPort.csv
```

#### Join Back to Ports

Created visualization layer:

```
ports_with_vessels
```

#### Thematic Mapping

Outputs:

* AIS_VesselCount_PerPort.png
* Phase1_Port_Traffic_Thematic_Layout.png

---

## GIS Screenshot Outputs

Location:

```
docs/screens/phase1/
```

Includes:

* AIS thematic port traffic layout
* AIS vessel counts visualization
* weather EDA charts
* maintenance EDA charts
* AIS spatial plots
* weather download validation screenshots

---

## Processed Data Outputs

Location:

```
data/processed/
```

* AIS_VesselCount_PerPort.csv
* AIS_VesselCount_PerPort.csv.xml (ArcGIS metadata)

---

## Phase 1 Results

* AIS spatial data successfully imported and georeferenced
* Weather data spatially validated
* Maintenance dataset analyzed for future ML integration
* Vessel traffic aggregated by port
* Thematic port traffic visualization created
* Project structure prepared for cleaning and preprocessing

---

## Phase 1 Deliverables

### Python

* EDA notebooks
* AIS, weather, and maintenance visualizations

### GIS

* AIS spatial join feature class
* Port traffic frequency table
* Thematic port traffic map
* GIS layout exports
