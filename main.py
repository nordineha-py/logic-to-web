from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Store current values
current_values = {"A": 0, "B": 0, "op": "+"}

def to_8bit_binary(n: int) -> str:
    """Convert number to 8-bit binary string, clamp 0-255"""
    return format(max(0, min(255, n)), "08b")

# POST /A - set A
@app.post("/A")
async def set_A(request: Request):
    data = (await request.body()).decode().strip()
    try:
        current_values["A"] = int(data, 2)
    except ValueError:
        current_values["A"] = 0
    return {"value": to_8bit_binary(current_values["A"])}

# POST /operation - set operation
@app.post("/operation")
async def set_operation(request: Request):
    data = (await request.body()).decode().strip()
    mapping = {
        "00000001": "+",
        "00000010": "-",
        "00000100": "*",
        "00001000": "/"
    }
    current_values["op"] = mapping.get(data, "+")
    return {"value": data}  # Echo back the operation signal

# POST /B - set B and calculate result
@app.post("/B")
async def set_B(request: Request):
    data = (await request.body()).decode().strip()
    try:
        current_values["B"] = int(data, 2)
    except ValueError:
        current_values["B"] = 0

    a = current_values["A"]
    b = current_values["B"]
    op = current_values["op"]

    try:
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a // b if b != 0 else 0
        else:
            result = 0
    except:
        result = 0

    return {"value": to_8bit_binary(result)}
