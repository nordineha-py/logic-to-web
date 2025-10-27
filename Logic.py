from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/transmit")
def transmit():
    # Always return exactly the 8-character pattern
    return 10000001
