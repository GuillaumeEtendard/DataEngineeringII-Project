import unittest
import requests

class Test(unittest.TestCase):
    def test_response(self):
        data = {'text':'i love chocolat !'}
        response = requests.post('http://localhost:8000/get_sentiment/', data)
        print(response.elapsed.total_seconds())
        self.assertLessEqual(response.elapsed.total_seconds(), 1) 

if __name__ == '__main__':
    unittest.main()