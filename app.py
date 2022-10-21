from preprocessing.cleaning_data import Cleaning
from fastapi import FastAPI, Body
from predict.prediction import Prediction
from typing import Union
from pydantic import BaseModel
import json
import os


# self = Prediction()
# self = self.predict()

class Properties(BaseModel):
    """Properties of the real estate"""
    area: int
    property_type: str
    rooms_number: int
    zip_code: int
    land_area: Union[int, None] = None
    garden: Union[bool, None] = None
    garden_area: Union[int, None] = None
    equipped_kitchen: Union[bool, None] = None
    full_address: Union[str, None] = None
    swimming_pool: Union[bool, None] = None
    furnished: Union[bool, None] = None
    open_fire: Union[bool, None] = None
    terrace: Union[bool, None] = None
    terrace_area: Union[int, None] = None
    facades_number: Union[int, None] = None
    building_state: Union[str, None] = None

# f = open ('test_app.json')
# y = json.load(f)
# json_file = y
# print(Prediction().predict(json_file))

PORT = os.environ.get("PORT", 9000)
app = FastAPI(port=PORT)

@app.get("/")
def read_root():
    return {"message": "Alive"}

@app.post("/prediction/")
async def real_estate_propreties( data : Properties=Body(embed=True)):
    json_file = data.dict()
    prediction = Prediction().predict(json_file)
    print(prediction)
    return prediction

    






