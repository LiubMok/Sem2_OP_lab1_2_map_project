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
        founded_coords = geolocator.geocode(scope_data)
        self.cache_geolocation.add(scope_data, founded_coords)
        return founded_coords

    def find_coords(self, location_name):
        splited_by_dot = location_name.split(';')
        for count in range(len(splited_by_dot)):
            data_to_find = splited_by_dot[count:]
            founded_coords = self._find_coords(self._join_in_str(data_to_find))
            if founded_coords is not None:
                return founded_coords.latitude, founded_coords.longitude
            else:
                print("None")
        return tuple((0, 0))
