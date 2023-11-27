import unittest
from flask import Flask, render_template
from app import app  # Assuming your Flask app is in a file named app.py

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_hello_route(self):
        response = self.app.get('/')
        self.assertIn(b"I'm almost a DevOps engineer", response.data)

    def test_static_file_exists(self):
        response = self.app.get('/static/images/sample.jpeg')
        self.assertEqual(response.status_code, 200)

    def test_404_error(self):
        response = self.app.get('/nonexistent')
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'The requested URL was not found on the server.', response.data)

if __name__ == '__main__':
    unittest.main()
