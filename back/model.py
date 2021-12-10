from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
from scipy.special import softmax
import csv
import urllib.request
import numpy as np 


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
    task='sentiment'
    MODEL = f"cardiffnlp/twitter-roberta-base-{task}"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    labels = []
    mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
    with urllib.request.urlopen(mapping_link) as f:
        html = f.read().decode('utf-8').split("\n")
        csvreader = csv.reader(html, delimiter='\t')
    labels = [row[1] for row in csvreader if len(row) > 1]
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    model.save_pretrained(MODEL+'-model')
    return model, tokenizer, labels


def prediction(model, text, tokenizer, labels):
    """
    model : pre-trained model 
    text: input text we want to predict the sentiment 
    return : the score the sentiment analysis
    """
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    return [-1, 0, 1], scores, labels

def prediction_df(df,model,text_col,tokenizer,labels):
    """
    df : dataframe
    model: pre-trained model
    text_col: column containing the text to predict
    return : the dataframe with a new column predict containing the prediction
    """
    def predict(text):
        """
        returns : the best score of the sentiment analysis 
        """
        p = prediction(m,text,tokenizer,labels)
        return p[0][np.argmax(p[1])]
    df['predict']= df[text_col].apply(predict)
    return df 

if __name__ == '__main__':
    print('Prediction')
    m, tokenizer, labels = model()
    text = 'good night !'
    p = prediction(m, text, tokenizer, labels)
    print(p)
