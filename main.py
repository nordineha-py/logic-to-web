from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import random

app = FastAPI()

@app.post("/dah", response_class=PlainTextResponse)
async def reverse_bits(request: Request):
    data = (await request.body()).decode().strip()

    # Ensure exactly 8 characters only 0/1
    if len(data) != 8 or any(c not in "01" for c in data):
        return "00000000"

    reversed_bits = data[::-1]
    return reversed_bits
@app.post('/test/number')
def test(data):
  return 10000000
@app.post('/test/text')
def testt(dataa):
  return "10000000"
@app.post('/test/plaintext')
def testtt(data):
  return PlainTextResponse('1000000')
