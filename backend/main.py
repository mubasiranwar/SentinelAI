from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd

from utils import clean_text
from sentiment import analyze_text
from spike_detector import detect_sentiment_spike
from narrative import detect_repeated_narratives
from risk_score import calculate_disinfo_risk


app = FastAPI(title="SentinelAI API")

# ----------------------------
# Request Model
# ----------------------------

class Post(BaseModel):
    text: str
    timestamp: str


# ----------------------------
# API Endpoint
# ----------------------------

@app.post("/analyze")
def analyze_posts(posts: List[Post]):

    # Clean text
    texts = [clean_text(p.text) for p in posts]

    # Sentiment & emotion
    analysis_results = [analyze_text(t) for t in texts]

    # Prepare DataFrame for spike detection
    df = pd.DataFrame({
        "timestamp": [p.timestamp for p in posts],
        "negative_probability": [r["negative_probability"] for r in analysis_results]
    })

    spikes = detect_sentiment_spike(df)
    spike_detected = len(spikes) > 0

    # Narrative repetition
    _, repetition_score = detect_repeated_narratives(texts)

    # Risk score (aggregate average)
    avg_negative = sum(r["negative_probability"] for r in analysis_results) / len(analysis_results)
    avg_intensity = sum(r["emotional_intensity"] for r in analysis_results) / len(analysis_results)

    risk = calculate_disinfo_risk(
        negative_probability=avg_negative,
        emotional_intensity=avg_intensity,
        repetition_score=repetition_score,
        spike_detected=spike_detected
    )

    return {
        "posts_analyzed": len(posts),
        "risk": risk,
        "spike_detected": spike_detected,
        "repetition_score": repetition_score,
        "details": analysis_results
    }
