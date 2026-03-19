#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import os

# -------------------------------
# Output path
# -------------------------------
OUTPUT_FOLDER = "../data/raw/maintenance/"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "maintenance_proxy.csv")

# -------------------------------
# Create proxy dataset
# -------------------------------
data = {
    "vessel_id": ["V001", "V002", "V003", "V004", "V005"],
    "vessel_type": ["Cargo", "Tanker", "Passenger", "Cargo", "Tanker"],
    "last_maintenance": ["2023-09-15", "2023-09-10", "2023-09-12", "2023-09-20", "2023-09-18"],
    "maintenance_type": ["Engine", "Hull", "Navigation", "Engine", "Hull"],
    "hours_since_last": [120, 300, 80, 50, 200],
    "next_due_hours": [500, 600, 400, 500, 600],
    "port": ["Livorno", "Genoa", "Livorno", "Marseille", "Genoa"]
}

# Create DataFrame
maint_df = pd.DataFrame(data)

# -------------------------------
# Save CSV
# -------------------------------
maint_df.to_csv(OUTPUT_FILE, index=False)

print(f"✅ Maintenance proxy CSV saved at: {OUTPUT_FILE}")


# In[ ]:




