from fastapi import FastAPI, Request # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from pydantic import BaseModel # type: ignore
import mysql.connector # type: ignore
from traffic_model import predict_congestion
from db_config import get_connection

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class TrafficInput(BaseModel):
    vehicle_count: int
    time_of_day: str

@app.post("/predict")
def predict(data: TrafficInput):
    vehicle_count = data.vehicle_count
    time_of_day = data.time_of_day

    prediction = predict_congestion(vehicle_count, time_of_day)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO traffic_logs (vehicle_count, time_of_day, prediction) VALUES (%s, %s, %s)",
        (vehicle_count, time_of_day, prediction)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return {"prediction": prediction}

@app.get("/logs")
def get_logs():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM traffic_logs ORDER BY id DESC")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

