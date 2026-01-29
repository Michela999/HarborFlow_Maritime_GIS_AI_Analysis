# HarborFlow – Maritime GIS & AI Analysis

HarborFlow is a **Maritime GIS & AI project** designed to analyze vessel movements, port activity, weather conditions, and maintenance patterns.

The project integrates **GIS mapping, Python analytics, SQL, and AI/ML** to deliver operational insights and portfolio-ready outputs for the maritime industry.

---

## **Project Objectives**

- Analyze maritime traffic and port activity using **AIS data**  
- Study **weather impacts** on vessel behavior  
- Simulate **vessel maintenance data** for predictive analysis  
- Visualize routes, density, and hotspots using **GIS**  
- Clean, preprocess, and merge datasets using **Python & SQL**  
- Build foundations for **predictive maintenance and route optimization**  
- Document the full workflow for **GitHub & portfolio presentation**  

---

## **Repository Structure**

HarborFlow_Maritime_GIS_AI_Analysis/
│
├─ data/
│ ├─ raw/
│ │ ├─ ais/
│ │ │ └─ Livorno.csv
│ │ ├─ weather/
│ │ │ └─ weather_openmeteo_livorno_oct2023.csv
│ │ └─ maintenance/
│ │ └─ maintenance_proxy.csv
│ ├─ cleaned/
│ │ └─ .gitkeep
│ └─ processed/
│ └─ .gitkeep
│
├─ docs/
│ └─ screens/
│ ├─ phase0/
│ ├─ phase1/
│ ├─ phase2/
│ ├─ phase3/
│ ├─ phase4/
│ ├─ phase5/
│ ├─ phase6/
│ └─ phase7/
│
├─ maps/ # ArcGIS Pro projects and geodatabases
├─ notebooks/ # Jupyter notebooks (EDA, cleaning, ML)
├─ tableau/ # Tableau dashboards
└─ README.md
---

## **Tools & Technologies**

**GIS**  
- ArcGIS Pro  
- Shapefiles & Geodatabases (.gdb)  

**Analytics & Data**  
- Python (Pandas, NumPy)  
- SQL (SQLite / PostgreSQL)  
- Jupyter Notebooks  

**Visualization**  
- Matplotlib  
- Seaborn  
- Plotly  
- Tableau  

**Machine Learning**  
- Scikit-learn  
- Random Forest  
- XGBoost  

**Documentation**  
- GitHub  
- Markdown  
- Screenshots & logs  

---

## **Phase Workflow Overview**

### **PHASE 0 – Initial Setup**

**Date:** 2026-01-17  

**Phase 0 Base Layers**  
The following shapefiles have been loaded for Phase 0 (ArcGIS Pro):  

- `data/raw/Natural_Earth_quick_start/10m_physical/ne_10m_ports.shp`  
- `data/raw/Natural_Earth_quick_start/10m_physical/ne_10m_coastline.shp`  
- `data/raw/Natural_Earth_quick_start/10m_physical/ne_10m_land_scale_rank.shp`  

**Tasks Completed:**  
- Folder structure verified  
- ArcGIS Pro project and geodatabase created  
- **Base layers loaded** (`Ports`, `Coastline`, `Land`)  
- Initial attribute tables reviewed   

**Outputs:**  
- Screenshots saved in `docs/screens/phase0/`  

---

### **PHASE 1 – Data Import & Exploratory Analysis**

**Date:** 2026-01-23  
**Status:** ✅ In progress  

#### **AIS Data**
- Imported AIS vessel traffic data for **Port of Livorno**  
- **File:** `data/raw/ais/Livorno.csv`  
- Records: ~19,700  
- No missing values or duplicates detected  

**EDA Outputs:**  
- Vessel count over time  
- Speed distribution  
- Vessel type frequency  
- Spatial position plots  

**Screenshots:**  
- `ais_ship_count_time.png`  
- `ais_speed_distribution.png`  
- `ais_vessel_type_frequency.png`  
- `ais_positions.png`  
- `ais_summary_statistics_before_cleaning.csv`  

---

#### **Weather Data**
- Downloaded historical weather data (Oct 2023) using **Open-Meteo API**  
- Location: **Livorno**  
- **File:** `data/raw/weather/weather_openmeteo_livorno_oct2023.csv`  

**Weather EDA Completed:**  
- Verified structure and datatypes  
- No missing values detected  
- Stable latitude/longitude (fixed location)  
- Key variables analyzed:  
  - Temperature  
  - Wind speed & direction  
  - Surface pressure  
  - Precipitation  
  - Weather codes  

**Screenshots:**  
- `01_weather_download_livorno.png`  
- `02_weather_download_livorno.png`  

---

#### **Maintenance Data (Proxy Dataset)**
- Simulated realistic maintenance scenarios  
- **File:** `data/raw/maintenance/maintenance_proxy.csv`  
- Columns:  
  - vessel_id  
  - vessel_type  
  - last_maintenance  
  - maintenance_type  
  - hours_since_last  
  - next_due_hours  
  - port  

**Maintenance EDA Results:**  
- No missing values  
- Vessel types: Cargo, Tanker, Passenger  
- Maintenance types: Engine, Hull, Navigation  
- Hours since last maintenance: **50–300**  
- Next maintenance due: **400–600 hours**  

✅ Phase 1 Maintenance EDA completed successfully  
⚠️ Phase 1 ArcGIS work is still in progress 

---

## **Next Steps**

### **PHASE 2 – Cleaning & Preprocessing**
- Remove outliers  
- Standardize formats  
- Merge AIS, weather, and maintenance datasets  
- Save cleaned data in `data/processed/`  

### **PHASE 3 – SQL Analysis & KPIs**
- Build SQL database  
- Aggregate KPIs (traffic, speed, weather impact)  
- Prepare data for Tableau & ArcGIS  

### **PHASE 4 – Visualizations & Dashboards**
- GIS heatmaps  
- Tableau dashboards  
- Python visualizations  

### **PHASE 5 – Cybersecurity & Risk Alerts**
- Anomaly detection  
- Risk simulations  
- GIS-based alert mapping  

### **PHASE 6 – AI / ML Modeling**
- Feature engineering  
- Predictive maintenance models  
- Route optimization  

### **PHASE 7 – Portfolio Integration**
- Repository polishing  
- Final documentation  
- Portfolio website integration  

---

## **Future Improvements**
- Live AIS streaming  
- Automated ETL pipelines  
- Cloud deployment (AWS / GCP / Azure)  
- Real-time dashboards  
- Advanced predictive models

