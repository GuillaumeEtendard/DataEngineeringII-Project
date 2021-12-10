import unittest
import requests

class Test(unittest.TestCase):
    def test_response(self):
        response = requests.get('http://localhost:8000/get_sentiment/')
        print(response.elapsed.total_seconds())
        self.assertLessEqual(response.elapsed.total_seconds(), 1) 

if __name__ == '__main__':
    unittest.main()