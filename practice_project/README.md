
# 🧠 AI-Based Sentiment Analysis Web Application (Flask + Watson NLP)

This project demonstrates how to build a sentiment analysis web app using **IBM Watson NLP**, **Python**, and **Flask**. Users can input text and get real-time predictions on whether the sentiment is **Positive**, **Negative**, or **Neutral**.

---

## ✅ Tasks Overview

| Task No. | Task Description                                 |
|----------|--------------------------------------------------|
| Task 1   | Clone the Project Repository                     |
| Task 2   | Create a Sentiment Analysis Application          |
| Task 3   | Format the Output of the Application             |
| Task 4   | Package the Application                          |
| Task 5   | Run Unit Tests                                   |
| Task 6   | Deploy as a Flask Web App                        |
| Task 7   | Incorporate Error Handling                       |
| Task 8   | Run Static Code Analysis                         |

---

## 🧩 Task 1: Clone the Project Repository

```bash
mkdir practice_project
cd practice_project
git clone https://github.com/ibm-developer-skills-network/zzrjt-practice-project-emb-ai.git .
python3.11 -V
pip3.11 show requests flask pylint
python3.11 -m pip install requests flask pylint
```

---

## 🧩 Task 2: Create Sentiment Analysis Application

**sentiment_analysis.py**

```python
import requests

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json=myobj, headers=header)
    return response.text
```

---

## 🧩 Task 3: Format the Output

```python
import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']
    return {'label': label, 'score': score}
```

---

## 🧩 Task 4: Package the Application

```bash
mkdir SentimentAnalysis
mv sentiment_analysis.py SentimentAnalysis/
echo "from . import sentiment_analysis" > SentimentAnalysis/__init__.py
```

Test in shell:
```bash
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
sentiment_analyzer("This is great!")
```

---

## 🧩 Task 5: Run Unit Tests

**test_sentiment_analysis.py**

```python
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        self.assertEqual(sentiment_analyzer('I love working with Python')['label'], 'SENT_POSITIVE')
        self.assertEqual(sentiment_analyzer('I hate working with Python')['label'], 'SENT_NEGATIVE')
        self.assertEqual(sentiment_analyzer('I am neutral on Python')['label'], 'SENT_NEUTRAL')

if __name__ == "__main__":
    unittest.main()
```

```bash
python3.11 test_sentiment_analysis.py
```

---

## 🧩 Task 6: Deploy as Web Application using Flask

**Directory Structure**
```
practice_project/
├── SentimentAnalysis/
│   ├── __init__.py
│   ├── sentiment_analysis.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
├── server.py
```

**server.py**

```python
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']

    if label is None:
        return "Invalid input! Try again."
    return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

```bash
python3.11 server.py
```

---

## 🧩 Task 7: Add Error Handling

Update `sentiment_analyzer()`:

```python
import requests
import json

def sentiment_analyzer(text_to_analyse):
    try:
        url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
        myobj = { "raw_document": { "text": text_to_analyse } }
        header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
        response = requests.post(url, json=myobj, headers=header, timeout=5)
        if response.status_code != 200:
            return {'label': None, 'score': None}
        formatted_response = json.loads(response.text)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
        return {'label': label, 'score': score}
    except Exception:
        return {'label': None, 'score': None}
```

---

## 🧩 Task 8: Static Code Analysis

```bash
pylint SentimentAnalysis/sentiment_analysis.py
pylint server.py
```

Fix issues like:
- Missing docstrings
- Line too long
- Wrong import order

---

## 🚀 Conclusion

With Watson NLP + Flask, you’ve created a complete AI web app. You can now enhance it further with databases, advanced UI, or deploy to platforms like **Render**, **Heroku**, or **IBM Cloud**.
