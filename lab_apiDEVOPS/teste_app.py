
import unittest
from app import app
import werkzeug

# Patch temporário para compatibilidade com diferentes versões do werkzeug
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"


class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Criação do cliente de teste
        cls.client = app.test_client()

    def test_home_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "API is running"})

    def test_items_list(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"items": ["item1", "item2", "item3"]})

    def test_login_and_use_token(self):
        resp = self.client.post('/login')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('access_token', resp.json)
        token = resp.json.get('access_token')
        self.assertTrue(isinstance(token, str) and len(token) > 0)


if __name__ == '__main__':
    unittest.main()
