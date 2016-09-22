import requests
import json

api_url = 'http://www.omdbapi.com/'

fake_data = {
    '12345': {"Title":"Big Momma's House",
              "Year":"2000",
              "Rated":"PG-13",
              "Released":"02 Jun 2000",
              "Runtime":"99 min",
              "Genre":"Action, Comedy, Crime",
              "Director":"Raja Gosnell",
              "Writer":"Darryl Quarles (story), Darryl Quarles (screenplay), Don Rhymer (screenplay)",
              "Actors":"Martin Lawrence, Nia Long, Paul Giamatti, Jascha Washington",
              "Plot":"In order to protect a beautiful woman and her son from a robber, a male FBI agent disguises himself as a large grandmother.",
              "Language":"English",
              "Country":"USA, Germany",
              "Awards":"1 win & 8 nominations.",
              "Poster":"http://ia.media-imdb.com/images/M/MV5BMTc4NTc0NzQ0OV5BMl5BanBnXkFtZTYwNDkxMjY5._V1_SX300.jpg",
              "Metascore":"33",
              "imdbRating":"5.1",
              "imdbVotes":"66,432",
              "imdbID":"12345",
              "Type":"movie",
              "Response":"True"},
    'kittens': {"Title": "A Fake Movie",
              "Year": "2001",
              "Rated": "R",
              "Director": "Sean Hannity",
              "Writer": "Sean Hannity's Face",
              "Actors": "Your mom, 200 kittens, Ted Cruz, half a whoopie pie",
              "Plot": "A bad lip reading.",
              "Language": "English?",
              "Country": "U!S!A!",
              "Awards": "Definitely none",
              "Poster": "http://ia.media-imdb.com/images/M/MV5BMTc4NTc0NzQ0OV5BMl5BanBnXkFtZTYwNDkxMjY5._V1_SX300.jpg",
              "Metascore": "2",
              "imdbRating": "1.1",
              "imdbVotes": "66,432",
              "imdbID": "kittens",
              "Type": "movie",
              "Response": "True"},
    'meow': {"Title": "Two Cats One Bowl",
                "Year": "2010",
                "Rated": "XXX",
                "Director": "Kerfluffle",
                "Writer": "Anonymous",
                "Actors": "Kerfluffle, Chairman Meow",
                "Plot": "2 cats. 1 bowl. Enough said.",
                "Language": "Meownglish",
                "Country": "Canadia",
                "Awards": "Academeow Awards",
                "Poster": "http://ia.media-imdb.com/images/M/MV5BMTc4NTc0NzQ0OV5BMl5BanBnXkFtZTYwNDkxMjY5._V1_SX300.jpg",
                "Metascore": "6.6",
                "imdbRating": "7.9",
                "imdbVotes": "2",
                "imdbID": "meow",
                "Type": "movie",
                "Response": "True"},
    'Something Really Obscure': {"Title": "Something Really Obscure",
                "Year": "2016",
                "Rated": "NR",
                "Director": "You Wouldn't Have Heard Of Them",
                "Writer": "The People of the Western Sahara",
                "Actors": "Madame Psychosis",
                "Plot": "Plotless and mostly dialogue-free",
                "Language": "Romanian with Quechua subtitles",
                "Country": "Sweden, Denmark, Senegal, France",
                "Awards": "TriBeCa Film Festival Critics' Choice Award",
                "Poster": "http://ia.media-imdb.com/images/M/MV5BMTc4NTc0NzQ0OV5BMl5BanBnXkFtZTYwNDkxMjY5._V1_SX300.jpg",
                "Metascore": "8.0",
                "imdbRating": "10",
                "imdbVotes": "1",
                "imdbID": "huh",
                "Type": "movie",
                "Response": "True"},
    'Not Even A Movie': {
        "Response": "False",
        "Error": "Nope, definitely not a movie."
    }
}

def get_api_movie_data(movie_identifier, has_imdb, use_fake):
    if use_fake:
        return fake_data[movie_identifier]
    else:
        url = api_url
        if has_imdb:
            url += '?i='
        else:
            url += '?t='
        url += movie_identifier
        response = requests.get(url)
        result = response.text
        return result


def get_joined_movie_data(movie_identifier, movie, use_fake):
    result = get_api_movie_data(movie_identifier, movie['HasImdb'], use_fake)
    if type(result).__name__ != 'dict':
        result = json.loads(result)
    result['Theaters'] = movie['Theaters']
    result['imdbUrl'] = movie['imdbUrl']
    return result