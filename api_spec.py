
from bs4 import BeautifulSoup
import unittest
import json

from app import app
from html_fetcher import fetch_html
import parser

expected_movies = {}
expected_movies['kittens'] = {
    'Title': 'A Fake Movie',
    'HasImdb': True,
    'Theaters': {
        'Alamo Drafthouse Cinema - New Mission': {
            'Info': 'Near the Old Popeye\'s',
            'Showtimes': {
                '0': ['1:40pm', '7:40pm', '10:45pm']
            }
        }
    }
}
expected_movies['meow'] = {
    'Title': 'Two Cats One Bowl',
    'HasImdb': True,
    'Theaters': {
        'Roxie Theater': {
            'Info': 'By Crackheads',
            'Showtimes': {
                '0': ['2:00pm']
            }
        }
    }
}
expected_movies['12345'] = {
    'Title': 'Big Momma\'s House',
    'HasImdb': True,
    'Theaters': {
        'Alamo Drafthouse Cinema - New Mission': {
            'Info': 'Near the Old Popeye\'s',
            'Showtimes': {
                '0': ['9:40pm', '10:45pm']
            }
        }
    }
}
expected_movies['Something Really Obscure'] = {
    'Title': 'Something Really Obscure',
    'HasImdb': False,
    'Theaters': {
        'Alamo Drafthouse Cinema - New Mission': {
            'Info': 'Near the Old Popeye\'s',
            'Showtimes': {
                '0': ['9:00pm']
            }
        },
        'Roxie Theater': {
            'Info': 'By Crackheads',
            'Showtimes': {
                '0': ['7:20pm', '9:45pm']
            }
        }
    }
}

class APITestCase(unittest.TestCase):

    def setUp(self):
        print 'setting up API test case'
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        print 'tearing down API test case'
        pass

    def test_status_code(self):
        result = self.app.get('/movies')
        self.assertEqual(result.status_code, 200)

    def test_data(self):
        result = self.app.get('/movies').get_data()
        movies = json.loads(result)['movies']
        first_movie = movies[0]
        print first_movie
        # self.assertEqual(first_movie['Title'], 'Mulholland Drive', 'movie title error')

