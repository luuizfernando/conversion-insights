import os
import matplotlib.pyplot as plt

def salvar_figura(fig, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path)
    print(f"[INFO] Figura salva em: {path}")

def setup_plot_style():
    plt.style.use("seaborn-v0_8")