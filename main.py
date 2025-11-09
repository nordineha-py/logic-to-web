from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

def to_8bit_binary(n):
    return format(n % 256, "08b")

def split_digits(value):
    return value // 10, value % 10

@app.get("/hour_tens")
def hour_tens():
    now = datetime.now()
    tens, _ = split_digits(now.hour)
    return {"value": to_8bit_binary(tens)}

@app.get("/hour_ones")
def hour_ones():
    now = datetime.now()
    _, ones = split_digits(now.hour)
    return {"value": to_8bit_binary(ones)}

@app.get("/minute_tens")
def minute_tens():
    now = datetime.now()
    tens, _ = split_digits(now.minute)
    return {"value": to_8bit_binary(tens)}

@app.get("/minute_ones")
def minute_ones():
    now = datetime.now()
    _, ones = split_digits(now.minute)
    return {"value": to_8bit_binary(ones)}

@app.get("/second_tens")
def second_tens():
    now = datetime.now()
    tens, _ = split_digits(now.second)
    return {"value": to_8bit_binary(tens)}

@app.get("/second_ones")
def second_ones():
    now = datetime.now()
    _, ones = split_digits(now.second)
    return {"value": to_8bit_binary(ones)}

