from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

def to_8bit_binary(n, bits=8):
    return format(n % (2**bits), f"0{bits}b")

@app.get("/time_hour")
def time_hour():
    now = datetime.now()
    return to_8bit_binary(now.hour)

@app.get("/time_minute")
def time_minute():
    now = datetime.now()
    return to_8bit_binary(now.minute)

@app.get("/time_second")
def time_second():
    now = datetime.now()
    return to_8bit_binary(now.second)

@app.get("/time_hms")
def time_hms():
    now = datetime.now()
    h = format(now.hour % 4, "02b")
    m = format(now.minute % 8, "03b")
    s = format(now.second % 8, "03b")
    return h + m + s  # always 8 chars

