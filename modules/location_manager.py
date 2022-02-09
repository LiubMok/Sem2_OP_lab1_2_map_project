"""
The module that forms the final list of data from which the map will be built.
"""


class LocationManager:
    """
    Class that is responsible for processing pre-parsed data and preparing
    information for map construction.
    """

    def __init__(self, year: str, location_data: list, coord_man, geo_manager, geo_distance) -> None:
        """
        Creating custom classes allows us to define new types of objects with particular
        attributes and functionalities specific to our work needs.
        :param year: year when film should had been taken.
        :param location_data: list of pre-parsed data.
        :param coord_man: coordinates to which the distance will be searched.
        :param geo_manager: class GeoManager.
        :param geo_distance: class CoordManager.
        """
        self._scoped_year = year
        self._location_data: list = location_data
        self._scope_coord = coord_man
        self.geo_manager = geo_manager
        self.geo_distance = geo_distance

    def _get_year_rating(self):
        """
        A method that returns a list of only those movies that were shot in self._scoped_year
        and adds the coordinates of the movies shot
        and adds distance to the self._scope_coord.
        :return: returns unsorted data that will be used to build the map.
        """
        result = []
        for data in self._location_data:
            if str(data.get_movie_year()) == self._scoped_year:
                fc = self.geo_manager.find_coords(data.get_movie_location_name())
                dist = self.geo_distance.get_distance(self._scope_coord, fc)
                data.set_movie_location_coord(fc)
                data.set_movie_distance_to_point(dist)
                # print(data)
                result.append(data)

        return result
    # TODO: doctest!!!
    def get_location_rating(self):
        """
        A method that sorts data from the _get_year_rating method.
        :return: sorted _get_year_rating data and sliced as needed.
        """
        movies = self._get_year_rating()
        movies.sort(key=lambda x: x.get_movie_distance_to_point(), reverse=True)
        sorted_list = movies
        if len(sorted_list) > 10:
            return sorted_list[-10:]
        else:
            return sorted_list
