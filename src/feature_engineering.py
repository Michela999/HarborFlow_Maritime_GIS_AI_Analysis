import pandas as pd
import os

base_path = os.path.join(os.getcwd(), "data", "processed")

traffic = pd.read_csv(os.path.join(base_path, "ais_traffic_export.csv"))
speed = pd.read_csv(os.path.join(base_path, "ais_avg_speed_export.csv"))
maintenance = pd.read_csv(os.path.join(base_path, "maintenance_gaps_export.csv"))
weather = pd.read_csv(os.path.join(base_path, "weather_speed_export.csv"))

# ======================================================
# 1️⃣ TRAFFIC FEATURES
# ======================================================

# Normalize visits (traffic intensity)
traffic["traffic_intensity"] = traffic["visits"] / traffic["visits"].max()

# Flag high traffic vessels
traffic["high_traffic_flag"] = (traffic["traffic_intensity"] > 0.7).astype(int)

# ======================================================
# 2️⃣ SPEED FEATURES
# ======================================================

if "avg_speed_knots" in speed.columns:
    speed["speed_normalized"] = speed["avg_speed_knots"] / speed["avg_speed_knots"].max()

# ======================================================
# 3️⃣ MAINTENANCE FEATURES
# ======================================================

if "maintenance_gap_days" in maintenance.columns:
    maintenance["maintenance_risk"] = (
        maintenance["maintenance_gap_days"] /
        maintenance["maintenance_gap_days"].max()
    )

# ======================================================
# 4️⃣ WEATHER FEATURES
# ======================================================

if "avg_wind_speed" in weather.columns and "avg_precipitation" in weather.columns:
    weather["weather_impact"] = (
        weather["avg_wind_speed"] * 0.7 +
        weather["avg_precipitation"] * 0.3
    )

# ======================================================
# 5️⃣ MERGE ON SHIPNAME (Safe Merge)
# ======================================================

ml_df = traffic.copy()

if "shipname" in speed.columns:
    ml_df = ml_df.merge(speed, on="shipname", how="left")

if "shipname" in weather.columns:
    ml_df = ml_df.merge(weather, on="shipname", how="left")

if "vessel_id" in maintenance.columns:
    # maintenance may not use shipname
    print("Maintenance dataset uses vessel_id. Not merged automatically.")

# ======================================================
# Save ML-ready dataset
# ======================================================

ml_df.to_csv(os.path.join(base_path, "ml_features_dataset.csv"), index=False)

print("✅ ML-ready dataset saved successfully.")