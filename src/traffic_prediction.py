import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import xgboost as xgb
import os

# Paths
base_path = os.path.join(os.getcwd(), "..", "data", "processed")
input_file = os.path.join(base_path, "ml_features_dataset.csv")
output_file = os.path.join(base_path, "ml_predictions.csv")

# Load dataset
df = pd.read_csv(input_file)

# Select features (skip IDs / non-numeric)
features = ['traffic_intensity', 'speed_normalized', 'weather_impact']
df_features = df[features]
target = df['high_traffic_flag']

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(
    df_features, target, test_size=0.2, random_state=42
)

# Train XGBoost classifier
model = xgb.XGBClassifier(
    n_estimators=100,
    max_depth=3,
    learning_rate=0.1,
    use_label_encoder=False,
    eval_metric='logloss',
    random_state=42
)
model.fit(X_train, y_train)

# Predict on full dataset
df['predicted_high_traffic'] = model.predict(df_features)

# Evaluate on test set
y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save predictions for GIS/dashboard use
df.to_csv(output_file, index=False)
print(f"✅ Predictions saved to {output_file}")
