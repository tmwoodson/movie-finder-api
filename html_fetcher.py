import requests
fake_data = '<div id="movie-results">' \
                '<div class="theater">' \
                    '<div class="desc" id="theater_1">' \
                        '<h2 class="name">' \
                            '<a href="/movies/?alamo">Alamo Drafthouse Cinema - New Mission</a>' \
                        '</h2>' \
                        '<div class="info">' \
                            'Near the Old Popeye\'s'\
                            '<a href target="_top"></a>' \
                        '</div>' \
                    '</div>' \
                    '<div class="showtimes">' \
                        '<div class="movie">' \
                            '<div class="name">' \
                                '<a href="fake.com">A Fake Movie</a>' \
                            '</div>' \
                            '<span class="info">' \
                                '<a href="whatevs.com" />' \
                                '<a href="/url?q=http://www.imdb.com/title/kittens" />' \
                            '</span>' \
                            '<div class="times">' \
                                '<span style="color:#666"><span style="padding:0 "></span><!-- -->1:40</span>' \
                                '<span style="color:#666"><span style="padding:0 "></span><!-- -->7:40</span>' \
                                '<span style="color:#666"><span style="padding:0 "></span><!-- -->10:45</span>' \
                            '</div>' \
                        '</div>' \
                        '<div class="movie">' \
                            '<div class="name">' \
                                '<a href="fake.com">Big Momma\'s House</a>' \
                            '</div>' \
                            '<span class="info">' \
                                '<a href="/url?q=http://www.imdb.com/title/12345" />' \
                            '</span>' \
                            '<div class="times">' \
                                '<span style="color:"><span style="padding:0 "></span><!-- --><a class="fl" href="/url?q=http://www.movietickets.com">9:40</a></span>' \
                                '<span style="color:"><span style="padding:0 "></span><!-- --><a class="fl" href="/url?q=http://www.movietickets.com">10:45</a></span>' \
                            '</div>' \
                        '</div>' \
                        '<div class="movie">' \
                            '<div class="name">' \
                                '<a href="fake.com">Something Really Obscure</a>' \
                            '</div>' \
                            '<span class="info">Documentary, 55 minutes, Mandarin with Esperanto subtitles</span>' \
                            '<div class="times">' \
                                '<span style="color:#666"><span style="padding:0 "></span><!-- -->9:00pm</span>' \
                            '</div>' \
                        '</div>' \
                    '</div>' \
                '</div>' \
                '<div class="theater">' \
                    '<div class="desc" id="theater_1">' \
                        '<h2 class="name">' \
                            '<a href="/movies/?roxie">Roxie Theater</a>' \
                        '</h2>' \
                        '<div class="info">' \
                            'By Crackheads'\
                            '<a href target="_top"></a>' \
                        '</div>' \
                    '</div>' \
                    '<div class="showtimes">' \
                        '<div class="movie">' \
                            '<div class="name">' \
                                '<a href="fake.com">Two Cats One Bowl</a>' \
                            '</div>' \
                            '<span class="info">' \
                                '<a href="/url?q=http://www.imdb.com/title/meow" />' \
                            '</span>' \
                            '<div class="times">' \
                                '<span style="color:#666"><span style="padding:0 "></span><!-- -->2:00pm</span>' \
                            '</div>' \
                        '</div>' \
                        '<div class="movie">' \
                            '<div class="name">' \
                                '<a href="fake.com">Something Really Obscure</a>' \
                            '</div>' \
                            '<span class="info">Documentary, 55 minutes, Mandarin with Esperanto subtitles</span>' \
                            '<div class="times">' \
                                '<span style="color:#666"><span style="padding:0 "></span><!-- -->7:20pm</span>' \
                                '<span style="color:#666"><span style="padding:0 "></span><!-- -->9:45pm</span>' \
                            '</div>' \
                        '</div>' \
                    '</div>' \
                '</div>' \
            '</div>'

def fetch_html(use_fake = False):
    if use_fake:
        return fake_data
    else:
        url = 'https://www.google.com/movies?near=94110'
        req = requests.get(url)
        data = req.text
        return data
