#!/usr/bin/env python
# coding: utf-8

# # HarborFlow – Phase 4: Operational Risk Dashboard & GIS/AI Integration
# 
# **Phase:** 4 – Operational Risk Dashboard & Final Dataset  
# **Date:** 2026-02-24 → 2026-03-07  
# **Status:** ✅ Completed (ArcGIS joins, feature engineering, predictive modeling, KPI tiles, final dataset, Tableau dashboard)
# 
# ---
# 
# ## Overview
# 
# Phase 4 integrated **AIS traffic predictions, maintenance proxies, and weather impact** into a **fleet-level operational risk dashboard**.  
# Key steps:
# 
# - ArcGIS Pro joins for spatial integration
# - Feature engineering and risk score computation
# - Predictive modeling preparation
# - Final dataset creation (`AIS_Tableau_Final_Operational_Enhanced.csv`)
# - KPI tiles, fleet distribution, top 10 high-risk vessels
# - Risk interaction scatter plots
# - Tableau dashboard assembly
# - Exported GIS map: `AIS_HighLowTraffic_Map.png`
# 
# Phase 4 captures the **full workflow from data integration to visualization**, providing actionable operational insights for vessels in the **Port of Livorno**.
# 

# ## 1️⃣ Libraries & Environment Setup

# In[2]:


# -----------------------------
# 1️⃣ Import libraries
# -----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)


# ## 2️⃣ Load Final Phase 4 Dataset 

# In[4]:


# -----------------------------
# 2️⃣ Load final Phase 4 enhanced dataset
# -----------------------------
final_path = r"C:\Users\miche\Documents\HarborFlow_Fresh\data\processed\AIS_Tableau_Final_Operational_Enhanced.csv"
df = pd.read_csv(final_path)
df.head()


# Load the final enhanced dataset that includes traffic prediction, normalized maintenance and weather risk, and operational risk scores.

# ## 3️⃣ Data Checks & Basic Stats

# In[14]:


# Check for missing values
df.isna().sum()

# Quick stats for operational risk
df['operational_risk_score_final'].describe()

# Count of high-risk vessels
df['operational_risk_category_pct'].value_counts()


# Confirm data integrity, missing values, and fleet-level risk distribution. High-risk vessels are highlighted for operational focus.

# ## 4️⃣Compute KPI Metrics (as in Tableau)

# In[15]:


total_fleet = df['shipname'].nunique()
avg_risk = df['operational_risk_score_final'].mean()
max_risk = df['operational_risk_score_final'].max()
high_traffic_vessels = df['predicted_high_traffic'].sum()

print(f"Total Fleet: {total_fleet}")
print(f"Average Operational Risk: {avg_risk:.3f}")
print(f"Maximum Operational Risk: {max_risk:.3f}")
print(f"High Traffic Vessels: {high_traffic_vessels}")


# Fleet-level KPIs calculated programmatically. These match the KPI Tiles displayed in Tableau.

# ## 5️⃣ Prepare Data for Tableau Dashboard

# In[17]:


# Select columns relevant for Tableau visualization
tableau_cols = [
    'shipname', 'vessel_type', 'operational_risk_category_pct', 
    'operational_risk_score_final', 'maintenance_risk_score_norm',
    'predicted_high_traffic', 'weather_risk_score_norm'
]

df_tableau = df[tableau_cols]

# Save final CSV for Tableau
df_tableau_path = r"C:\Users\miche\Documents\HarborFlow_Fresh\data\processed\AIS_Tableau_Final_Operational_Enhanced.csv"
df_tableau.to_csv(df_tableau_path, index=False)
print("✅ Tableau CSV exported:", df_tableau_path)


# Exported a cleaned dataset for Tableau Public to produce KPI Tiles, Fleet Risk Distribution, Top 10 High-Risk Vessels, and Risk Interaction Scatter plots.

# ## 6️⃣ Notes on Maintenance Fields 
# Some maintenance columns may still have missing values due to incomplete historical records. These fields can be augmented with simulated or real maintenance schedules in future phases.

# ## 7️⃣ Summary & Phase 4 Outcome

# | Deliverable                 | Status     |
# | --------------------------- | ---------- |
# | Feature-engineered dataset  | ✅          |
# | ML predictions              | ✅          |
# | Operational risk scoring    | ✅          |
# | Tableau KPI tiles           | ✅          |
# | Fleet Risk Distribution     | ✅          |
# | Top 10 High-Risk Vessels    | ✅          |
# | Risk Interaction Scatter    | ✅          |
# | Maintenance data enrichment | ⚠️ Partial |
# | Dashboard publishing        | ✅          |
# 
