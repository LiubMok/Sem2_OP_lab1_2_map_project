import folium


class HtmlCreator:
    def __init__(self, sorted_location, parsed_info):
        self._sorted_location = sorted_location
        self.parsed_info = parsed_info

    def create(self):
        map = folium.Map(list(self.parsed_info), zoom_start=4)

        for i in self._sorted_location:
            if i[4] < 1000:
                folium.Marker(i[3], popup=i[0], tooltip=i[2], icon=folium.Icon(color="blue")).add_to(map)
            else:
                folium.Marker(i[3], popup=i[0], tooltip=i[2], icon=folium.Icon(color="red")).add_to(map)
        map.save("Map_fuck.html")

