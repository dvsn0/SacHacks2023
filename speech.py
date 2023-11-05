from hume import HumeBatchClient
from hume.models.config import LanguageConfig
from dotenv import load_dotenv
import os
#import pprint
#from utilities import print_emotions
from typing import Any, Dict, List
from utilities import print_emotions



#Load in API Key and use it in the client
load_dotenv()
apiKey = os.environ['API_KEY']
client = HumeBatchClient(apiKey)

#Define filepath and job
filepaths = ["sample.txt"]
config = LanguageConfig(sentiment={})
job = client.submit_job(None, [config], files=filepaths)

#Run job
print(job)
print("Running...")

#Get job results
job.await_complete()

# def print_emotions(emotions: List[Dict[str, Any]]) -> None:
#     emotion_map = {e["name"]: e["score"] for e in emotions}
#     count = 0
#     totalValence = 0
#     for emotion in ["Sadness", "Anger", "Anxiety", "Distress", "Disappointment"]:
#         totalValence = totalValence + round(emotion_map[emotion], 2)
#         count += 1
#     avg = totalValence / count  
#     return avg

full_predictions = job.get_predictions()
certainValue = 0.0
for source in full_predictions:
    source_name = source["source"]
    predictions = source["results"]["predictions"]
    for prediction in predictions:
        language_predictions = prediction["models"]["language"]["grouped_predictions"]
        for language_prediction in language_predictions:
            for chunk in language_prediction["predictions"]:
                certainValue = print_emotions(chunk["emotions"])

print(certainValue)
                
def get_certain_value():
    return certainValue
