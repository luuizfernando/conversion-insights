import pytest
import matplotlib.pyplot as plt
import os
from src.utils.plotting import salvar_figura, setup_plot_style

def test_setup_plot_style():
    # Testa se o estilo é configurado corretamente
    setup_plot_style()
    assert plt.style.available  # Verifica se há estilos disponíveis

def test_salvar_figura():
    # Cria uma figura de teste
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3])
    
    # Define o caminho para salvar
    test_path = "reports/test/test_plot.png"
    
    # Testa o salvamento
    salvar_figura(fig, test_path)
    
    # Verifica se o arquivo foi criado
    assert os.path.exists(test_path)
    
    # Limpa
    plt.close(fig)
    if os.path.exists(test_path):
        os.remove(test_path)
        os.rmdir(os.path.dirname(test_path)) 