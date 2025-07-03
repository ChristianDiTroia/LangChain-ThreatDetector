from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ThreatDetectionRequest(BaseModel):
    text: str


class ThreatDetectionResponse(BaseModel):
    threat_detected: bool
    emotion: str
    suspicious_text: list[str]
    processed_text: str


@app.get("/")
async def root():
    return {"message": "Welcome to the Threat Detector API"}


@app.post("/detect-threat")
async def detect_threat(data: ThreatDetectionRequest):
    response = ThreatDetectionResponse(
        threat_detected=False,
        emotion="neutral",
        suspicious_text=["Testing123", "Attacking at dawn"],
        processed_text=data.text,
    )
    return response
