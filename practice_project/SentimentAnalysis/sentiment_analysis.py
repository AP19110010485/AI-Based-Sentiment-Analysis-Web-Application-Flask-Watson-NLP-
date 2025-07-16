"""
This module provides a function to analyze sentiment
using IBM Watson's NLP BERT-based sentiment API.
"""

import json  # Standard library import
import requests  # Third-party library import

def sentiment_analyzer(text_to_analyse):
    """
    Sends the input text to IBM Watson Sentiment API and returns the result.

    Parameters:
    text_to_analyse (str): The input text to analyze.

    Returns:
    dict: A dictionary containing 'label' and 'score'.
          Returns None values if the request fails or the API returns an error.
    """
    url = (
        "https://sn-watson-sentiment-bert.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/SentimentPredict"
    )
    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    headers = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }

    try:
        response = requests.post(url, json=myobj, headers=headers, timeout=10)
        formatted_response = json.loads(response.text)

        if response.status_code == 200:
            label = formatted_response['documentSentiment']['label']
            score = formatted_response['documentSentiment']['score']
        else:
            label = None
            score = None

    except requests.exceptions.RequestException:
        label = None
        score = None

    return {'label': label, 'score': score}
