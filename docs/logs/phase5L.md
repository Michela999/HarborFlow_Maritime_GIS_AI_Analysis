# **Phase 5 – AI Anomaly Detection & Fleet Risk Intelligence**

**Date:** 2026-03-07 → 2026-03-18  
**Status:** ✅ Completed (*Anomaly detection, scoring, fleet intelligence dataset, risk prioritization, visual analytics, documentation*)

---

## **Overview**

Phase 5 focused on extending the operational risk framework into an **AI-driven anomaly detection and fleet risk intelligence system**.

This phase introduced **unsupervised machine learning (Isolation Forest)** to identify abnormal vessel behavior and enhance risk monitoring beyond traditional scoring models.

The work included:

* **Anomaly detection using machine learning**
* **Anomaly scoring and classification**
* **Integration with existing risk metrics**
* **Fleet-level intelligence dataset creation**
* **Risk prioritization and advanced visual analysis**

This phase completes the HarborFlow pipeline, transforming it into a **full maritime intelligence workflow from raw data to AI-driven insights**.

---

## **Objectives Achieved**

* **Anomaly Detection (Machine Learning)**

  * Implemented **Isolation Forest model**
  * Selected features:

    * `operational_risk_score_final`
    * `maintenance_risk_score_norm`
    * `weather_risk_score_norm`
    * `predicted_high_traffic`
  * Standardized features using `StandardScaler`
  * Trained model to detect abnormal vessel patterns

* **Anomaly Classification & Scoring**

  * Generated:

    * `anomaly_flag` (0 = normal, 1 = anomaly)
    * `anomaly_score` (continuous score, higher = more anomalous)
  * Converted model outputs into interpretable indicators
  * Verified anomaly distribution across fleet

* **Risk Integration**

  * Combined:

    * Operational risk (Phase 4)
    * Anomaly detection outputs
  * Created **combined_risk_score**
  * Generated **combined_risk_alert categories**:

    * Normal
    * Warning
    * Critical

* **Fleet Intelligence Dataset**

  * Created structured dataset including:

    * Vessel identifiers
    * Risk scores (operational + combined)
    * Anomaly indicators
  * Final dataset:

    ```
    data/processed/fleet_risk_intelligence.csv
    ```

* **Risk Prioritization**

  * Ranked vessels by:

    * `combined_risk_score`
    * `anomaly_score`
  * Identified **high-risk and anomalous vessels**
  * Enabled prioritization for monitoring and decision-making

* **Visual Analysis**

  * Generated plots:

    * Anomaly score distribution
    * Risk vs anomaly scatter plots
    * Correlation heatmap of risk variables
  * Verified relationships between risk components

* **Documentation & Reproducibility**

  * All steps documented in:

    ```
    notebooks/05_anomaly_detection_and_risk_intelligence.ipynb
    ```
  * Notebook includes:

    * Feature preparation
    * Model training
    * Scoring and classification
    * Dataset export
    * Visualization

---

## **Tools & Technologies Used**

* **Python 3.11** – data processing, ML modeling, scoring  
* **Pandas / NumPy** – dataset manipulation  
* **Scikit-learn** – Isolation Forest, StandardScaler  
* **Matplotlib / Seaborn** – visual analysis  
* **Jupyter Notebook** – reproducible workflow  
* **Git / GitHub** – version control and project documentation  

---

## **Data Sources & Outputs**

| Dataset              | Source                                  | Records | Processed Output                        | Notes                                  |
|---------------------|------------------------------------------|--------|----------------------------------------|----------------------------------------|
| Phase 4 Dataset     | Operational enhanced dataset             | 94     | Used as input                          | Includes all risk features             |
| Anomaly Features    | Derived                                 | 94     | Scaled feature matrix                  | Used for ML model                      |
| Phase 5 Final       | Combined                                | 94     | `fleet_risk_intelligence.csv`          | Final AI-enhanced dataset              |

---

## **Phase 5 Results**

* Isolation Forest model successfully implemented and validated  
* Anomaly detection integrated with operational risk framework  
* Combined risk scoring system created  
* Fleet-level intelligence dataset generated  
* High-risk and anomalous vessels identified  
* Visual analytics confirm relationships between variables  
* Fully reproducible notebook and outputs completed  

---

## **Final Outcome**

With Phase 5 completed, HarborFlow now delivers:

* End-to-end maritime data pipeline  
* Multi-factor risk modeling  
* AI-driven anomaly detection  
* Fleet-level risk intelligence  

This phase represents the transition from **descriptive analytics to intelligent, data-driven decision support** in a maritime context.

---

**Project Status:** ✅ Fully Completed  