"""
The module is responsible for finding the distance.
"""
from geopy.distance import great_circle


class CoordManager:
    """
    This class contains a method for finding distances.
    """
    def get_distance(self, coord_input: tuple, coord_variable: tuple) -> float:
        """
        The method looks for the distance between two coordinates.
        :param coord_input: coordinates that are transmitted at program startup.
        :param coord_variable: variable coordinates from the sorted list
        :return: distance (in kilometers).
        """
        return round(great_circle(coord_input, coord_variable).km, 2)
