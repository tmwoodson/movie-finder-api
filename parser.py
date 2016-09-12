from bs4 import BeautifulSoup
from html_fetcher import fetch_html
from movie_api_helper import get_joined_movie_data

def get_movie_title(movie_node):
    title_node = movie_node.find('div', class_='name')
    title_anchor = title_node.find('a')
    title = title_anchor.string
    return title

def get_imdb_id(movie_node):
    info_node = movie_node.find('span', class_='info')
    info_anchors = info_node.find_all('a')
    imdb_id = None
    if len(info_anchors) > 0:
        imdb_anchor = info_anchors[-1]
        imdb_url = imdb_anchor['href']
        if 'imdb' in imdb_url:
            imdb_id = imdb_url.split('/title')[1].split('/')[1]
    return imdb_id

def get_movie_showtimes(movie_node):
    times_node = movie_node.find('div', class_="times")
    showtimes_nodes = times_node.contents
    times = []
    for showtime in showtimes_nodes:
        unparsed_time = showtime.contents[2]
        if type(unparsed_time) == type(showtime):
            unparsed_time = unparsed_time.string
        parsed_time = unparsed_time.split('pm')[0]
        parsed_time = parsed_time.encode("ascii", "replace")
        parsed_time = parsed_time.split('?')[0]
        if 'am' not in parsed_time:
            parsed_time += 'pm'
        times.append(parsed_time)
    return times

def get_theater_name(theater_node):
    desc_node = theater_node.find('div', class_='desc')
    name_node = desc_node.find('h2', class_='name')
    name_anchor = name_node.find('a')
    name = name_anchor.string
    return name

def get_theater_info(theater_node):
    desc_node = theater_node.find('div', class_='desc')
    info_node = desc_node.find('div', class_='info')
    info = info_node.text
    return info

def get_movies_from_html(data):
    soup = BeautifulSoup(data, 'html.parser')
    movies = {}
    for theater in soup.find_all('div', class_='theater'):
        theater_name = get_theater_name(theater)
        theater_info = get_theater_info(theater)

        for movie in theater.find_all('div', class_='movie'):
            showtimes = get_movie_showtimes(movie)
            theater_data = {'Info': theater_info, 'Showtimes': {'0': showtimes}}
            movie_title = get_movie_title(movie)
            movie_imdb_id = get_imdb_id(movie)
            movie_identifier = movie_imdb_id
            has_imdb = True
            if not movie_imdb_id:
                movie_identifier = movie_title
                has_imdb = False
            if movie_identifier not in movies:
                movies[movie_identifier] = {'Title': movie_title, 'HasImdb': has_imdb, 'Theaters': {}}
            movies[movie_identifier]['Theaters'][theater_name] = theater_data

    return movies

def get_movie_list(movies, use_fake=False):
    joined_list = [get_joined_movie_data(movie_id, movies[movie_id], use_fake) for movie_id in movies]
    return joined_list

def get_movies():
    html_text = fetch_html()
    movies_with_showtimes = get_movies_from_html(html_text)
    joined_movies = get_movie_list(movies_with_showtimes)
    return joined_movies

if __name__ == '__main__':
    movies = get_movies()

