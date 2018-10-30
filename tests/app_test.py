# from flask_testing import TestCase
from app import app, mongodb_server, mongo
import unittest


class TestApp(unittest.TestCase):
    def test_app(self):
        '''to ensure  that flask was set up correctly'''
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_app_page(self):
        '''to ensure  that flask was set up correctly'''
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Today\'s Update' in response.data)


if __name__ == '__main__':
    unittest.main()



