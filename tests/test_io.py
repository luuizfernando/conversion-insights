import pytest
import pandas as pd
import os
from src.utils.io import load_csv, save_dataframe

def test_load_csv():
    # Teste com um arquivo que existe
    df = load_csv("data/processed/cleaned_data.csv")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

    # Teste com um arquivo que não existe
    with pytest.raises(FileNotFoundError):
        load_csv("arquivo_inexistente.csv")

def test_save_dataframe():
    # Criar um DataFrame de teste
    df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
    
    # Testar salvamento
    test_path = "data/test/test_output.csv"
    save_dataframe(df, test_path)
    
    # Verificar se o arquivo foi criado
    assert os.path.exists(test_path)
    
    # Limpar
    if os.path.exists(test_path):
        os.remove(test_path)
        os.rmdir(os.path.dirname(test_path)) 