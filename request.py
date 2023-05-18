import requests
import json


if __name__ == '__main__':
    input_dict = {
        'build_tech': 1,
        'floor': 1,
        'area': 1,
        'rooms': 1,
        'balcon': 1,
        'metro_dist': 1
    }
    resp = requests.post('http://127.0.0.1:8000/predict/', data=json.dumps(input_dict))
    print(resp.json())
