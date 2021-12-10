from model import load_model, prediction_df
import pandas as pd
from sklearn.metrics import accuracy_score
import unittest

df = pd.read_csv('../data/process/data_cleaned.csv')
m, tokenizer, labels = load_model()


class Test(unittest.TestCase):
    def test_accuracy(self):
        predicted_df = prediction_df(df, m, 'text', tokenizer, labels)
        acc = accuracy_score(
            predicted_df['sentiment'].astype('int64'), predicted_df['predict'])
        print(acc)
        self.assertTrue(acc >= 0.8)


if __name__ == '__main__':
    unittest.main()
