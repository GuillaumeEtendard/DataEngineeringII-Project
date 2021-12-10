from model import preprocess, prediction, model
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import unittest

df_tw = pd.read_csv('train.tsv',sep='\t')
df_tw['sentiment'] = df_tw['Sentiment']
df_tw['text'] = df_tw['Phrase']
df_tw = df_tw.drop(columns=['Sentiment', 'Phrase', 'SentenceId', 'PhraseId'])

df_tw = df_tw[(df_tw.sentiment != 3) & (df_tw.sentiment != 1)]
df_tw.sentiment[df_tw.sentiment == 4] = 1 
df_tw.sentiment[df_tw.sentiment == 0] = -1 
df_tw.sentiment[df_tw.sentiment == 2] = 0
df_tw['sentiment'] = df_tw['sentiment'].astype('int64')
df_tw = df_tw
df0_train = df_tw[df_tw.sentiment == 0].iloc[:200][:]
dfpos_train = df_tw[df_tw.sentiment == 1].iloc[:200][:]
dfneg_train = df_tw[df_tw.sentiment == -1].iloc[:200][:]

merged_df_train = pd.concat([df0_train, dfpos_train,dfneg_train])

m, tokenizer, labels = model()
def predict(text):
    p = prediction(m, text, tokenizer, labels)
    return p[0][np.argmax(p[1])]
merged_df_train['predict'] = merged_df_train['text'].apply(predict)

accuracy_score(merged_df_train['sentiment'].astype('int64'), merged_df_train['predict'])
