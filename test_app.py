import unittest
import os
import json
from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_countly_endpoint(self):
        # Prepare test data
        metrics = {
            "metric1": 10,
            "metric2": 20
        }
        headers = {
            "X-Secret-Key": "your_secret_key"
        }

        # Send a POST request to the countly endpoint
        response = self.app.post("/countly", json=metrics, headers=headers)

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check if the metrics file is created and contains the correct data
        path = os.path.join(os.path.dirname(__file__), "metrics.json")
        with open(path, 'r') as f:
            saved_metrics = json.load(f)
        self.assertEqual(saved_metrics, metrics)

if __name__ == '__main__':
    unittest.main()