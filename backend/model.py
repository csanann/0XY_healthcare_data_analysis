#/0XY_healthcare_data_analysis/backend/model.py

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score import pickle
from backend.data_loading import load_data

def train_model(data_path):
    
    X_train, X_val, y_train, y_val = load_data(data_path)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    r2 = r2_score(y_val, y_pred)
    mse = mean_squared_error(y_val, y_pred)
    return model, r2, mse
    
def predict(model, X):
    return model.predict(X)

def load_model(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def save_model(model, model_path):
    with open(model_path, 'wb') as f:
        pickle.dump(model,f)