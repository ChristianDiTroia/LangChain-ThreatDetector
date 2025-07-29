from pydantic import BaseModel


class ThreatDetectionRequest(BaseModel):
    text: str


class SentimentAnalysisResponse(BaseModel):
    sentiments: list[tuple[str, str]]


class DangerExtractionResponse(BaseModel):
    danger_words: list[str]


class ThreatAnalysisResponse(BaseModel):
    negative_sentiments: int
    emotions: list[tuple[str, str]]
    danger_words: list[str]
