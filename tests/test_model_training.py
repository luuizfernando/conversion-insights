import pytest
import pandas as pd
from src import model_training

def test_load_data():
    df = model_training.load_data("data/processed/cleaned_data.csv")
    assert not df.empty

def test_train_model():
    df = model_training.load_data("data/processed/cleaned_data.csv")
    X_train, X_test, y_train, y_test = model_training.split_data(df)
    model = model_training.train_model(X_train, y_train)
    assert model is not None