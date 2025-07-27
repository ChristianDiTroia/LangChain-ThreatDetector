from fastapi import FastAPI
from pydantic import BaseModel
from ThreatAnalyzer import ThreatAnalyzer

threat_analyzer = ThreatAnalyzer()
app = FastAPI()


class ThreatDetectionRequest(BaseModel):
    text: str


class ThreatDetectionResponse(BaseModel):
    negative_sentiments: int
    emotions: list[str]
    danger_words: list[str]


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Threat Detector API. Post to /detect-threat with {text: str } to analyze text."
    }


@app.post("/detect-threat")
async def detect_threat(data: ThreatDetectionRequest) -> ThreatDetectionResponse:
    analysis = threat_analyzer.perform_analysis(data.text)

    response = ThreatDetectionResponse(
        negative_sentiments=analysis.get_negative_sentiments(),
        emotions=analysis.get_emotions(),
        danger_words=analysis.get_danger_words(),
    )

    return response
