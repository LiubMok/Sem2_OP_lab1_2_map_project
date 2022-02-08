from geopy.distance import great_circle


class CoordManager:

    def get_distance(self, coord_input: tuple, coord_variable: tuple) -> float:
        return round(great_circle(coord_input, coord_variable).km, 2)
