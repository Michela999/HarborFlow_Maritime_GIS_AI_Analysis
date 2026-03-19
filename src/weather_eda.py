#!/usr/bin/env python
# coding: utf-8

# In[5]:


# ==================================================
# HarborFlow – Phase 1 Weather Data Exploration
# ==================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --------------------------------------------------
# Paths (relative to notebooks/)
# --------------------------------------------------
DATA_PATH = "../data/raw/weather/weather_openmeteo_livorno_oct2023.csv"
OUTPUT_PATH = "../docs/screens/phase1/"
os.makedirs(OUTPUT_PATH, exist_ok=True)

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# --------------------------------------------------
# Load raw weather data
# --------------------------------------------------
weather_df = pd.read_csv(DATA_PATH)
print("Dataset shape:", weather_df.shape)
display(weather_df.head())

# --------------------------------------------------
# Inspect columns and data
# --------------------------------------------------
print("\nColumn names:")
display(weather_df.columns)

print("\nData types & non-null counts:")
weather_df.info()

print("\nMissing values per column:")
display(weather_df.isna().sum())

print("\nSummary statistics:")
display(weather_df.describe())

# --------------------------------------------------
# Time handling (index)
# --------------------------------------------------
weather_df["time"] = pd.to_datetime(weather_df["time"])
weather_df.set_index("time", inplace=True)

# --------------------------------------------------
# Temperature (2m above ground)
# --------------------------------------------------
plt.figure()
sns.lineplot(x=weather_df.index, y=weather_df["temperature_2m"])
plt.title("Air Temperature at 2m – Livorno (Oct 2023)")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.savefig(f"{OUTPUT_PATH}weather_temperature_2m_timeseries.png")
plt.close()

# --------------------------------------------------
# Wind speed (10m above ground)
# --------------------------------------------------
plt.figure()
sns.lineplot(x=weather_df.index, y=weather_df["wind_speed_10m"])
plt.title("Wind Speed at 10m – Livorno (Oct 2023)")
plt.xlabel("Date")
plt.ylabel("Wind Speed (m/s)")
plt.tight_layout()
plt.savefig(f"{OUTPUT_PATH}weather_wind_speed_10m_timeseries.png")
plt.close()

# --------------------------------------------------
# Wind direction (10m)
# --------------------------------------------------
plt.figure()
sns.histplot(weather_df["wind_direction_10m"], bins=36)
plt.title("Wind Direction Distribution – Livorno (Oct 2023)")
plt.xlabel("Degrees (0-360)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(f"{OUTPUT_PATH}weather_wind_direction_10m_histogram.png")
plt.close()

# --------------------------------------------------
# Surface pressure
# --------------------------------------------------
plt.figure()
sns.lineplot(x=weather_df.index, y=weather_df["surface_pressure"])
plt.title("Surface Pressure – Livorno (Oct 2023)")
plt.xlabel("Date")
plt.ylabel("Pressure (hPa)")
plt.tight_layout()
plt.savefig(f"{OUTPUT_PATH}weather_surface_pressure_timeseries.png")
plt.close()

# --------------------------------------------------
# Precipitation
# --------------------------------------------------
plt.figure()
sns.lineplot(x=weather_df.index, y=weather_df["precipitation"])
plt.title("Precipitation – Livorno (Oct 2023)")
plt.xlabel("Date")
plt.ylabel("Precipitation (mm)")
plt.tight_layout()
plt.savefig(f"{OUTPUT_PATH}weather_precipitation_timeseries.png")
plt.close()

# --------------------------------------------------
# Optional: quick observations (Phase 1 pre-cleaning)
# --------------------------------------------------
print("✅ Phase 1 Weather EDA completed successfully.")
print("Observations:")
print("- Temperature ranges ~13.3°C to 27.7°C")
print("- Wind speed ranges 0.5 to 47.5 m/s (strong gusts possible)")
print("- Wind direction spans full 0-360 degrees")
print("- Surface pressure mostly 991–1025 hPa")
print("- Precipitation is sparse, mostly 0 mm, occasional spikes up to 11.7 mm")


# In[ ]:




