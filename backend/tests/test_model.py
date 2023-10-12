# /0XY_healthcare_data_analysis/backend/tests/test_model.py

import os
import pandas as pd
import numpy as np
import pytest
from backend.model import train_model, predict, save_model, load_model
from sklearn.linear_model import LinearRegression

X_train_sample = pd.DataFrame({'feature1':[1, 2, 3, 4, 5], 'feature2': [0.1, 0.2, 0.3, 0.4, 0.5]})
y_train_sample = pd.Series([0.5, 0.7, 0.9, 1.1, 1.3])
X_val_sample = pd.DataFrame({'feature1': [6, 7, 8, 9, 10], 'feature2': [0.6, 0.7, 0.8, 0.9, 1.0]})
y_val_sample = pd.Series([1.5, 1.7, 1.9, 2.1, 2.3])

def test_train_model():
    model, r2, mse = train_model(X_train_sample, y_train_sample, X_val_sample, y_val_sample)
    
    assert isinstance(model, LinearRegression)
    assert 0 <= r2 <= 1 #is r2 in the accepatable range?
    assert mse >= 0 #is mse non negative value?
    
def test_predict():
    model = LinearRegression()
    model.fit(X_train_sample, y_train_sample)
    y_pred = predict(model, X_val_sample)
    
    assert y_pred.shape == y_val_sample.shape
    
def test_save_and_load_model(tmp_path):
    model, _, _ = train_model(X_train_sample, y_train_sample, X_val_sample, y_val_sample)
    model_path = os.path.join(tmp_path, 'test_model.pkl')
    
    save_model(model, model_path)
    loaded_model = load_model(model_path)
    
    assert isinstance(loaded_model, LinearRegression)
    assert model.coef_.all() == loaded_model.coef_.all()
    assert model.intercept_ == loaded_model.intercept_
    
if __name__ == "__main__":
    pytest.main([__file__])
    
    