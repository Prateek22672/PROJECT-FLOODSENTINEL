import joblib
import numpy as np

# Load model
model = joblib.load("model/flood_model.pkl")

# Simulated weather data (from weather.py)
weather_data = {
    "temp": 30,
    "humidity": 70
}

# Convert weather → model features
# (simple mapping for now)
# Extract weather
temp = weather_data["temp"]
humidity = weather_data["humidity"]

# Smart mapping (simple logic)
monsoon_intensity = min(max(int(humidity / 10), 1), 10)
climate_change = min(max(int(temp / 5), 1), 10)

# Create feature list dynamically
features = [
    monsoon_intensity,
    5,
    5,
    6,
    5,
    climate_change,
    5,
    5,
    5,
    5,
    5,
    5,
    4,
    4,
    5,
    6,
    5,
    4,
    6,
    5
]

# Convert to array
features_array = np.array(features).reshape(1, -1)

# Predict
prediction = model.predict(features_array)[0]

print("Flood Risk (Auto):", prediction)