class ParserTestCase(unittest.TestCase):

    def setUp(self):
        print 'setting up parser test case'
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        print 'tearing down parser test case'
        pass

    def test_title(self):
        movie_title = 'Ping Pong in a Time of Cholera'
        movie_text = '<div class="movie"><div class="name"><a>' + movie_title + '</a></div></div>'
        soup = BeautifulSoup(movie_text, 'html.parser')
        result = parser.get_movie_title(soup)
        self.assertEqual(result, movie_title, 'movie title does not match')

    def test_imdb_id(self):
        imdb_id = 'idididid'
        imdb_href = '/url?q=http://www.imdb.com/title/' + imdb_id + '/&sa=X&oi=moviesi&ii=0&usg=AFQjCNEOO9oSaPr-r6KyQoMHMh3Y7zJ66g'
        movie_text = '<div class="movie">' \
                        '<span class="info">' \
                            '<a href="/url?q=http://www.youtube.com/watch%3Fv%3DY7JG42F6_2E&sa=X&oi=movies&ii=0&usg=AFQjCNE-kwxjcB4pQmFAAIhw0iuoshaZkg">Trailer</a>' \
                            '<a href="' + imdb_href + '"></a>' \
                        '</span>' \
                     '</div>'
        soup = BeautifulSoup(movie_text, 'html.parser')
        result = parser.get_imdb_id(soup)
        self.assertEqual(imdb_id, result, 'imdb id does not match')

    def test_missing_imdb_id(self):
        movie_text = '<div class="movie">' \
                        '<span class="info">Spanish with Laoatian Subtitles</span>' \
                     '</div>'
        soup = BeautifulSoup(movie_text, 'html.parser')
        result = parser.get_imdb_id(soup)
        self.assertEqual(result, None, 'improper handling for missing imdb id')

    def test_movie_showtimes(self):
        showtimes = ['9:30pm', '10:30pm']
        movie_text = '<div class="movie">' \
                        '<div class="name">' \
                            '<a href="fake.com">Something Really Obscure</a>' \
                        '</div>' \
                        '<span class="info">Documentary, 55 minutes, Mandarin with Esperanto subtitles</span>' \
                        '<div class="times">' \
                            '<span style="color:#666"><span style="padding:0 "></span><!-- -->' + showtimes[0] + '</span>' \
                            '<span style="color:"><span style="padding:0 "></span><!-- --><a class="fl" href="/url?q=http://www.movietickets.com">' + showtimes[1] + '</a></span>' \
                        '</div>' \
                    '</div>'
        soup = BeautifulSoup(movie_text, 'html.parser')
        result = parser.get_movie_showtimes(soup)
        self.assertEqual(result, showtimes, 'movie showtimes do not match')

    def test_theater_name(self):
        theater_name = 'Century Landmark 4D Futureplex'
        theater_text = '<div class="theater">' \
                            '<div class="desc" id="theater_1">' \
                                '<h2 class="name">' \
                                    '<a href="">' + theater_name + '</a>' \
                                '</h2>' \
                                '<div class="info"></div>' \
                            '</div>' \
                            '<div class="showtimes"></div>' \
                        '</div>'
        soup = BeautifulSoup(theater_text, 'html.parser')
        result = parser.get_theater_name(soup)
        self.assertEqual(result, theater_name, 'theater name does not match')

    def test_theater_info(self):
        theater_info = 'in C-Stat\'s room'
        theater_text = '<div class="theater">' \
                            '<div class="desc" id="theater_1">' \
                                '<h2 class="name"></h2>' \
                                '<div class="info">' \
                                    '' + theater_info + '' \
                                    '<a href target="_top" />' \
                                '</div>' \
                            '</div>' \
                            '<div class="showtimes"></div>' \
                        '</div>'
        soup = BeautifulSoup(theater_text, 'html.parser')
        result = parser.get_theater_info(soup)
        self.assertEqual(result, theater_info, 'theater info does not match')


    def test_get_movies(self):
        html_text = fetch_html(True)
        parsed_movies = parser.get_movies_from_html(html_text)
        self.assertEqual(len(parsed_movies.keys()), len(expected_movies.keys()), 'not the expected number of movies')
        for movie_id in expected_movies:
            expected = expected_movies[movie_id]
            found = parsed_movies[movie_id]
            self.assertEqual(expected['Title'], found['Title'], 'title mismatch for movie id ' + movie_id)
            self.assertEqual(expected['HasImdb'], found['HasImdb'],
                             'has_imdb mismatch for movie id ' + movie_id)
            expected_theaters = expected['Theaters']
            found_theaters = found['Theaters']
            self.assertEqual(len(found_theaters.keys()), len(expected_theaters.keys()), 'not the expected number of theaters for movie ' + movie_id)
            for theater_name in expected_theaters:
                expected_theater = expected_theaters[theater_name]
                found_theater = found_theaters[theater_name]
                self.assertEqual(expected_theater['Info'], found_theater['Info'], 'theater info does not match for theater ' + theater_name)
                expected_showtimes = expected_theater['Showtimes']['0']
                found_showtimes = found_theater['Showtimes']['0']
                self.assertEqual(expected_showtimes, found_showtimes, 'showtimes do not match for ' + theater_name + ' and ' + movie_id)

class MovieAPIHelperTestCase(unittest.TestCase):

    def test_movie_list(self):
        html_text = fetch_html(True)
        parsed_movies = parser.get_movies_from_html(html_text)
        joined_movies = parser.get_movie_list(parsed_movies, True)
        self.assertIsInstance(joined_movies, list, 'parser.get_movie_list should return a list')
        self.assertEqual(len(joined_movies), 4, 'movie list does not have the expected length')
        first_movie = joined_movies[0]
        self.assertTrue('Title' in first_movie, 'movie output does not have a title')
        self.assertTrue('Theaters' in first_movie, 'movie output does not have a theater')
        self.assertTrue('Roxie Theater' in first_movie['Theaters'], 'missing theater data in movie list')


if __name__ == '__main__':

    test_classes = [APITestCase, ParserTestCase, MovieAPIHelperTestCase]
    loader = unittest.TestLoader()
    test_suites = [loader.loadTestsFromTestCase(klass) for klass in test_classes]

    big_suite = unittest.TestSuite(test_suites)

    unittest.TextTestRunner(verbosity=2).run(big_suite)