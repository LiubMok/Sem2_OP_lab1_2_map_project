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
        >>> self.get_distance(tuple((34.0536909, -118.242766)), tuple((49.83826, 24.02324)))
        9973.48
        >>> self.get_distance(tuple((30.26740345, -97.73958582383372)), tuple((49.83826, 24.02324)))
        9420.75
        """
        return round(great_circle(coord_input, coord_variable).km, 2)
