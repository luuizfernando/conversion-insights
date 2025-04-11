import os
import pandas as pd


def load_csv(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    try:
        return pd.read_csv(path)
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar CSV de {path}: {e}")


def save_dataframe(df, path):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        df.to_csv(path, index=False)
        print(f"[INFO] DataFrame salvo em: {path}")
    except Exception as e:
        raise RuntimeError(f"Erro ao salvar DataFrame em {path}: {e}")