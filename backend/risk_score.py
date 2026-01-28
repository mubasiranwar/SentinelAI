def calculate_disinfo_risk(
    negative_probability: float,
    emotional_intensity: float,
    repetition_score: float,
    spike_detected: bool
) -> dict:
    """
    Calculates Disinformation Risk Score.
    """

    spike_factor = 1.0 if spike_detected else 0.0

    risk_score = (
        negative_probability
        + emotional_intensity
        + repetition_score
        + spike_factor
    )

    return {
        "risk_score": round(risk_score, 2),
        "level": classify_risk(risk_score)
    }



def classify_risk(score: float) -> str:
    if score >= 3.5:
        return "ACTIVE DISINFORMATION CAMPAIGN"
    elif score >= 2.5:
        return "COORDINATED NARRATIVE"
    elif score >= 1.5:
        return "ELEVATED RISK"
    else:
        return "LOW RISK"


# ----------------------------
# Run test
# ----------------------------
if __name__ == "__main__":
    result = calculate_disinfo_risk(
        negative_probability=0.85,
        emotional_intensity=0.75,
        repetition_score=0.6,
        spike_detected=True
    )

    print(result)
