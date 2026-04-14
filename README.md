# 🚀 HarborFlow – Maritime Intelligence System (AIS + GIS + AI)

**HarborFlow** is an independent maritime data intelligence system that transforms AIS vessel tracking and geospatial data into actionable insights for shipping operations, risk monitoring, and route analysis.

It is designed as a **prototype decision-support product** for maritime stakeholders, combining GIS analytics, data engineering, and machine learning to interpret vessel behavior at scale.

---

# 🎯 Problem

Maritime stakeholders operate with fragmented and reactive information systems:

- vessel movement is difficult to interpret in real time  
- port congestion and route inefficiencies are not transparently visible  
- risk signals (behavioral + environmental) are scattered across systems  
- decision-making is often delayed or manual  

👉 There is a need for **lightweight maritime intelligence tools** that consolidate AIS and geospatial data into clear operational signals.

---

# 💡 Solution

HarborFlow provides a modular maritime intelligence system that:

- processes AIS and environmental datasets  
- builds geospatial representations of vessel movements  
- generates operational and behavioral risk indicators  
- applies anomaly detection to highlight unusual vessel activity  
- produces decision-ready visual analytics for maritime operations  

👉 The system acts as a **lightweight intelligence layer over raw AIS data**

---

# 🔍 System Outputs

The following visuals highlight key analytical outputs and decision-support insights generated throughout the system.

## 📸 Visual Insights

### 🗺️ Maritime Traffic & Spatial Patterns

<img src="docs/screens/phase4/AIS_HighLowTraffic_Map.png" width="700">

*Geospatial visualization of vessel traffic density highlighting maritime corridors and congestion patterns.*

---

### 📊 Operational Risk vs Maintenance Behavior

<img src="docs/screens/phase5/maintenance_vs_operational_risk.png" width="600">

*Relationship between operational behavior and maintenance signals used for risk modeling.*

---

### 🤖 Anomaly Detection (AI Output)

<img src="docs/screens/phase5/anomaly_scatter_operational_vs_maintenance.png" width="600">

*Unsupervised ML model identifying unusual vessel behavior patterns.*

---

### 📉 Anomaly Score Distribution

<img src="docs/screens/phase5/anomaly_score_distribution.png" width="600">

*Distribution of anomaly scores used to classify abnormal vessel activity.*

---

### ⚠️ Combined Risk Monitoring

<img src="docs/screens/phase5/combined_risk_alerts.png" width="600">

*Unified risk scoring system combining operational and environmental signals.*

---

### 🔗 Risk Correlation Analysis

<img src="docs/screens/phase5/risk_correlation_matrix.png" width="600">

*Correlation structure between key risk variables in the system.*

---

### 🚢 High-Risk Vessel Prioritization

<img src="docs/screens/phase5/top10_critical_vessels.png" width="600">

*Ranking of vessels based on aggregated operational risk indicators.*

---

# 📊 Why It Matters

This system demonstrates how AIS and geospatial data can be transformed into actionable maritime intelligence:

- improved operational visibility  
- early risk detection  
- better route and congestion awareness  
- data-driven maritime decision support  

---

# 🧠 Core Capabilities

- 🚢 **AIS Traffic Intelligence** → vessel movement & port activity  
- 🌦️ **Environmental Impact Analysis** → weather influence on operations  
- 🛠️ **Operational Risk Modeling** → predictive risk indicators  
- 🗺️ **GIS Spatial Intelligence** → routes, ports, geographic clustering  
- 🤖 **Anomaly Detection** → unsupervised ML (Isolation Forest)  
- ⚠️ **Risk Scoring System** → unified operational risk index  
- 📊 **Fleet Intelligence Dataset** → structured analytical outputs  

---

# 🏗️ System Architecture

## Phase 0 — GIS Foundation
- spatial layers and port mapping  

## Phase 1 — Exploratory Data Analysis
- AIS, weather, operational patterns  

## Phase 2 — Data Processing
- cleaning + feature engineering  

## Phase 3 — Data & KPI Layer
- structured metrics extraction  

## Phase 4 — Risk Intelligence Layer
- operational risk scoring system  

## Phase 5 — AI Layer
- anomaly detection (Isolation Forest)  

---

# 📊 Key Metrics

- 158 vessels analyzed  
- ~19,700 AIS records processed  
- 744 environmental observations  
- 12 anomalies detected  

---

# 🧪 Data Sources

- AIS Data — Port of Livorno  
- Weather Data — Open-Meteo API  
- Operational Data — simulated maintenance dataset  
- Port Data — Natural Earth dataset  

---

# 🛠️ Tech Stack

## Data & Analytics
- Python (Pandas, NumPy)  
- SQL (PostgreSQL)  

## Machine Learning
- Scikit-learn  
- XGBoost  
- Random Forest  

## Geospatial
- GeoPandas  
- ArcGIS Pro  

## Visualization
- Tableau  
- Matplotlib  
- Seaborn  

---

# 📈 Outputs

- 📊 dashboards (Tableau)  
- 🗺️ GIS maritime maps  
- 🤖 anomaly detection outputs  
- 📁 fleet intelligence dataset  

---

# 📂 Repository Structure

HarborFlow_Fresh/
├── data/
├── docs/
├── maps/
├── notebooks/
├── sql/
├── src/
├── tableau/
├── .gitignore
├── LICENSE
└── README.md


---

# 🔬 Methodology

- multi-source maritime data integration  
- geospatial feature engineering  
- risk scoring system  
- unsupervised machine learning  
- visual analytics  

---

# 🎯 Use Cases

- maritime logistics operators  
- port congestion monitoring  
- vessel behavior analysis  
- geospatial intelligence workflows  
- transportation analytics  

---

# 📡 Potential Extensions

HarborFlow can evolve into:

- AIS-based maritime intelligence SaaS  
- real-time vessel tracking dashboard  
- API-based shipping data service  
- predictive risk intelligence platform  

---

# 👤 About

HarborFlow demonstrates an independent approach to building maritime data intelligence systems by combining GIS, data engineering, and machine learning into a unified analytical workflow.

The focus is on transforming raw maritime data into structured intelligence for operational and strategic decision-making.

---

# 📌 Status

✅ Completed — end-to-end maritime intelligence pipeline implemented