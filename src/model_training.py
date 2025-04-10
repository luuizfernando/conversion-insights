import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from xgboost import XGBClassifier

PROCESSED_DATA = "data/processed/cleaned_data.csv"
MODEL_PATH = "models/xgb_model.pkl"

def load_data(path):
    return pd.read_csv(path)

def split_data(df):
    X = df.drop(columns=["revenue"])
    y = df["revenue"]
    return train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

def train_model(X_train, y_train):
    model = XGBClassifier(n_estimators=100, max_depth=4, learning_rate=0.1, use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    print("[INFO] Confusion Matrix:\n", confusion_matrix(y_test, preds))
    print("[INFO] Classification Report:\n", classification_report(y_test, preds))

def save_model(model, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)
    print(f"[INFO] Modelo salvo em: {path}")

def main():
    df = load_data(PROCESSED_DATA)
    X_train, X_test, y_train, y_test = split_data(df)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model, MODEL_PATH)

if __name__ == "__main__":
    main()