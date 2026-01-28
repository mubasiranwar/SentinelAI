import pandas as pd

def detect_sentiment_spike(df: pd.DataFrame, window_size="10min", spike_threshold=1.5):
    """
    Detects abnormal spikes in negative sentiment over time.
    """

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    rolling_avg = (
        df.set_index("timestamp")
        .rolling(window_size)["negative_probability"]
        .mean()
    )

    baseline = df["negative_probability"].mean()

    spikes = rolling_avg[rolling_avg > baseline * spike_threshold]

    return spikes.reset_index()


if __name__ == "__main__":
    data = {
        "timestamp": [
            "2024-08-01 10:00", "2024-08-01 10:01", "2024-08-01 10:02",
            "2024-08-01 10:10", "2024-08-01 10:11", "2024-08-01 10:12"
        ],
        "negative_probability": [0.2, 0.25, 0.3, 0.8, 0.85, 0.9]
    }

    df = pd.DataFrame(data)
    spikes = detect_sentiment_spike(df)

    print(spikes)
