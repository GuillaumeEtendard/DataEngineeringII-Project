import unittest
import requests

class Test(unittest.TestCase):
    def test_response(self):
        params = {'text':'i love chocolat !'}
        response = requests.get('http://localhost:8000/get_sentiment/',params = params)
        print(response.elapsed.total_seconds())
        self.assertLessEqual(response.elapsed.total_seconds(), 5) 

if __name__ == '__main__':
    unittest.main()