from typing import Any, Dict, List


def print_emotions(emotions: List[Dict[str, Any]]) -> None:
    emotion_map = {e["name"]: e["score"] for e in emotions}
    count = 0
    totalValence = 0
    for emotion in ["Sadness", "Anger", "Anxiety", "Distress", "Disappointment"]:
        totalValence = totalValence + round(emotion_map[emotion], 2)
        count += 1
    avg = totalValence / count  
    return avg 


# def print_sentiment(sentiment: List[Dict[str, Any]]) -> None:
#     sentiment_map = {e["name"]: e["score"] for e in sentiment}
#     for rating in range(1, 10):
#         print(f"- Sentiment {rating}: {sentiment_map[str(rating)]:4f}")