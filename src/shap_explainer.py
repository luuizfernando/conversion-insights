import pandas as pd
import joblib
import shap
import os

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print("[WARNING] matplotlib não encontrado. Instale com `pip install matplotlib` para gerar gráficos SHAP.")
    plt = None

MODEL_PATH = "models/xgb_model.pkl"
DATA_PATH = "data/processed/cleaned_data.csv"

model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATA_PATH)
X = df.drop(columns=["revenue"])

explainer = shap.Explainer(model)
shap_values = explainer(X)

if plt:
    shap.summary_plot(shap_values, X, show=False)
    os.makedirs("reports", exist_ok=True)
    plt.savefig("reports/shap_summary_plot.png")
    print("[INFO] SHAP summary plot salvo em reports/")
else:
    print("[INFO] SHAP valores calculados, mas matplotlib ausente para gerar o gráfico.")
