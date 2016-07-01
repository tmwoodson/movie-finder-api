from app import app
import unittest
import json

class APITestCase(unittest.TestCase):

    def setUp(self):
        print 'setting up'
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        print 'tearing down'
        pass

    def test_basic(self):
        self.assertEqual(1, 1, 'basic test fails')

    def test_status_code(self):
        result = self.app.get('/movies')
        self.assertEqual(result.status_code, 200)

    def test_data(self):
        result = self.app.get('/movies').get_data()
        movies = json.loads(result)['movies']
        first_movie = movies[0]
        self.assertEqual(first_movie['Title'], 'Mulholland Drive', 'movie title error')

suite = unittest.TestLoader().loadTestsFromTestCase(APITestCase)

unittest.TextTestRunner(verbosity=2).run(suite)