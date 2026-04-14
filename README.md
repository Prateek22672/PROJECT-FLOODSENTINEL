# Project Sentinel // v3.0

Project Sentinel is a specialized Neural Network framework designed for urban flood resilience. The system integrates real-time meteorological data with a 24-month hydrological footprint to assess flood risk based on soil saturation, infrastructure capacity, and atmospheric load.

*This project was developed for the Cognizant Hackathon to demonstrate Explainable AI (XAI) in environmental monitoring.*

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/814cf573-750c-4a52-bc63-e8c2e104b6e5" width="800" alt="Sentinel Dashboard Main">
</p>

---

## Technical Overview
The system transitions from traditional binary reporting to a probabilistic model, providing Explainable Intelligence (XAI) by analyzing current environmental variables against historical climate cycles.

### Functional Components
* **Predictive Engine:** A pre-trained machine learning model (Random Forest/XGBoost) that processes 20 distinct environmental features.
* **Temporal Trend Analysis:** Real-time integration of 90-day, 6-month, and 12-month climate archives to determine ground saturation levels.
* **Explainable AI (XAI):** A reasoning module that translates numerical risk indices into technical insights regarding the "Sponge Effect" and infrastructure load.
* **2026 Climate Logic:** Calibrated for the 92% Below Normal monsoon forecast associated with the El Nino cycle.

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/87abfa18-a300-4b1a-84a8-39a46314d59f" width="800" alt="XAI Analysis Section">
</p>

---

## Methodology and Logic
The system operates via a multi-stage analytical pipeline:

### 1. Feature Engineering
Input vectors are constructed using live telemetry:
* **Atmospheric Load:** Relative humidity and temperature gradients.
* **Ground Saturation Index:** Cumulative rainfall sums from the preceding 90-day window.
* **Infrastructure Baseline:** Urban drainage capacity estimated from long-term hydrological activity.

### 2. The Saturation Principle
The model applies a weighted adjustment based on the ground's absorption capacity:
* **Dry/Absorptive State:** High surface infiltration capacity acts as a natural buffer.
* **Saturated State:** Deep-soil moisture at capacity leads to immediate surface runoff and urban inundation.

---

## Technical Stack
| Category | Technologies |
| :--- | :--- |
| **Frontend** | React 18, Vite, Lucide Architecture |
| **Backend** | FastAPI, Uvicorn, Python 3.11 |
| **Intelligence** | Scikit-Learn, Joblib, NumPy, Pandas |
| **Data APIs** | Open-Meteo Forecast and Archive Nodes |

---

## Installation and Deployment

### Backend Initialization
```bash
# Navigate to the project directory
cd backend

# Install required dependencies
pip install -r requirements.txt

# Execute the server
uvicorn main:app --host 127.0.0.1 --port 8000
