# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 03/15/2024
# Description: Project 10

class Movie:
    "'an init method that takes as arguments the title, genre, director, and year'"
    def __init__(self, title, genre, director, year):
        "'assigns the parameters to the data members'"
        self.__title = title
        self.__genre = genre
        self.__director = director
        self.__year = year

    "'get methods for each of the data members'"
    "'get method for the title'"
    def get_title(self):
        return self.__title

    "'get method for the genre'"
    def get_genre(self):
        return self.__genre

    "'get method for the director'"
    def get_director(self):
        return self.__director

    "'get method for the year'"
    def get_year(self):
        return self.__year

    def __str__(self):
        return self._title+"("+str(self._year)+"), Director: "+self._director+", Genre: "+self._genre"

"'write a class named StreamingService'"
class StreamingService:
    "'an init method that takes the name as an argument'"
    def __init__(self, name):
        "'assigns the parameter to the name data member'"
        self.__name = name
        "'the catalog data member should be empty'"
        self.__catalog = []

    "'get methods for each of the data members'"
    "'get method for the name'"
    def get_name(self):
        return self.__name

    "'get method for the catalog'"
    def get_catalog(self):
        return self.__catalog

    "'method named add_movie that takes a Movie object as an argument'"
    def add_movie(self, movie):
        # add the movie to the catalog
        self.__catalog.append(movie)

    "'method named delete_movie that takes a movie title as an argument'"
    def delete_movie(self, movie_title):
        "'check if the given movie title is present in the catalog'"
        for m in self.__catalog:
            "'remove the movie from the catalog if the movie does exist in it'"
            if m.get_title() == movie_title:
                self.__catalog.remove(m)

"'write a class named StreamingGuide'"
class StreamingGuide:
    "'an init method that takes no arguments'"
    def __init__(self):
        "'initializes the services data member to an empty list'"
        self._services = []

    "'method called add_streaming_service that takes a StreamingService object as an argument'"
    def add_streaming_service(self, stream_service):
        "'add the stream_service to the services list'"
        self._services.append(stream_service)

    "'method named delete_streaming_service that takes the name of a streaming service as an argument'"
    def delete_streaming_service(self, service_name):
        # check if the service is already present in the guide
        for s in self._services:
            # remove the service from the guide if it does exist in the guide
            if s.get_name() == service_name:
                self._services.remove(s)

    "'method named where_to_watch_movie that takes a movie title as an argument'"
    def where_to_watch_movie(self, movie_title):
        "'create an empty result_guide list'"
        result_guide = []
        firstFound = False

        "'check each service in the list'"
        for i in range(len(self._services)):
            "'get the catalog of each service in the guide'"
            catalog = self._services[i].get_catalog()
            "'check each movie in the catalog'"
            for m in catalog:
                "'when a match is found in the catalog'"
                if m.get_title() == movie_title:
                    "'when first match is found'"
                    if firstFound == False:
                        "'concatenate name & year of the movie (with the year in parentheses)'"
                        movie = movie_title + '('+str(m.get_year())+')'
                        "'append the movie as the first record in the result_guide'"
                        result_guide.append(movie)
                        "'set firstFound to true'"
                        firstFound = True
                    "'also append the service's name in the result_guide list'"
                    result_guide.append(self._services[i].get_name())

        "'return the result_guide list of where to watch the given movie'"
        if firstFound == True:
            return result_guide

        "'return None if no service is found'"
        return None
