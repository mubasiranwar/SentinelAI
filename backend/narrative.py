from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from utils import clean_text



def detect_repeated_narratives(texts, similarity_threshold=0.7):
    """
    Detects narrative repetition using TF-IDF and cosine similarity.

    Returns:
    - clusters of similar texts
    - repetition score
    """

    if len(texts) < 2:
        return [], 0.0

    vectorizer = TfidfVectorizer(
        ngram_range=(2, 3),
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(texts)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    clusters = []
    visited = set()

    for i in range(len(texts)):
        if i in visited:
            continue

        similar = np.where(similarity_matrix[i] > similarity_threshold)[0]

        if len(similar) > 1:
            cluster = [texts[j] for j in similar]
            clusters.append(cluster)
            visited.update(similar)

    repetition_score = len(clusters) / len(texts)

    return clusters, round(repetition_score, 3)


# ----------------------------
# Run test
# ----------------------------
if __name__ == "__main__":
    sample_texts = [
        "government hiding flood casualties",
        "government hiding real flood numbers",
        "wake up before it too late",
        "this is a natural disaster",
        "government hiding truth"
    ]

    clusters, score = detect_repeated_narratives(sample_texts)

    print("Clusters:")
    for c in clusters:
        print(c)

    print("Repetition Score:", score)
