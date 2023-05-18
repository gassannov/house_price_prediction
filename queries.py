from inference.inference import inference
from apart_model import ApartModel
import numpy as np


def query_predict(apart: ApartModel):
    input_array = np.array([[
        apart.build_tech,
        apart.floor,
        apart.area,
        apart.rooms,
        apart.balcon,
        apart.metro_dist]])
    output_price = inference(input_array, model_path='models/xgb_model.json')
    return output_price[0]


if __name__ == '__main__':
    query_predict(ApartModel(build_tech=1, floor=1, area=1, rooms=1, balcon=1, metro_dist=1))
