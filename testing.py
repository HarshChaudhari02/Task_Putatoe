import unittest
import requests

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:5000'

    def test_get_test(self):
        response = requests.get(f'{self.base_url}/api/test')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('test', data)
        self.assertIsInstance(data['test'], str)

if __name__ == '__main__':
    unittest.main()
