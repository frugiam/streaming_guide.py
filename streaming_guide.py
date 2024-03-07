# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 03/15/2024
# Description: Project 10

class Movie:
    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

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

    def get_name(self):
        return self._name

    def get_catalog(self):
        return self._catalog

    def add_movie(self, movie):
        self._catalog[movie.get_title()] = movie

    def delete_movie(self, title):
        if title in self._catalog:
            del self._catalog[title]


class StreamingGuide:
    def __init__(self):
        self._listofservices = []

    def add_streaming_service(self, service):
        self._listofservices.append(service)

    def delete_streaming_service(self, name):
        for service in self._listofservices:
            if service.get_name() == name:
                self._listofservices.remove(service)
                break

    def where_to_watch(self, title):
        result = []
        for service in self._listofservices:
            if title in service.get_catalog():
                result.append(service.get_name())
        if len(result) == 0:
            return None
        else:
            movie = service.get_catalog()[title]
            result.insert(0, f"{movie.get_title()} ({movie.get_year()})")
            return result