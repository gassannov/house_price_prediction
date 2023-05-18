import numpy as np
import pickle as pkl
import xgboost as xgb


def inference(X: np.array, model_path: str):
    model = xgb.XGBRegressor()
    model.load_model(model_path)

    return model.predict(X)
