from fastapi import FastAPI
from pydantic import BaseModel
from trying_twilio import call_sleep, call_wake
from fastapi.responses import JSONResponse

app = FastAPI()

class CallRequest(BaseModel):
    callType: str
    number: str

@app.post("/call")
def call_endpoint(req: CallRequest):
    call_type = req.callType.lower()
    number = req.number
    try:
        if call_type == "sleep":
            call_sleep(number)
        elif call_type == "wake":
            call_wake(number)
        else:
            return JSONResponse(content={"status": "error", "message": "Invalid callType"}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)