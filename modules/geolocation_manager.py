"""
Module for finding coordinates and processing input data.
"""
from typing import Optional

import geopy
from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter

from modules.cache_geolocation_manager import CacheGeolocationManagerList


class GeoManager:
    """
    Coordinate class and auxiliary functions.
    """

    def __init__(self, cache_geolocation_manager: CacheGeolocationManagerList) -> None:
        """
        Creating custom classes allows us to define new types of objects with particular
        attributes and functionalities specific to our work needs.
        :param cache_geolocation_manager: class with cache.
        """
        self.cache_geolocation = cache_geolocation_manager

    def _join_in_str(self, list_to_convert: list) -> str:
        """
        An additional method for converting a list to str.
        :param list_to_convert: list to be covered.
        :return: string.
        >>> self._join_in_str(['New York', 'Nem Your', 'USA'])
        New York, Nem Your, USA
        >>> self._join_in_str(['Chicago', 'Illinois', 'USA'])
        Chicago, Illinois, USA
        """
        return ''.join(part_location + ', ' for part_location in list_to_convert).rstrip(', ')

    # TODO: rename
    def _find_coords(self, scope_data: str) -> Optional[tuple]:
        """
        Method for finding coordinates by location.
        :param scope_data: location.
        :return: coordinates ot None
        >>> self._find_coords('Los Angeles, California, USA')
        (34.0536909, -118.242766)
        >>> self._find_coords('Hudson Valley, New York, USA')
        (41.31611085, -74.12629189225156)
        """
        geolocator = Nominatim(user_agent="University")
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
        if self.cache_geolocation.check(scope_data):
            return self.cache_geolocation.get(scope_data)
        founded_result = geolocator.geocode(scope_data)
        if founded_result is not None:
            try:
                tuple_coord = (founded_result.latitude, founded_result.longitude)
                self.cache_geolocation.add(scope_data, tuple_coord)
                return tuple_coord
            except geopy.exc.GeocoderUnavailable:
                return None
        else:
            return None

    def find_coords(self, location_name: str) -> Optional[tuple]:
        """
        The method calls auxiliary methods and returns coordinates.
        :param location_name: name of the location where the film was taken.
        :return:coordinates
        >>> self.find_coords('Spiderhouse Cafe; Austin; Texas; USA')
        (30.2711286, -97.7436995)
        >>> self.find_coords('Jos Cafe; San Marcos; Texas; USA')
        (29.8826436, -97.9405828)
        """
        splited_by_dot = location_name.split(';')
        for count in range(len(splited_by_dot)):
            data_to_find = splited_by_dot[count:]
            founded_coords = self._find_coords(self._join_in_str(data_to_find))
            if founded_coords is not None:
                return founded_coords[0], founded_coords[1]
            else:
                print("None")
        return tuple((0, 0))
