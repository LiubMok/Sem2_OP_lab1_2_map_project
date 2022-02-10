"""
Module that generates html card
"""
import webbrowser

import folium

from containers.data_cont import DataCont


class HtmlCreator:
    """
    Class for the map to create html maps with different feature groups.
    """

    def __init__(self, sorted_location, parsed_info):
        """
        Creating custom classes allows us to define new types of objects with particular
        attributes and functionalities specific to our work needs.
        :param sorted_location: list with sorted info.
        :param parsed_info: class with location from input.
        """
        self._sorted_location = sorted_location
        self.parsed_info = parsed_info

    def _create_feature_group(self, location_or_coord, title_name):
        """
        A universal method for creating feature groups
        :param location_or_coord: name of the location or coordinates as a tooltip.
        :param title_name: name of the feature group.
        :return:feature group.
        """
        fg = folium.FeatureGroup(name=title_name)
        for elem in self._sorted_location:
            elem: DataCont = elem
            if elem.get_movie_distance_to_point() <= 100:
                col = 'blue'
            elif elem.get_movie_distance_to_point() <= 1000:
                col = 'orange'
            else:
                col = 'red'
            fg.add_child(folium.Marker(
                elem.get_movie_location_coord(),
                popup=elem.get_movie_name(),
                tooltip=elem.get_movie_location_name() if location_or_coord == 'loc_name'
                else elem.get_movie_location_coord(),
                icon=folium.Icon(color=col)))
        return fg

    def open_html_in_browser(self, path_to_html_file):
        url = f'file:///{path_to_html_file}'
        webbrowser.open(url, new=2)

    def create(self):
        """
        A method for creating marks on a map
        :return: html map.
        """
        map_m = folium.Map(list(self.parsed_info), zoom_start=4)
        fg_loc = self._create_feature_group('loc_name', 'City names')
        fg_cords = self._create_feature_group('coords', 'Location coordinates')

        map_m.add_child(fg_loc)
        map_m.add_child(fg_cords)
        map_m.add_child(folium.LayerControl())
        map_m.save("Map_film.html")
        self.open_html_in_browser("Map_film.html")
