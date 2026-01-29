HarborFlow – Maritime GIS & AI Analysis

HarborFlow is a Maritime GIS & AI project focused on analyzing vessel movements, port activity, weather conditions, and maintenance patterns.

The project integrates GIS mapping, Python analytics, SQL, and AI/ML to produce operational insights and portfolio-ready outputs for the maritime and logistics sectors.

Project Goals

Analyze maritime traffic and port activity using AIS data

Evaluate weather impacts on vessel behavior

Simulate and study vessel maintenance patterns

Visualize spatial dynamics with GIS

Build foundations for predictive maintenance and route optimization

Document a complete, professional data workflow

Repository Overview

HarborFlow_Maritime_GIS_AI_Analysis/
│
├─ data/
│   ├─ raw/          # Source datasets (AIS, weather, maintenance)
│   ├─ cleaned/      # Cleaned datasets (generated)
│   └─ processed/    # Feature-ready datasets (generated)
│
├─ docs/
│   ├─ logs/         # Detailed phase documentation
│   └─ screens/      # GIS & analysis screenshots by phase
│
├─ maps/             # GIS assets (excluding large ArcGIS project files)
├─ notebooks/        # Jupyter notebooks (EDA, cleaning, ML)
├─ tableau/          # Tableau dashboards
└─ README.md


Large GIS project files (.aprx, .gdb) are intentionally excluded due to size and platform locking.

Project Status

| Phase   | Description                     | Status         |
| ------- | ------------------------------- | -------------- |
| Phase 0 | Project setup & GIS base layers | ✅ Completed    |
| Phase 1 | Data import & EDA               | ⚠️ In progress |
| Phase 2 | Cleaning & preprocessing        | ⏳ Planned      |
| Phase 3 | SQL analysis & KPIs             | ⏳ Planned      |
| Phase 4 | Visualizations & dashboards     | ⏳ Planned      |
| Phase 5 | Risk analysis & alerts          | ⏳ Planned      |
| Phase 6 | AI / ML modeling                | ⏳ Planned      |
| Phase 7 | Portfolio integration           | ⏳ Planned      |

Detailed technical logs for each phase are available in docs/logs/.

Technologies Used

GIS

ArcGIS Pro

Shapefiles & Geodatabases

Data & Analytics

Python (Pandas, NumPy)

SQL

Jupyter Notebooks

Visualization

GIS maps

Python plots

Tableau dashboards

Machine Learning

Scikit-learn

Random Forest

XGBoost

Notes

Base GIS layers are sourced from Natural Earth (10m resolution)

Real maintenance data is simulated using a proxy dataset

The ArcGIS Pro project file (.aprx) can be shared via cloud storage upon request

Future Extensions

Live AIS data ingestion

Automated ETL pipelines

Cloud deployment (AWS / GCP / Azure)

Real-time dashboards

Advanced predictive modelling

📁 For detailed workflows, logs, and screenshots, see the docs/ folder.

