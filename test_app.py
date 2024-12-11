import unittest
from app import app, collection
from pymongo import MongoClient

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        
        self.app = app.test_client()
        self.app.testing = True

        # Set up test database
        self.mongo_client = MongoClient("url")  # Use local MongoDB for testing
        self.test_db = self.mongo_client["test_todo"]
        self.test_collection = self.test_db["test_tododb"]

        #
        global collection
        collection = self.test_collection

    def tearDown(self):
        # Drop the test database after tests
        self.mongo_client.drop_database("test_todo")

    def test_home(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome", response.data)

    def test_descriptive_statistics(self):
        response = self.app.get("/descriptive")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Descriptive Statistics", response.data)

    def test_visualization(self):
        response = self.app.get("/visualization")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Scatter Plot", response.data)
        self.assertIn(b"Heatmap", response.data)
        self.assertIn(b"Boxplot", response.data)

    def test_prediction(self):
        form_data = {
            "median_income": 5.0,
            "housing_median_age": 30,
            "total_rooms": 5000,
            "total_bedrooms": 1000,
            "population": 3000,
            "households": 800,
            "longitude": -120.0,
            "latitude": 35.0
        }
        response = self.app.post("/predict", data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Predicted Value", response.data)

        # Check if data is stored in the test collection
        record = self.test_collection.find_one({"median_income": 5.0})
        self.assertIsNotNone(record)
        self.assertIn("predicted_value", record)

if __name__ == "__main__":
    unittest.main()
