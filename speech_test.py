from hume import HumeBatchClient
from hume.models.config import LanguageConfig
from dotenv import load_dotenv
import os
import streamlit as st
#import pprint
#from utilities import print_emotions
from typing import Any, Dict, List

#Load in API Key and use it in the client
load_dotenv()
apiKey = os.environ['API_KEY']
client = HumeBatchClient(apiKey)

def print_emotions(emotions: List[Dict[str, Any]]) -> None:
    emotion_map = {e["name"]: e["score"] for e in emotions}
    count = 0
    totalValence = 0
    for emotion in ["Sadness", "Anger", "Anxiety", "Distress", "Disappointment"]:
        totalValence = totalValence + round(emotion_map[emotion], 2)
        count += 1
    avg = totalValence / count  
    return avg



#Define filepath and job
filepaths = ["sample.txt"]
def edit_file(user_input):
    f = open('sample.txt', 'w')
    f.write(user_input)
    


#Run job


#Get job results


# def print_emotions(emotions: List[Dict[str, Any]]) -> None:
#     emotion_map = {e["name"]: e["score"] for e in emotions}
#     count = 0
#     totalValence = 0
#     for emotion in ["Sadness", "Anger", "Anxiety", "Distress", "Disappointment"]:
#         totalValence = totalValence + round(emotion_map[emotion], 2)
#         count += 1
#     avg = totalValence / count  
#     return avg
def get_sentiment_value():
    config = LanguageConfig(sentiment={})
    job = client.submit_job(None, [config], files=filepaths)
    job.await_complete()
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
                    return certainValue
                

def value_decider(value):
    if value < 0.3:
        return 'Sentiment regarding the stock market seem positive, you should be bullish'
    else:
        return 'Sentiment regarding the stock market seem positive, you should be bearish'


def main():
    st.title('Sentiment Analysis')
    user_input = st.text_input('Please enter the transcript')
    edit_file(user_input=user_input)
    if st.button('Get the sentiment assessment'):
        st.write(value_decider(get_sentiment_value()))
        
if __name__ == '__main__':
    main()