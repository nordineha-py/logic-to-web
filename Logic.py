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
    # compress HHMMSS into 8 bits (example: HH % 4, MM % 4, SS % 4)
    h = now.hour % 4
    m = now.minute % 4
    s = now.second % 4
    return format(h, "02b") + format(m, "03b") + format(s, "03b")
