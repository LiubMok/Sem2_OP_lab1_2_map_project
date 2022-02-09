"""
The module acts as a container in which information is added or removed.
"""


class DataCont:
    """
    Class that is responsible for storing and transferring information to other
    classes, to avoid direct interaction between information.
    """
    def __init__(self, movie_name, movie_year, movie_location_name) -> None:
        """
        Creating custom classes allows us to define new types of objects with particular
        attributes and functionalities specific to our work needs.
        :param movie_name: name of the film.
        :param movie_year: year when film eas taken.
        :param movie_location_name: place where film was taken.
        """
        self._movie_distance_to_point = None
        self._movie_location_coord: tuple = None
        self._movie_location_name = movie_location_name
        self._movie_year = movie_year
        self._movie_name = movie_name

    def get_movie_name(self):
        """
        Typical getter for self._movie_name
        :return: name of the movie.
        """
        return self._movie_name

    def get_movie_year(self):
        """
        Typical getter for self._movie_year
        :return: year when the film was taken.
        """
        return self._movie_year

    def get_movie_location_name(self):
        """
        Typical getter for self._movie_location_name
        :return:place where film was taken.
        """
        return self._movie_location_name

    def get_movie_distance_to_point(self):
        """
        Typical getter for self._movie_distance_to_point
        :return: distance between two points.
        """
        return self._movie_distance_to_point

    def set_movie_distance_to_point(self, distance_to_point):
        """
        Typical setter for
        :param distance_to_point:
        :return:
        """
        self._movie_distance_to_point = distance_to_point

    def get_movie_location_coord(self):
        """
        Typical getter for self._movie_location_coord
        :return: coordinates where film was taken.
        """
        return self._movie_location_coord

    def set_movie_location_coord(self, location_coords):
        """
        Typical setter for
        :param location_coords:
        :return:
        """
        self._movie_location_coord = location_coords

    def to_string(self):
        return f"{self._movie_name}, {self._movie_year}, {self._movie_location_name}, {self._movie_location_coord}, {self._movie_distance_to_point} "
