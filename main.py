from fastapi import FastAPI, Request
from datetime import datetime
from typing import Tuple

app = FastAPI()

def to_8bit_binary(n: int) -> str:
    """Return an 8-character binary string for integer n (0-255)."""
    return format(n % 256, "08b")

def split_digits(value: int) -> Tuple[int, int]:
    """Split a two-digit number into (tens, ones)."""
    return value // 10, value % 10

# Optional root so you can visit in browser (GET) and see server is up
@app.get("/")
def root():
    now = datetime.now().strftime("%H:%M:%S")
    return {"value": f"API Live - {now}"}

# All endpoints accept POST (Build Logic sends POSTs)
@app.post("/hour_one")
async def hour_one(request: Request):
    await request.body()  # consume POST body (ignored)
    tens, _ = split_digits(datetime.now().hour)
    return {"value": to_8bit_binary(tens)}

@app.post("/hour_two")
async def hour_two(request: Request):
    await request.body()
    _, ones = split_digits(datetime.now().hour)
    return {"value": to_8bit_binary(ones)}

@app.post("/minute_one")
async def minute_one(request: Request):
    await request.body()
    tens, _ = split_digits(datetime.now().minute)
    return {"value": to_8bit_binary(tens)}

@app.post("/minute_two")
async def minute_two(request: Request):
    await request.body()
    _, ones = split_digits(datetime.now().minute)
    return {"value": to_8bit_binary(ones)}

@app.post("/second_one")
async def second_one(request: Request):
    await request.body()
    tens, _ = split_digits(datetime.now().second)
    return {"value": to_8bit_binary(tens)}

@app.post("/second_two")
async def second_two(request: Request):
    await request.body()
    _, ones = split_digits(datetime.now().second)
    return {"value": to_8bit_binary(ones)}

@app.post("/time_hms")
async def time_hms(request: Request):
    """
    Compressed 8-bit pattern: 2 bits hours%4 | 3 bits minutes%8 | 3 bits seconds%8
    (always returns 8 chars)
    """
    await request.body()
    now = datetime.now()
    h = format(now.hour % 4, "02b")
    m = format(now.minute % 8, "03b")
    s = format(now.second % 8, "03b")
    return {"value": h + m + s}
