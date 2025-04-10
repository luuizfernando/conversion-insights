import pandas as pd
import os
from sklearn.preprocessing import StandardScaler, LabelEncoder

RAW_PATH = "data/raw/online_shoppers_intention.csv"
PROCESSED_PATH = "data/processed/cleaned_data.csv"

def load_raw_data(path):
    df = pd.read_csv(path)
    return df

def clean_columns(df):
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    print("[DEBUG] Colunas após renomeação:", df.columns.tolist())
    return df

def encode_categoricals(df):
    label_cols = ['month', 'visitortype', 'weekend']
    for col in label_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
    return df

def scale_numerics(df):
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    print("[DEBUG] Colunas numéricas:", numeric_cols.tolist())
    
    if 'revenue' in numeric_cols:
        numeric_cols = numeric_cols.drop('revenue')
    
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df

def preprocess_and_save():
    if not os.path.exists("data/processed"):
        os.makedirs("data/processed")

    df = load_raw_data(RAW_PATH)
    df = clean_columns(df)
    df = encode_categoricals(df)
    df = scale_numerics(df)

    df.to_csv(PROCESSED_PATH, index=False)
    print(f"[INFO] Dados processados salvos em: {PROCESSED_PATH}")

if __name__ == "__main__":
    preprocess_and_save()