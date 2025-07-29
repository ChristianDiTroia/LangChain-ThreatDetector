from langchain_core.messages import SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import json

from models import (
    ThreatAnalysisResponse,
    DangerExtractionResponse,
    SentimentAnalysisResponse,
)


class ThreatAnalyzer:

    # TODO - move these to a config file or similar
    __system_prompts = {
        "sentiment_analysis": SystemMessage(
            "You are an emotion analysis bot. Your job is to perform sentiment analysis on the given text and identify the top 5 emotions present. "
            "Your response should be in the form of a JSON object with a single attribute called 'sentiments' "
            "which contains an array of the top 5 emotions in order from most prevalent to least prevalent. "
            "Each emotion should be an ordered pair of strings with the first element as the emotion and the second "
            "as a rating of the emotion. The rating can only be 'positive', 'neutral', or 'negative'."
        ),
        "action_extraction": SystemMessage(
            "You are a threat analysis bot. Your job is to find every phrase in the given text that may indicate the intent for action, "
            "especially those with intent for harmful action. Return a JSON object with only a single element called 'actions' as a list "
            "containing every phrase fitting this context that is actionable. Be liberal with your analysis, as these can be phrases without verbs."
        ),
        "danger_extraction": SystemMessage(
            "You are a text extraction bot. Your job is to find and extract every word in the given text which may convey danger, violence, or harm. "
            "Only extract these words and return them in the form of a JSON object with a single attribute called "
            "'danger_words' containing an array of the words you have extracted ordered from most to least dangerous/violent/harmful. "
            "This list can be empty if no danger words are found."
        ),
    }

    __templates = {
        "sentiment_analysis": ChatPromptTemplate.from_messages(
            [__system_prompts["sentiment_analysis"], ("user", "{input}")]
        ),
        "action_extraction": ChatPromptTemplate.from_messages(
            [__system_prompts["action_extraction"], ("user", "{input}")]
        ),
        "danger_extraction": ChatPromptTemplate.from_messages(
            [__system_prompts["danger_extraction"], ("user", "{input}")]
        ),
    }

    # TODO - make this configurable such that actual LangChain Models can be passed in
    def __init__(
        self,
        sentiment_analysis_groq_model="llama-3.3-70b-versatile",
        feature_extraction_groq_model="gemma2-9b-it",
    ):
        load_dotenv()

        self.sentiment_analysis_model = ChatGroq(
            model=sentiment_analysis_groq_model,
            model_kwargs={"response_format": {"type": "json_object"}},
        )
        self.feature_extraction_model = ChatGroq(
            model=feature_extraction_groq_model,
            model_kwargs={"response_format": {"type": "json_object"}},
        )

        self.sentiment_pipeline: RunnableSequence = (
            ThreatAnalyzer.__templates["sentiment_analysis"]
            | self.sentiment_analysis_model
            | ThreatAnalyzer.__parse_json_response
        )
        self.extraction_pipeline: RunnableSequence = (
            ThreatAnalyzer.__templates["action_extraction"]
            | self.feature_extraction_model
            | ThreatAnalyzer.__parse_json_response
            | ThreatAnalyzer.__get_action_phrases_from_response
            | ThreatAnalyzer.__templates["danger_extraction"]
            | self.feature_extraction_model
            | ThreatAnalyzer.__parse_json_response
        )

    def full_analysis(self, text: str) -> ThreatAnalysisResponse:
        sentiment_analysis = self.sentiment_pipeline.invoke({"input": text})
        danger_extraction = self.extraction_pipeline.invoke({"input": text})

        negative_sentiments = 0
        for emotion in sentiment_analysis["sentiments"]:
            if emotion[1] == "negative":
                negative_sentiments += 1

        return ThreatAnalysisResponse(
            negative_sentiments=negative_sentiments,
            emotions=sentiment_analysis["sentiments"],
            danger_words=danger_extraction["danger_words"],
        )

    def sentiment_analysis(self, text: str) -> SentimentAnalysisResponse:
        response = self.sentiment_pipeline.invoke({"input": text})
        return SentimentAnalysisResponse(sentiments=response["sentiments"])

    def danger_word_extraction(self, text: str) -> DangerExtractionResponse:
        response = self.extraction_pipeline.invoke({"input": text})
        return DangerExtractionResponse(danger_words=response["danger_words"])

    def __parse_json_response(response: AIMessage) -> dict:
        try:
            return json.loads(response.content)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON response received.")

    def __get_action_phrases_from_response(response: dict) -> str:
        if "actions" in response:
            return ".\n".join(response["actions"])
        elif len(response) > 0:
            return ".\n".join(response.values())
        else:
            raise ValueError("Actionable phrases not found in response.")
