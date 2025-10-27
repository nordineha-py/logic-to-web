from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse

app = FastAPI()

stored_value = "00000000"

@app.post("/transmit")
async def receive(value: str = Form(...)):
    global stored_value
    stored_value = value
    print(f"Received from Build Logic: {stored_value}")
    return PlainTextResponse(stored_value)

@app.get("/receive")
async def send():
    return PlainTextResponse(stored_value)
