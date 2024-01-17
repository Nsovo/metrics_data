import unittest
import json
from app import metricsLocal
from flask import Flask

class TestCountlyUploadEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = metricsLocal.test_client()

    def test_countly_upload(self):
        # Prepare test data, Random data since we don't know the structure of the data
        test_data = {
            "key1": "value1",
            "key2": "value2"
        }

        # Send POST request to the /countly endpoint
        response = self.app.post('/countly',
                                data=json.dumps(test_data),
                                content_type='application/json')

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check response data
        response_data = json.loads(response.data)
        self.assertEqual(response_data, {"success": True})

        # Check if data is saved correctly
        with open("data/metrics.json", 'r') as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data, test_data)

if __name__ == "__main__":
    unittest.main()