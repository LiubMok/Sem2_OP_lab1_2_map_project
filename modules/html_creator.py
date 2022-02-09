import folium

from containers.data_cont import DataCont


class HtmlCreator:
    def __init__(self, sorted_location, parsed_info):
        self._sorted_location = sorted_location
        self.parsed_info = parsed_info

    def _create_feature_group(self, l_c, title_name):
        fg_loc = folium.FeatureGroup(name=title_name)
        for elem in self._sorted_location:
            elem: DataCont = elem
            if elem.get_movie_distance_to_point() <= 100:
                col = 'blue'
            elif elem.get_movie_distance_to_point() <= 1000:
                col = 'orange'
            else:
                col = 'red'
            fg_loc.add_child(folium.Marker(
                elem.get_movie_location_coord(),
                popup=elem.get_movie_name(),
                tooltip=elem.get_movie_location_name() if l_c == 'loc_name'
                else elem.get_movie_location_coord(),
                icon=folium.Icon(color=col)))
        return fg_loc

    def create(self):
        map_m = folium.Map(list(self.parsed_info), zoom_start=4)
        fg_loc = self._create_feature_group('loc_name', 'City names')
        fg_cords = self._create_feature_group('coords', 'Location coordinates')

        map_m.add_child(fg_loc)
        map_m.add_child(fg_cords)
        map_m.add_child(folium.LayerControl())
        map_m.save("Map_film.html")
