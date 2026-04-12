import unittest
# Assuming your main file is named flask_app.py
from flask_app import app 

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        """Set up the test client before each test runs."""
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        """Test if the root / route loads correctly."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_gamelist_route(self):
        """Test if the /gamelist route loads and returns data."""
        response = self.app.get('/gamelist')
        
        # Verify the page loads successfully
        self.assertEqual(response.status_code, 200)
        
        # Verify that HTML content from the template is returned
        self.assertIn(b'MMO Games', response.data)
        
    def test_404_error(self):
        """Test that a non-existent route returns a 404."""
        response = self.app.get('/this-page-does-not-exist')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
