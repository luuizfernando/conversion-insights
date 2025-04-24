# 🧠 Conversion Insights

A complete and interpretable machine learning pipeline for e-commerce conversion prediction, using the **Online Shoppers Intention Dataset**.

---

## 🚀 Project Overview

This project demonstrates how to go from raw data to actionable insights using:

- **Data Preprocessing** with pandas
- **Machine Learning** with XGBoost
- **Explainability** with SHAP
- **Visualization** with Streamlit
- **KPI Analysis** with SQL simulations

---
## 💻 Technologies Used

| Technology     | Purpose                                         |
|----------------|-------------------------------------------------|
| `pandas`       | Data manipulation and cleaning                  |
| `scikit-learn` | Data splitting and evaluation metrics           |
| `xgboost`      | High-performance gradient boosting model        |
| `shap`         | Feature importance and explainability           |
| `matplotlib`   | Visualization (used by SHAP)                    |
| `streamlit`    | Interactive dashboard creation                  |
| `joblib`       | Model persistence                               |
| `pytest`       | Unit testing                                    |
| `SQL`          | Simulated KPI queries                           |

---
## 🔁 Execution Pipeline

### Preprocessing:
`src/data_processing.py` cleans the dataset and saves it as `data/processed/cleaned_data.csv`.

### Model Training:
`src/model_training.py` trains an XGBoost model, evaluates it using metrics, and saves the trained model.

### SHAP Explainability:
`src/shap_explainer.py` generates a feature importance plot based on SHAP values.

### Interactive Dashboard:
`dashboard/app.py` displays metrics and predictions in an interactive interface built with Streamlit.

### Simulated SQL Queries:
`sql/kpi_queries.sql` contains sample queries for KPI analysis, such as conversion rate and visitor behavior.

---

## 🧪 Testing

Run the tests with:

```bash
pytest tests/
```
---
## ▶️ Running the Project
### Install required packages:
```bash
pip install -r requirements.txt
```
---

## Run the full pipeline:
```bash
bash run_all.sh
```
---
