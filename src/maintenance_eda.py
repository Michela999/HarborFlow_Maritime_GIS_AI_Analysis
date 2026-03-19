#!/usr/bin/env python
# coding: utf-8

# In[4]:


# ==================================================
# HarborFlow – Phase 1 Maintenance Proxy EDA
# ==================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --------------------------------------------------
# Paths
# --------------------------------------------------
DATA_PATH = "data/raw/maintenance/maintenance_proxy.csv"
OUTPUT_PATH = "docs/screens/phase1/"
os.makedirs(OUTPUT_PATH, exist_ok=True)
print(f"Output folder ready at: {OUTPUT_PATH}")

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12,6)

# --------------------------------------------------
# Load CSV
# --------------------------------------------------
try:
    maint_df = pd.read_csv(DATA_PATH)
    print("✅ Maintenance CSV loaded successfully!")
except FileNotFoundError:
    print(f"❌ CSV not found! Check the path: {DATA_PATH}")
    raise

display(maint_df.head())

# --------------------------------------------------
# Inspect structure
# --------------------------------------------------
print("\nColumn names:")
display(maint_df.columns)

print("\nData types & non-null counts:")
maint_df.info()

print("\nMissing values per column:")
display(maint_df.isna().sum())

print("\nSummary statistics (numeric columns):")
display(maint_df.describe())

# --------------------------------------------------
# Convert date column for plotting
# --------------------------------------------------
maint_df["last_maintenance"] = pd.to_datetime(maint_df["last_maintenance"])

# --------------------------------------------------
# Phase 1 visualizations (pre-cleaning)
# --------------------------------------------------

# 1. Vessel type counts
plt.figure()
sns.countplot(x="vessel_type", data=maint_df)
plt.title("Vessel Type Frequency")
plt.xlabel("Vessel Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "maintenance_vessel_type_count.png"))
plt.close()

# 2. Maintenance type counts
plt.figure()
sns.countplot(x="maintenance_type", data=maint_df)
plt.title("Maintenance Type Frequency")
plt.xlabel("Maintenance Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "maintenance_type_count.png"))
plt.close()

# 3. Hours since last maintenance
plt.figure()
sns.histplot(maint_df["hours_since_last"], bins=10, kde=True)
plt.title("Hours Since Last Maintenance")
plt.xlabel("Hours")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "maintenance_hours_since_last.png"))
plt.close()

# 4. Next due maintenance hours
plt.figure()
sns.histplot(maint_df["next_due_hours"], bins=10, kde=True)
plt.title("Next Due Maintenance Hours")
plt.xlabel("Hours")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "maintenance_next_due_hours.png"))
plt.close()

# --------------------------------------------------
# Quick Phase 1 observations
# --------------------------------------------------
print("✅ Phase 1 Maintenance EDA completed successfully.")
print("Observations:")
print("- Vessel types: Cargo, Tanker, Passenger")
print("- Maintenance types: Engine, Hull, Navigation")
print("- Hours since last maintenance vary from 50 to 300")
print("- Next due maintenance mostly between 400-600 hours")


# In[ ]:




