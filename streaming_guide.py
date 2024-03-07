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
        self._streaming_services = []

    def add_streaming_service(self, streaming_service):
        self._streaming_services.append(streaming_service)

    def delete_streaming_service(self, name):
        for service in self._streaming_services:
            if service.get_name() == name:
                self._streaming_services.remove(service)
                break

    def where_to_watch_movie(self, title):
        for service in self._streaming_services:
            catalog = service.get_catalog()
            if title in catalog:
                available_services = [f'{title} ({catalog[title].get_year()})'] + [service.get_name() for service in self._streaming_services if title in service.get_catalog()]
                return available_services

        return None