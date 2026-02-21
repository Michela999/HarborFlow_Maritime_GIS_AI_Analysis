# **Phase 3 – SQL Integration & KPI Visualization**  
**Date:** 2026-02-11 → 2026-02-18  
**Status:** ✅ Completed (*SQL staging tables, CSV exports, Google Sheets KPI charts, screenshots*)

---

## **Overview**  

Phase 3 focused on integrating the cleaned datasets into **SQL staging tables**, generating **KPIs** for vessel traffic, vessel speed, weather impact, and maintenance gaps, and creating **portfolio-ready charts**.  

Staging tables were used for **fast KPI calculations and Google Sheets visualization**, while the normalized PostgreSQL schema was prepared for Phase 4 feature engineering and predictive modeling.

---

## **Objectives Achieved**

- **SQL Staging Tables**  
  - Created staging tables for AIS, Weather, and Maintenance datasets.  
  - Loaded CSV exports from `data/processed/` into PostgreSQL using `\copy`.  
  - Prepared normalized PostgreSQL schema (`vessels`, `ports`, `ais_data`, `weather_data`, `maintenance_events`) for Phase 4.  

- **CSV Exports & KPI Preparation**  
  - Generated KPI CSVs from SQL queries:
    - *AIS Traffic* (`ais_traffic_export.csv`)  
    - *Vessel Speed* (`ais_avg_speed_export.csv`)  
    - *Weather Impact* (`weather_speed_export.csv`)  
    - *Maintenance Gaps* (`maintenance_gaps_export.csv`) – simulated realistic intervals  
  - Stored all CSVs in `data/processed/`  

- **Google Sheets KPI Visualization**  
  - Imported KPI CSVs into **Google Sheets**  
  - Cleaned headers and standardized column names  
  - Created charts (Column/Bar/Scatter) for each KPI  
  - Screenshots and downloaded PNG charts saved to:  
    ```
    docs/screens/phase3/
    ```  
  - Chart titles standardized for portfolio presentation:
    - Vessel Traffic by Vessel  
    - Average Vessel Speed  
    - Weather Impact on Vessel Speed  
    - Maintenance Gaps by Vessel  

- **Documentation & Reproducibility**  
  - Added SQL scripts in `sql/` folder:
    - `phase3_drop_tables.sql`  
    - `phase3_create_staging_tables.sql`  
    - `load_phase3_data.sql`  
    - `schema_postgresql_fixed.sql`  
  - Folder structure verified and ready for Phase 4.

---

## **Tools & Technologies Used**

- **Python 3.11** – minor scripts for exporting SQL queries to CSV  
- **PostgreSQL / pgAdmin4** – staging and normalized tables  
- **Google Sheets** – KPI visualization, pivot tables, chart creation  
- **NeoOffice / Excel** – optional validation and chart review  
- **Git / GitHub / Git Bash** – version control, folder management, reproducibility  

---

## **Data Sources & Outputs**

| Dataset       | Source                               | Records | Processed Output                                    | Notes                                   |
|---------------|-------------------------------------|--------|---------------------------------------------------|----------------------------------------|
| AIS           | `data/processed/AIS_cleaned.csv`    | 19,700 | `ais_traffic_export.csv`, `ais_avg_speed_export.csv` | KPI preparation, traffic/speed charts |
| Weather       | `data/processed/Weather_cleaned.csv`| 744    | `weather_speed_export.csv`                        | Weather impact on vessel speed         |
| Maintenance   | `data/processed/Maintenance_cleaned.csv` | 5  | `maintenance_gaps_export.csv`                     | Simulated maintenance gaps             |

**Screenshots / Charts:**  

docs/screens/phase3/ais_traffic_google_chart.png
docs/screens/phase3/ais_speed_google_chart.png
docs/screens/phase3/weather_google_chart.png
docs/screens/phase3/maintenance_google_chart.png


---

## **Phase 3 Results**

- All staging tables created and CSVs loaded successfully  
- KPIs calculated and visualized in Google Sheets  
- Charts downloaded as PNGs for portfolio presentation  
- Normalized schema prepared for Phase 4 feature engineering  
- Folder structure updated with `sql/`, `data/processed/`, `docs/screens/phase3/`  

**Ready for:** *Phase 4 – Feature Engineering & Predictive Modeling*




