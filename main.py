from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

sensors = {}

class SensorData(BaseModel):
    id: str
    temperature: float
    humidity: float

@app.post("/sensor")
def post_sensor(data: SensorData):
    sensors[data.id] = {
        "temperature": data.temperature,
        "humidity": data.humidity
    }
    return {"status": "ok"}

@app.get("/sensor/{sensor_id}")
def get_sensor(sensor_id: str):
    if sensor_id in sensors:
        return sensors[sensor_id]
    return {"error": "Sensor not found"}
