# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 03/15/2024
# Description: Project 10

class Movie:
    def __init__(self, title, genre, director, year):
        "'since as mentioned in question all member variable should be private. they are starting with _(underscore)'"
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    "'getters for all 4 member variablesself.'"
    def get_title(self):
        return self._title

    def get_genre(self):
        return self._genre

    def get_director(self):
        return self._director

    def get_year(self):
        return self._year


class StreamingService:
    def __init__(self, name):
        self._name = name
        self._catalog = {}

    "'getters for name and catalog.'"
    def get_name(self):
        return self._name

    def get_catalog(self):
        return self._catalog

    "'a method named add_movie that takes a Movie object as an argument and adds it to the catalog.'"
    def add_movie(self, movie):
        self._catalog[movie.get_title()] = movie

    "'a method named delete_movie that takes a movie title as an argument and if that Movie is in the catalog, removes it.'"
    def delete_movie(self, title):
        if title in self._catalog:
            del self._catalog[title]


class StreamingGuide:
    def __init__(self):
        self._listOfservices = []

    def add_streaming_service(self, service):
        self._listOfservices.append(service)

    def delete_streaming_service(self, name):
        for service in self._listOfservices:
            if service.get_name() == name:
                self._listOfservices.remove(service)
                break

    def where_to_watch(self, title):
        result = []
        for service in self._listOfservices:
            if title in service.get_catalog():
                result.append(service.get_name())
        if len(result) == 0:
            "'if its not available in any of the streaming service it should return None.'"
            return None
        else:
            movie = service.get_catalog()[title]
            result.insert(0, f"{movie.get_title()} ({movie.get_year()})")
            return result


movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

stream_serv_1 = StreamingService('Netflick')
stream_serv_1.add_movie(movie_2)

stream_serv_2 = StreamingService('Hula')
stream_serv_2.add_movie(movie_1)
stream_serv_2.add_movie(movie_4)
stream_serv_2.delete_movie('The Seventh Seal')
stream_serv_2.add_movie(movie_2)

stream_serv_3 = StreamingService('Dizzy+')
stream_serv_3.add_movie(movie_4)
stream_serv_3.add_movie(movie_3)
stream_serv_3.add_movie(movie_1)

stream_guide = StreamingGuide()
stream_guide.add_streaming_service(stream_serv_1)
stream_guide.add_streaming_service(stream_serv_2)
stream_guide.add_streaming_service(stream_serv_3)
stream_guide.delete_streaming_service('Hula')
search_results = stream_guide.where_to_watch_movie('Little Women')
