from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter


class GeoManager:

    def find_coords(self, location_name):
        geolocator = Nominatim(user_agent="location_file_parse.py")
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
        if len(location_name.split(';')) > 3:
            loc = location_name.split(';')[-3:]
            location = geolocator.geocode(''.join(loc).rstrip(','))
            # print(tuple((location.latitude, location.longitude)))
            return tuple((location.latitude, location.longitude))
        else:
            location = geolocator.geocode(location_name)
            # print(tuple((location.latitude, location.longitude)))
            return tuple((location.latitude, location.longitude))
        # geolocator = Nominatim(user_agent="location_file_parse.py")
        # geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
        # loc = location_name.split(';')
        # iterator_of_unknown_places = 1
        # while True:
        #     location = geolocator.geocode(''.join(loc).rstrip(','))
        #     if location != None:
        #         print(tuple((location.latitude, location.longitude)))
        #         return tuple((location.latitude, location.longitude))
        #     else:
        #         loc = loc[iterator_of_unknown_places:]
        #         iterator_of_unknown_places += 1
