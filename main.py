import dataclasses
import sys

from fastapi import FastAPI
import uvicorn
from apart_model import ApartModel
from queries import query_predict
import logging

app = FastAPI()

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.post('/predict/')
async def get_predict(input_item: ApartModel):
    print(f'received {input_item}')
    response = query_predict(input_item)
    response = float(response)
    print(response)
    return response


if __name__ == '__main__':
    uvicorn.run('main:app', port=8090, reload=True)
