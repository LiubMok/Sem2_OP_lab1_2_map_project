from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter

from modules.cache_geolocation_manager import CacheGeolocationManagerList

class GeoManager:

    def __init__(self, cache_geolocation_manager: CacheGeolocationManagerList) -> None:
        self.cache_geolocation = cache_geolocation_manager

    def _join_in_str(self, list):
        return ''.join(list).rstrip(',')

    # TODO: rename!
    def _find_coords(self, scope_data):
        geolocator = Nominatim(user_agent="University")
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
        if self.cache_geolocation.check(scope_data):
            return self.cache_geolocation.get(scope_data)
        founded_result = geolocator.geocode(scope_data)
        if founded_result is not None:
            tuple_coord = (founded_result.latitude, founded_result.longitude)
            self.cache_geolocation.add(scope_data, tuple_coord)
            return tuple_coord
        else:
            return None

    def find_coords(self, location_name):
        splited_by_dot = location_name.split(';')
        for count in range(len(splited_by_dot)):
            data_to_find = splited_by_dot[count:]
            founded_coords = self._find_coords(self._join_in_str(data_to_find))
            if founded_coords is not None:
                return founded_coords[0], founded_coords[1]
            else:
                print("None")
        return tuple((0, 0))
