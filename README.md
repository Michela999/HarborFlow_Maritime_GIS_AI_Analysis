Overview

HarborFlow is a Maritime GIS \& AI project designed to monitor vessel movements, port operations, weather interactions, and maintenance patterns. The system integrates ArcGIS Pro mapping, Python analytics, SQL queries, anomaly detection, and predictive machine learning models to generate operational insights and professional portfolio-ready outputs.

Objectives

Analyze maritime traffic and port activity using AIS and weather data.

Visualize vessel routes, density, and hotspots with interactive GIS maps.

Clean, preprocess, and merge large datasets using Python and SQL.

Simulate cybersecurity monitoring and risk alerts.

Build predictive models for travel time, route optimization, and maintenance forecasting.

Document all steps for GitHub and portfolio demonstration.

Folder Structure
HarborFlow\_Maritime\_GIS\_AI\_Analysis/
│
├─ data/                  # Raw, cleaned, and processed datasets
├─ docs/                  # Screenshots and documentation
│   └─ screens/
│       ├─ phase0/        # Initial setup
│       ├─ phase1/        # Data import \& exploration
│       ├─ phase2/        # Cleaning \& preprocessing
│       ├─ phase3/        # SQL analysis \& KPIs
│       ├─ phase4/        # Visualizations \& dashboards
│       ├─ phase5/        # Cybersecurity / risk alerts
│       ├─ phase6/        # AI / ML modeling
│       └─ phase7/        # Portfolio \& GitHub integration
├─ maps/                  # ArcGIS Pro project (.aprx) \& geodatabase (.gdb)
├─ notebooks/             # Python / Jupyter notebooks (EDA, SQL, ML)
├─ tableau/               # Tableau dashboards
└─ README.md

Tools \& Technologies

GIS: ArcGIS Pro, shapefiles, geodatabases (.gdb)

Analytics: Python (Pandas, NumPy), SQL (SQLite/PostgreSQL), Excel

Visualization: Tableau, Matplotlib, Seaborn, Plotly

Machine Learning: Scikit-learn, XGBoost, Random Forest

Cybersecurity: Python anomaly detection \& risk simulations

Documentation: GitHub, Markdown, screenshots

Phase Workflow

##### **PHASE 0 LOG**

**Date:** 2026-01-17
**Phase:** 0 – Initial Setup

**Tasks Completed:**

* Folder structure verified
* ArcGIS Pro project and geodatabase created
* Base layers loaded (Ports, Coastline, Land Scale Rank)
* Initial attribute tables reviewed
* Screenshots saved in docs/screens/phase0/

**Insights:**

* Base layers successfully configured
* Ready for Phase 1

**Screenshots Added:**

* docs/screens/phase0/global\_map\_layout.png
* docs/screens/phase0/initial\_setup.png



Phase 1 – Data Import \& Exploration

Import AIS, weather, and maintenance data

Inspect attributes for missing values or anomalies

Generate initial visualizations

Save outputs to docs/screens/phase1/

Phase Workflow

##### **PHASE 1 LOG**

**Date:** 2026-01-23

**Phase:** 1 – Data Import \& Exploration

**Tasks Completed:**

\- Created folders: data/raw/weather and data/raw/maintenance

\- Downloaded hourly weather data for Livorno (Oct 2023) using Open-Meteo API

\- Saved CSV: data/raw/weather/weather\_openmeteo\_livorno\_oct2023.csv

\- Jupyter notebook executed successfully, outputs verified

**Screenshots Added:**

docs/screens/phase1/01\_weather\_download\_livorno.png

docs/screens/phase1/02\_weather\_download\_livorno.png

**Insights:**

\- Folder structure for raw data verified

\- Weather data successfully imported and saved

\- Project ready to expand to grid-based weather download and ArcGIS layer import



Phase 2 – Cleaning \& Preprocessing

Remove invalid/outlier values

Standardize column formats

Merge AIS, weather, and maintenance datasets

Save cleaned datasets in /data/processed/

Store screenshots in docs/screens/phase2/

Phase 3 – SQL Analysis \& KPIs

Build SQL database (SQLite or PostgreSQL)

Aggregate KPIs (vessels per port, avg speed, hotspots)

Export results for Tableau \& ArcGIS

Save visuals in docs/screens/phase3/

Phase 4 – Visualizations \& Dashboards

Create ArcGIS heatmaps \& overlay layers

Build Tableau dashboards: density, speed, weather overlays

Produce Python visualizations (Seaborn, Matplotlib, Plotly)

Save screenshots in docs/screens/phase4/

Phase 5 – Cybersecurity / Risk Alerts

Run anomaly detection scripts on traffic \& weather data

Map flagged anomalies in ArcGIS

Document risk analysis

Store outputs in docs/screens/phase5/

Phase 6 – AI / ML Predictive Modeling

Feature engineering

Train Random Forest, XGBoost, Regression models

Evaluate metrics (RMSE, Accuracy, Precision/Recall)

Map predictions in ArcGIS / Tableau

Save outputs in docs/screens/phase6/

Phase 7 – Portfolio \& GitHub Integration

Organize repository for GitHub

Finalize README \& documentation

Prepare portfolio website sections

Store final screenshots in docs/screens/phase7/

Daily Outputs

ArcGIS maps and screenshots

Python notebooks (data exploration, cleaning, SQL, ML)

Tableau dashboards \& images

README micro-updates with insights

Portfolio website updates

Daily Log Template

## Phase X Log

**Date:** YYYY-MM-DD  
**Phase:** X

## **Tasks Completed:**

* 

## **Insights / Key Observations:**

**Screenshots Added:**

* docs/screens/phaseX/

Future Improvements

Live AIS streaming and API integration

Automated ETL pipelines for real-time data

Cloud deployment (AWS / GCP / Azure)

Web-based interactive GIS dashboards (Leaflet / Mapbox)

Real-time anomaly detection dashboards

