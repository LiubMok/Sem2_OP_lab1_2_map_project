import pandas as pd
from operator import itemgetter


class LocationManager:

    def __init__(self, year, location_data, coord_man, geo_maneger, geo_distance) -> None:
        self._year = year
        self._location_data = location_data
        self._coord_man = coord_man
        self.geo_maneger = geo_maneger
        self.geo_distance = geo_distance

    def _get_year_rating(self):
        data = pd.read_csv(self._location_data)
        result = []
        number_of_line = 0
        for years in data['Year']:
            if str(years) == self._year:
                data_new = str(data.loc[[number_of_line]]).split('\n')[1].split('#')[1].split('  ')
                fc = self.geo_maneger.find_coords(data_new[-1])
                dist = self.geo_distance.get_distance(self._coord_man, fc)
                data_new.append(fc)
                data_new.append(dist)
                result.append(data_new)
            number_of_line += 1

        return result

    def get_location_rating(self):
        year_sorted_list = self._get_year_rating()
        if len(year_sorted_list) > 10:
            return sorted(year_sorted_list, key=itemgetter(-1), reverse=True)[-10:]
        else:
            return sorted(year_sorted_list, key=itemgetter(-1), reverse=True)
