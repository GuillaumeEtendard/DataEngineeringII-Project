from model import preprocess, prediction, model,prediction_df,predict
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import unittest

df = pd.read_csv('../data/process/data_cleaned.csv')
m, tokenizer, labels = model()
prediction_df = prediction_df(df,model,'text',tokenizer,labels)

class Test(unittest.TestCase):
    def test_accuracy(self):
        self.assertLessEqual(accuracy_score(df['sentiment'].astype('int64'), df['predict']),0.8 )
        

if __name__ == '__main__':
    unittest.main()