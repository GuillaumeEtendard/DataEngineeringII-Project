from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request
import tensorflow as tf
tf.config.experimental.list_physical_devices('GPU')

def preprocess(text):
    """
    preprocess text such as username and link placeholders 
    """
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

def model():
    """
    Loading the pre-trained model
    """
    MODEL = f"cardiffnlp/twitter-roberta-base-{'sentiment'}"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    labels=[]
    mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
    with urllib.request.urlopen(mapping_link) as f:
        html = f.read().decode('utf-8').split("\n")
        csvreader = csv.reader(html, delimiter='\t')
    labels = [row[1] for row in csvreader if len(row) > 1]
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    model.save_pretrained(MODEL)
    return model,tokenizer

def prediction(model,text,tokenizer):
    """
    model : pre-trained model 
    text: input text we want to predict the sentiment 
    print : the score the sentiment analysis
    """
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    for i in range(scores.shape[0]):
        l = labels[ranking[i]]
        s = scores[ranking[i]]
        print(f"{i+1}) {l} {np.round(float(s), 4)}")

if __name__ == 'main':
    print('Prediction')
    model,tokenizer = model()
    text = 'good night !'
    prediction = prediction(model,text,tokenizer)
