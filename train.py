import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Load dataset
df = pd.read_csv("data/flood_data.csv")

# Split features and target
X = df.drop("FloodProbability", axis=1)
y = df["FloodProbability"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = XGBRegressor()

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)

joblib.dump(model, "model/flood_model.pkl")

print("Model saved successfully!")