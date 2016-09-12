#!flask/bin/python
# coding: utf-8
from flask import Flask, jsonify
from flask_cors import CORS

from parser import get_movies

app = Flask(__name__)
CORS(app)

movies = [
    {
        "Title": "Mulholland Drive",
        "Year": "2001",
        "Rated": "R",
        "Released": "19 Oct 2001",
        "Runtime": "147 min",
        "Genre": "Drama, Mystery, Thriller",
        "Director": "David Lynch",
        "Writer": "David Lynch",
        "Actors": "Naomi Watts, Jeanne Bates, Dan Birnbaum, Laura Harring",
        "Plot": "After a car wreck on the winding Mulholland Drive renders a woman amnesiac, she and a perky Hollywood-hopeful search for clues and answers across Los Angeles in a twisting venture beyond dreams and reality.",
        "Language": "English, Spanish",
        "Country": "France, USA",
        "Awards": "Nominated for 1 Oscar. Another 46 wins & 56 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMjE4MDUyMzMyOF5BMl5BanBnXkFtZTcwMTAxOTQyMQ@@._V1_SX300.jpg",
        "Metascore": "81",
        "imdbRating": "8.0",
        "imdbVotes": "233,424",
        "imdbID": "tt0166924",
        "Type": "movie",
        "Response": "True",
        "Theaters": {
            "Roxie Theater": {
                "Info": "3117 16th Street, San Francisco, CA - (415) 863-1087",
                "Showtimes": {
                    "Today": ["7:00&ltrm;", "9:00pm&ltrm;"],
                    "Tomorrow": ["9:15pm‎&ltrm;"],
                    "Thursday": ['8:35pm&ltrm;'],
                    "Friday": ['7pm', '9:15pm', '11:00&ltrm;']
                }
            },
            "Alamo Drafthouse -- New Mission": {
                "Info": "2550 Mission Street, San Francisco, CA - (415) 549-5959",
                "Showtimes": {
                    "Today": ['7pm', '9:15pm', '11:00&ltrm;'],
                    "Tomorrow": ['8:35pm&ltrm;'],
                    "Thursday": ['7:00&ltrm;', '9:00pm&ltrm;'],
                    "Friday": ['7:00&ltrm;', '9:00pm&ltrm;']
                }
            }
        }
    },
    {
        "Title": "Aguirre, the Wrath of God",
        "Year": "1972",
        "Rated": "NOT RATED",
        "Released": "03 Apr 1977",
        "Runtime": "93 min",
        "Genre": "Adventure, Drama, History",
        "Director": "Werner Herzog",
        "Writer": "Werner Herzog",
        "Actors": "Klaus Kinski, Helena Rojo, Del Negro, Ruy Guerra",
        "Plot": "In the 16th century, the ruthless and insane Don Lope de Aguirre leads a Spanish expedition in search of El Dorado.",
        "Language": "German, Quechua, Spanish",
        "Country": "West Germany",
        "Awards": "4 wins & 3 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BNDU5ODY4ODY5Ml5BMl5BanBnXkFtZTcwODA2NTUyMQ@@._V1_SX300.jpg",
        "Metascore": "N/A",
        "imdbRating": "8.0",
        "imdbVotes": "37,812",
        "imdbID": "tt0068182",
        "Type": "movie",
        "Response": "True",
        "Theaters": {
            "Alamo Drafthouse -- New Mission": {
                "Info": "2550 Mission Street, San Francisco, CA - (415) 549-5959",
                "Showtimes": {
                    "Today": ['7pm', '9:15pm', '11:00&ltrm;'],
                    "Tomorrow": ['8:35pm&ltrm;'],
                    "Thursday": ['7:00&ltrm;', '9:00pm&ltrm;'],
                    "Friday": ['7:00&ltrm;', '9:00pm&ltrm;']
                }
            }
        }
    },
    {
        "Title": "Blood Simple.",
        "Year": "1984",
        "Rated": "R",
        "Released": "18 Jan 1985",
        "Runtime": "99 min",
        "Genre": "Crime, Thriller",
        "Director": "Joel Coen, Ethan Coen",
        "Writer": "Joel Coen, Ethan Coen",
        "Actors": "John Getz, Frances McDormand, Dan Hedaya, M. Emmet Walsh",
        "Plot": "A rich but jealous man hires a private investigator to kill his cheating wife and her new man. But, when blood is involved, nothing is simple.",
        "Language": "English, Spanish",
        "Country": "USA",
        "Awards": "4 wins & 6 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMTU5OTM3OTQ5M15BMl5BanBnXkFtZTYwNzEzMDc5._V1_SX300.jpg",
        "Metascore": "81",
        "imdbRating": "7.7",
        "imdbVotes": "66,630",
        "imdbID": "tt0086979",
        "Type": "movie",
        "Response": "True"
    },
    {
        "Title": "Oldboy",
        "Year": "2003",
        "Rated": "R",
        "Released": "21 Nov 2003",
        "Runtime": "120 min",
        "Genre": "Drama, Mystery, Thriller",
        "Director": "Chan-wook Park",
        "Writer": "Garon Tsuchiya (story), Nobuaki Minegishi (comic), Chan-wook Park (screenplay), Chun-hyeong Lim (screenplay), Jo-yun Hwang (screenplay), Joon-hyung Lim",
        "Actors": "Min-sik Choi, Ji-tae Yu, Hye-jeong Kang, Dae-han Ji",
        "Plot": "After being kidnapped and imprisoned for 15 years, Oh Dae-Su is released, only to find that he must find his captor in 5 days.",
        "Language": "Korean",
        "Country": "South Korea",
        "Awards": "26 wins & 16 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMTI3NTQyMzU5M15BMl5BanBnXkFtZTcwMTM2MjgyMQ@@._V1_SX300.jpg",
        "Metascore": "74",
        "imdbRating": "8.4",
        "imdbVotes": "351,374",
        "imdbID": "tt0364569",
        "Type": "movie",
        "Response": "True"
    },
    {
        "Title": "The Birds",
        "Year": "1963",
        "Rated": "PG-13",
        "Released": "29 Mar 1963",
        "Runtime": "119 min",
        "Genre": "Horror",
        "Director": "Alfred Hitchcock",
        "Writer": "Daphne Du Maurier (from the story by), Evan Hunter (screenplay)",
        "Actors": "Tippi Hedren, Suzanne Pleshette, Rod Taylor, Jessica Tandy",
        "Plot": "A wealthy San Francisco socialite pursues a potential boyfriend to a small Northern California town that slowly takes a turn for the bizarre when birds of all kinds suddenly begin to attack people.",
        "Language": "English",
        "Country": "USA",
        "Awards": "Nominated for 1 Oscar. Another 2 wins & 5 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMTAxNDA1ODc5MDleQTJeQWpwZ15BbWU4MDg2MDA4OTEx._V1_SX300.jpg",
        "Metascore": "N/A",
        "imdbRating": "7.7",
        "imdbVotes": "127,416",
        "imdbID": "tt0056869",
        "Type": "movie",
        "Response": "True",
        "Theaters": {
            "Alamo Drafthouse -- New Mission": {
                "Info": "2550 Mission Street, San Francisco, CA - (415) 549-5959",
                "Showtimes": {
                    "Today": ['7pm', '9:15pm', '11:00&ltrm;'],
                    "Tomorrow": ['8:35pm&ltrm;'],
                    "Thursday": ['7:00&ltrm;', '9:00pm&ltrm;'],
                    "Friday": ['7:00&ltrm;', '9:00pm&ltrm;']
                }
            }
        }
    },
    {
        "Title": "The Neon Demon",
        "Year": "2016",
        "Rated": "R",
        "Released": "24 Jun 2016",
        "Runtime": "117 min",
        "Genre": "Drama, Horror, Thriller",
        "Director": "Nicolas Winding Refn",
        "Writer": "Nicolas Winding Refn (story by), " + "Nicolas Winding Refn (screenplay), " + "Mary Laws (screenplay), Polly Stenham (screenplay)",
        "Actors": "Keanu Reeves, Jena Malone, Christina Hendricks, Elle Fanning",
        "Plot": "When aspiring model Jesse moves to Los Angeles, her youth and vitality are devoured by a group of beauty-obsessed women who will take any means necessary to get what she has.",
        "Language": "English", "Country": "France, USA, Denmark", "Awards": "2 wins & 2 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMTcyMjcxNTc3M15BMl5BanBnXkFtZTgwMTcxNTM4ODE@._V1_SX300.jpg",
        "Metascore": "57",
        "imdbRating": "7.0",
        "imdbVotes": "720",
        "imdbID": "tt1974419",
        "Type": "movie",
        "Response": "True"
    },
    {
        "Title": "Upstream Color",
        "Year": "2013",
        "Rated": "NOT RATED",
        "Released": "30 Aug 2013",
        "Runtime": "96 min",
        "Genre": "Drama, Sci-Fi",
        "Director": "Shane Carruth",
        "Writer": "Shane Carruth",
        "Actors": "Amy Seimetz, Shane Carruth, Andrew Sensenig, Thiago Martins",
        "Plot": "A man and woman are drawn together, entangled in the life cycle of an ageless organism. Identity becomes an illusion as they struggle to assemble the loose fragments of wrecked lives.",
        "Language": "English",
        "Country": "USA",
        "Awards": "3 wins & 30 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMTQzMzQ4MDAyNF5BMl5BanBnXkFtZTcwNzE0MDk3OA@@._V1_SX300.jpg",
        "Metascore": "81",
        "imdbRating": "6.8",
        "imdbVotes": "21,548",
        "imdbID": "tt2084989",
        "Type": "movie",
        "Response": "True"
    }
]


@app.route('/movies', methods=['GET'])
def get_all_movies():
    movies_to_return = get_movies()
    return jsonify({'movies': movies_to_return})

if __name__ == '__main__':
    app.run(threaded=True)