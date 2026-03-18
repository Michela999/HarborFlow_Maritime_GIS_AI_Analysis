# HarborFlow – Maritime GIS & AI Analysis

**HarborFlow** is an end-to-end **Maritime Data Intelligence project** integrating **GIS, data analytics, and machine learning** to analyze vessel activity, port operations, and environmental conditions.  

The project transforms raw maritime data into **actionable insights** through spatial analysis, risk modeling, and anomaly detection — simulating real-world decision-support systems used in modern maritime operations.

---

## 🚀 Project Overview

HarborFlow demonstrates how data-driven approaches can improve:

- Maritime situational awareness  
- Operational efficiency  
- Risk monitoring and early warning systems  

It combines:

- 🗺️ **Geospatial analysis (GIS)**  
- 🐍 **Python data analytics**  
- 🗄️ **SQL data modeling**  
- 🤖 **Machine learning (anomaly detection)**  
- 📊 **Data visualization & dashboards**  

---

## 🔍 Key Capabilities

- 🚢 **AIS Traffic Analysis** – Analyze vessel movements, density, and port activity patterns  
- 🌦️ **Weather Impact Analysis** – Evaluate how environmental conditions influence vessel operations  
- 🛠️ **Maintenance Risk Modeling** – Simulate maintenance patterns for predictive insights  
- 🗺️ **Spatial Intelligence (GIS)** – Map vessel routes, port infrastructure, and geographic risk factors  
- 🤖 **AI-Based Anomaly Detection** – Detect abnormal vessel behavior using Isolation Forest  
- ⚠️ **Risk Scoring System** – Combine operational, maintenance, and weather risks into unified indicators  
- 📊 **Fleet Risk Intelligence Dataset** – Produce a structured dataset for monitoring and prioritization  

---

# 🧠 Project Architecture

The project is structured as a complete data pipeline:

## Phase 0 — GIS Setup
- Base maps and port layers  
- Spatial data integration  
**Outputs:** Base maps, port shapefiles, initial GIS validation  

## Phase 1 — Data Import, GIS Integration & EDA
- AIS, weather, and maintenance data analysis  
- Initial statistics, visualizations, and thematic mapping  
**Outputs:** EDA notebooks, AIS/Weather/Maintenance charts, thematic maps  

## Phase 2 — Data Cleaning & Preprocessing
- Data cleaning and filtering  
- Timestamp conversion and rounding  
- Feature engineering for modeling  
**Outputs:** Cleaned CSVs, GIS-ready shapefiles, intermediate datasets  

## Phase 3 — SQL Integration & KPI Visualization
- Relational schema design  
- KPI extraction and querying  
**Outputs:** SQL staging tables, normalized schema, KPI CSVs, Google Sheets charts  

## Phase 4 — Operational Risk Dashboard & GIS/AI Integration
- Operational risk scoring  
- Maintenance and weather risk modeling  
- Combined risk score calculation  
**Outputs:** Enhanced dataset (`AIS_Tableau_Final_Operational_Enhanced.csv`), Tableau dashboards, KPI tiles  

## Phase 5 — AI Anomaly Detection & Fleet Risk Intelligence
- Anomaly detection using Isolation Forest  
- Anomaly scoring and classification  
- Fleet-level intelligence dataset creation  
- Risk prioritization and ranking  
**Outputs:** `fleet_risk_intelligence.csv`, anomaly & risk visualizations, portfolio-ready charts  

---

## 📊 Quick Stats

| Metric | Count |
|--------|-------|
| Vessels analyzed | 158 |
| AIS records | ~19,700 |
| Weather observations | 744 |
| Maintenance events | 5 |
| Anomalies detected | 12 |

---

## 🧪 Data Sources

- **AIS Data** — Vessel traffic data (Port of Livorno)  
- **Weather Data** — Historical weather (Open-Meteo API)  
- **Maintenance Data** — Simulated dataset for modeling  
- **Ports Dataset** — Natural Earth shapefiles  

---

## 🛠️ Technologies Used

**Geospatial Analysis**  
- ArcGIS Pro  
- GeoPandas  
- Pyogrio  

**Data & Analytics**  
- Python (Pandas, NumPy)  
- SQL (PostgreSQL, pgAdmin)  

**Machine Learning**  
- Scikit-learn (Isolation Forest)  
- Random Forest  
- XGBoost  

**Visualization**  
- Matplotlib  
- Seaborn  
- Tableau Public  
- GIS mapping tools  

---

## 📈 Outputs & Deliverables

- 📊 Risk dashboards (Tableau & Python)  
- 🗺️ GIS-based spatial visualizations  
- 📉 Statistical analysis and charts  
- 🤖 Anomaly detection results  
- 📁 Fleet risk intelligence dataset  

---

## 🔬 Methodology Highlights

- Multi-source data integration (AIS + weather + maintenance)  
- Feature engineering for risk modeling  
- Weighted scoring system for combined risk indicators  
- Unsupervised learning for anomaly detection  
- Visual analytics for interpretability  

---

## 🎯 Applications

This project is relevant for:

- Port authorities  
- Maritime logistics companies  
- Smart port initiatives  
- Maritime data analytics roles  
- AI applications in transportation systems  

---

## 📊 Repository Structure

HarborFlow_Fresh/
│
├── data/ # Raw, cleaned, and processed datasets
├── docs/ # Technical logs, screenshots, reports
├── maps/ # GIS assets (lightweight)
├── notebooks/ # Jupyter notebooks (analysis & modeling)
├── sql/ # Database schema and queries
├── src/ # Python scripts, helper modules
├── tableau/ # Dashboard outputs
├── venv/ # Virtual environment (ignored by Git)
├── .gitattributes
├── .gitignore
├── LICENSE
└── README.md


> Large GIS files (.aprx, .gdb) are excluded to keep the repository lightweight.

---

## 🔬 Reproducibility

- All steps are documented in **notebooks/**  
- Python scripts in **src/** allow pipeline re-run  
- CSV exports and shapefiles in **data/processed/**  
- Tableau dashboards in **tableau/**  

This ensures the full workflow can be reproduced from raw data to final AI-enhanced risk intelligence.

---

## 📌 Project Status

**Status:** ✅ Completed  

All phases — including anomaly detection and fleet risk intelligence — have been fully implemented and validated.

---

## 📬 About

HarborFlow is a **portfolio project** demonstrating the integration of:

- GIS systems  
- Data engineering  
- Machine learning  
- Operational risk analysis  

It reflects a complete workflow from raw data to actionable intelligence in a maritime context.
