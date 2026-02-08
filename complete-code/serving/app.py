import random, mlflow
from fastapi import FastAPI
from pydantic import BaseModel

CANARY_RATIO = 0.1

prod = mlflow.pyfunc.load_model("models:/iris-classifier/Production")
shadow = mlflow.pyfunc.load_model("models:/iris-classifier/Shadow")

app = FastAPI()

class Item(BaseModel):
    features: list

@app.post("/predict")
def predict(item: Item):
    if random.random() < CANARY_RATIO:
        return shadow.predict([item.features])[0]
    return prod.predict([item.features])[0]
