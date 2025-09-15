from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ThreatAnalyzer import ThreatAnalyzer
from models import *

threat_analyzer = ThreatAnalyzer()
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Threat Detector API. Post to /detect-threat with body {text: str } to analyze text."
    }


@app.post("/threat-analysis", response_model=ThreatAnalysisResponse)
async def detect_threat(data: ThreatDetectionRequest) -> ThreatAnalysisResponse:
    print("Processing request: ", data.text)
    response = threat_analyzer.full_analysis(data.text)
    return response


@app.post("/sentiment-analysis", response_model=SentimentAnalysisResponse)
async def sentiment_analysis(data: ThreatDetectionRequest) -> SentimentAnalysisResponse:
    response = threat_analyzer.sentiment_analysis(data.text)
    return response


@app.post("/danger-word-extraction", response_model=DangerExtractionResponse)
async def danger_word_extraction(
    data: ThreatDetectionRequest,
) -> DangerExtractionResponse:
    response = threat_analyzer.danger_word_extraction(data.text)
    return response
