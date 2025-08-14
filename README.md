# Advanced Flood Susceptibility Mapping for Vellore, India

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.x-orange.svg)
![GIS](https://img.shields.io/badge/GIS-QGIS%20%7C%20GEE-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A comprehensive, data-driven framework for modeling flood susceptibility in the Palar River Basin (Vellore, India) using machine learning, remote sensing, and GIS.



---

## 📝 Overview

This project moves beyond simple thresholding techniques by employing a **Random Forest machine learning model** to predict flood-prone areas. It integrates key hydro-geomorphic factors derived from a high-resolution DEM with historical flood data from Sentinel-1 SAR imagery. The final output is not just a map, but a full **Flood Risk Dossier**, including an exposure analysis that quantifies the risk to critical infrastructure and land use, providing actionable intelligence for disaster management.


***Figure 1: Final Flood Susceptibility Map***

---

## 🚀 Key Features

* **Machine Learning Approach:** Utilizes a Random Forest Classifier for high-accuracy susceptibility prediction.
* **Advanced Feature Engineering:** Incorporates key hydrological parameters like Topographic Wetness Index (TWI) for a scientifically robust model.
* **Multi-Source Data Fusion:** Integrates DEMs, Sentinel-1 SAR, ESA WorldCover, and OpenStreetMap data.
* **Impact Analysis:** Quantifies risk to critical infrastructure (hospitals, schools, roads) and land use types (cropland, urban areas).
* **End-to-End Workflow:** Provides a complete, replicable pipeline from data acquisition to final reporting.

---

## 📂 Repository Structure

```
Flood-Susceptibility-Vellore/
│
├── .gitignore          # Files to be ignored by Git
├── README.md           # This project overview
├── requirements.txt    # Python dependencies
│
├── code/
│   └── train_flood_model.py # Python script for model training
│
├── data/
│   ├── raw/            # -> Place raw downloaded data here
│   ├── processed/      # -> Intermediate, cleaned data
│   └── outputs/        # -> Final outputs (maps, tables, model)
│
└── notebooks/          # -> Jupyter notebooks for exploration (optional)
```

---

## 🛠️ Methodology

The project workflow is divided into four main stages:


***Figure 2: Methodological Workflow***

1.  **Data Acquisition & Pre-processing:**
    * **DEM:** ALOS PALSAR 12.5m DEM was acquired from ASF DAAC.
    * **Ground Truth:** Historical flood extent (Nov-Dec 2023) was mapped using Sentinel-1 SAR in Google Earth Engine.
    * **Ancillary Data:** Land use (ESA WorldCover) and infrastructure (OpenStreetMap) were collected.
    * All data was re-projected to **WGS 84 / UTM Zone 44N** and clipped to the Vellore district boundary.

2.  **Feature Engineering (QGIS):**
    * Five predictor variables were derived from the DEM: **Elevation**, **Slope**, **Aspect**, **Topographic Wetness Index (TWI)**, and **Distance from Rivers**.

3.  **Machine Learning (Python & Scikit-learn):**
    * **Training Data Generation:** 1,000 points (500 flood, 500 no-flood) were sampled.
    * **ETL:** The `Point sampling tool` in QGIS was used to extract feature values at these points, creating the final training matrix.
    * **Model Training:** A Random Forest Classifier was trained on a 70/30 split of the data. The script for this is available at `code/train_flood_model.py`.

4.  **Prediction & Exposure Analysis:**
    * The trained model was used to predict flood probability for every pixel in the study area.
    * The resulting susceptibility map was used to perform an exposure analysis on land use and infrastructure using zonal statistics and spatial queries in QGIS.

---

## 📈 Results & Outputs

### Model Performance

The Random Forest model achieved an **overall accuracy of 92.67%** on the holdout test set.

```
Classification Report:
              precision    recall  f1-score   support

           0       0.92      0.94      0.93       150
           1       0.94      0.91      0.93       150

    accuracy                           0.93       300
```

### Exposure Analysis

The analysis identified significant assets within the "Very High" susceptibility zones.

**Land Use Exposure:**
| Land Use Type | Area at High Risk (Hectares) |
| :--- | :--- |
| Cropland | 1,250 ha |
| Built-up Area | 480 ha |
| Grassland | 620 ha |

**Critical Infrastructure at Risk:**
| Name | Type | Location (Lat, Lon) |
| :--- | :--- | :--- |
| Government Hospital, Ambur | Hospital | 12.78, 78.71 |
| CMC Hospital Vellore | Hospital | 12.92, 79.13 |
| NH 48 Highway Segment | Primary Road | (Line geometry) |

---

## ⚙️ How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/Flood-Susceptibility-Vellore.git](https://github.com/YourUsername/Flood-Susceptibility-Vellore.git)
    cd Flood-Susceptibility-Vellore
    ```

2.  **Set up a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Add Data:**
    * Download the required raw data as per the links in the "Data Acquisition" section.
    * Place the raw DEM, shapefiles, etc., in the `data/raw/` folder.
    * Perform the QGIS-based feature engineering and export the `final_training_data.csv` to `data/processed/`.

4.  **Run the Model:**
    ```bash
    python code/train_flood_model.py
    ```
    This will train the model and save the `flood_susceptibility_model.pkl` file.


