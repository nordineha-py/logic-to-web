from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return "API Live"

@app.post("/transmit")
def transmit():
    return "00000000"

@app.get("/time")
def current_time():
    now = datetime.now()
    # HHMMSS00 format
    time_str = now.strftime("%H%M%S") + "00"
    return time_str
