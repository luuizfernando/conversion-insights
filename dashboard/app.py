import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Conversion Insights Dashboard", layout="wide")

model = joblib.load("../models/xgb_model.pkl")
df = pd.read_csv("../data/processed/cleaned_data.csv")
X = df.drop(columns=["revenue"])
y = df["revenue"]
preds = model.predict(X)

st.title("📊 Conversion Insights Dashboard")

st.metric("Total registros", len(df))
st.metric("Conversões", int(y.sum()))
st.metric("Conversão prevista", int(preds.sum()))

st.write("### Dados com previsão")
df_result = df.copy()
df_result["predicted_revenue"] = preds
st.dataframe(df_result.head(50))