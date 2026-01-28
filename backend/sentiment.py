from transformers import pipeline
import numpy as np
from utils import clean_text


# ----------------------------
# Load pretrained models
# ----------------------------

# Sentiment analysis model
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Emotion detection model
emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)


# ----------------------------
# Sentiment Analysis Function
# ----------------------------

def analyze_sentiment(text: str) -> dict:
    """
    Returns negative sentiment probability and label
    """
    result = sentiment_model(text)[0]

    label = result["label"]
    score = result["score"]

    negative_prob = score if label == "NEGATIVE" else 1 - score

    return {
        "label": label,
        "negative_probability": round(negative_prob, 3)
    }


# ----------------------------
# Emotion Detection Function
# ----------------------------

def analyze_emotion(text: str) -> dict:
    """
    Returns dominant emotion and emotional intensity
    """
    results = emotion_model(text)[0]

    # Find top emotion
    top_emotion = max(results, key=lambda x: x["score"])

    return {
        "emotion": top_emotion["label"],
        "intensity": round(top_emotion["score"], 3)
    }


# ----------------------------
# Combined Analysis
# ----------------------------

def analyze_text(text: str) -> dict:
    sentiment = analyze_sentiment(text)
    emotion = analyze_emotion(text)

    return {
        "text": text,
        "negative_probability": sentiment["negative_probability"],
        "emotion": emotion["emotion"],
        "emotional_intensity": emotion["intensity"]
    }


# ----------------------------
# Run test
# ----------------------------

if __name__ == "__main__":
    test_text = "The government is hiding the truth and people should be afraid"
    result = analyze_text(test_text)
    print(result)
