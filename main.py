from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/dah", response_class=PlainTextResponse)
async def reverse_bits(request: Request):
    data = (await request.body()).decode().strip()
    if len(data) != 8 or any(c not in "01" for c in data):
        return "00000000"
    return data[::-1]

@app.post("/test/number")
async def test_number(request: Request):
    await request.body()
    return 10000000    # numeric JSON response

@app.post("/test/text")
async def test_text(request: Request):
    await request.body()
    return "10000000"  # JSON string response

@app.post("/test/plaintext")
async def test_plaintext(request: Request):
    await request.body()
    # Explicit PlainTextResponse object returned
    return PlainTextResponse("10000000")
