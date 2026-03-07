
# **Phase 4 – Operational Risk Dashboard & GIS/AI Integration**

**Date:** 2026-02-24 → 2026-03-07
**Status:** ✅ Completed (*Phase 4 dataset preparation, operational risk scoring, KPI tiles, fleet risk charts, Tableau dashboard, screenshots*)

---

## **Overview**

Phase 4 focused on integrating **traffic predictions, maintenance, and weather factors** into a comprehensive **operational risk framework** for the Port of Livorno fleet.

The work included:

* **Data normalization and feature engineering** for ML-ready and visualization-ready datasets
* **Operational risk calculation** combining traffic, maintenance, and weather metrics
* **Fleet-level KPIs** and identification of high-risk vessels
* **Tableau dashboard preparation** with KPI tiles, Fleet Risk Distribution, Top 10 High-Risk Vessels, and Risk Interaction Scatter plots
* **Portfolio-ready outputs** with clear titles and descriptions

This phase completes the end-to-end preparation of Phase 4 deliverables and sets the stage for Phase 5 (advanced weather and maintenance analytics).

---

## **Objectives Achieved**

* **Phase 4 Dataset Preparation**

  * Loaded Phase 3 CSVs (`AIS_Tableau_Final_v3.csv`, `weather_speed_export.csv`)
  * Cleaned and normalized:

    * `maintenance_risk_score` → `maintenance_risk_score_norm`
    * `predicted_high_traffic` → `predicted_high_traffic_norm`
    * `weather_risk_score` → `weather_risk_score_norm`
  * Merged AIS, traffic prediction, maintenance, and weather into **Phase 4 enhanced dataset**
  * Saved final CSV:

    ```
    data/processed/AIS_Tableau_Final_Operational_Enhanced.csv
    ```

* **Operational Risk Scoring**

  * Computed **operational_risk_score_final** using weighted sum:

    ```
    0.4 * traffic + 0.3 * maintenance + 0.3 * weather
    ```
  * Generated **percentile-based risk categories** (`Low`, `Medium`, `High`)
  * Computed **fleet risk rank** for prioritizing vessels

* **KPI Tiles & Charts**

  * Calculated fleet-level KPIs:

    * Total fleet: 158 vessels
    * Average operational risk: 0.207
    * Maximum operational risk: 0.717
    * High traffic vessels: 3
  * Built charts:

    * Fleet Risk Distribution (Low/Medium/High)
    * Top 10 High-Risk Vessels (bar chart)
    * Risk Interaction Scatter (maintenance vs operational risk)

* **Tableau Dashboard Integration**

  * Created **HarborFlow – Port of Livorno Maritime Risk Analytics** dashboard
  * Dashboard sections:

    1. KPI Tiles
    2. Fleet Risk Distribution
    3. Top 10 High-Risk Vessels
    4. Risk Interaction Scatter
  * Verified interactivity, colors, and labels
  * Added subtitle: *Fleet Operational Risk Monitoring • Traffic Prediction • Weather Risk Analysis*
  * Published to **Tableau Public** for portfolio presentation
  * Exported portfolio-ready PNG: HarborFlow_Fresh/tableau/HarborFlow_Operational_Risk_Dashboard.png
  * ArcGIS Pro Map:
docs/screens/phase4/ AIS_HighLowTraffic_Map

* **Documentation & Reproducibility**

  * All Python scripts documented in Jupyter Notebook (`Phase4_Operational_Risk.ipynb`)
  * Notebook contains: data loading, normalization, risk calculation, KPI computation, Tableau export preparation
  * Outputs verified and ready for Phase 5

---

## **Tools & Technologies Used**

* **Python 3.11** – data processing, risk scoring, KPI computation
* **Pandas / NumPy / Seaborn / Matplotlib** – dataset manipulation and quick visualizations
* **Tableau Public (Desktop)** – dashboard creation, KPI tiles, portfolio-ready visuals
* **Git / GitHub** – version control, reproducibility, notebook and CSV storage

---

## **Data Sources & Outputs**

| Dataset       | Source                     | Records | Processed Output                             | Notes                              |
| ------------- | -------------------------- | ------- | -------------------------------------------- | ---------------------------------- |
| AIS + Traffic | `AIS_Tableau_Final_v3.csv` | 94      | `AIS_Tableau_Final_Operational.csv`          | Traffic prediction, risk scoring   |
| Weather       | `weather_speed_export.csv` | 94      | Integrated into operational risk scoring     | Avg precipitation, wind speed      |
| Maintenance   | Phase 3 dataset            | 94      | `maintenance_risk_score_norm`                | Partial coverage; gaps noted       |
| Phase 4 Final | Combined                   | 94      | `AIS_Tableau_Final_Operational_Enhanced.csv` | Ready for Tableau dashboard & KPIs |

---

## **Phase 4 Results**

* All enhanced datasets created and merged successfully
* Operational risk scores and percentile categories computed
* Fleet-level KPIs calculated and verified
* Tableau dashboard designed, polished, and published
* Portfolio-ready visuals prepared with proper titles and subtitles
* Notebook documented for reproducibility

---

**Ready for:** *Phase 5 – Risk Analysis & Alerts (Cybersecurity)*

