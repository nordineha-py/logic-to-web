from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

def to_8bit_binary(n):
    """Convert number to 8-character binary string."""
    return format(n % 256, "08b")  # keep it as string!

def split_digits(value):
    """Split a two-digit number into tens and ones."""
    tens = value // 10
    ones = value % 10
    return tens, ones

@app.get("/hour_one")
def hour_one():
    now = datetime.now()
    tens, _ = split_digits(now.hour)
    return to_8bit_binary(tens)

@app.get("/hour_two")
def hour_two():
    now = datetime.now()
    _, ones = split_digits(now.hour)
    return to_8bit_binary(ones)

@app.get("/minute_one")
def minute_one():
    now = datetime.now()
    tens, _ = split_digits(now.minute)
    return to_8bit_binary(tens)

@app.get("/minute_two")
def minute_two():
    now = datetime.now()
    _, ones = split_digits(now.minute)
    return to_8bit_binary(ones)
 
