"""
A module that acts as a cache.
"""

from containers.data_cont import DataCont


class CacheGeolocationManagerList:
    """
    A class that creates, complements, or checks for already
    added coordinates in the cache dictionary.
    """

    def __init__(self) -> None:
        """
        The method creates a dictionary when the module is called for the first time.
        """
        self.cache_data: dict = {}

    def add(self, loc_name: str, coord: tuple):
        """
        The method adds new unique data to the cache dictionary.
        :param loc_name: the name of the location as a key.
        :param coord: coordinates as values.
        """
        # print(f"cache add: {loc_name} -> {coord}")
        self.cache_data[loc_name] = coord

    def get(self, loc_name: str) -> tuple:
        """
        The method returns the value of the dictionary by key.
        :param loc_name: the name of the location as a key
        :return: the value of the dictionary by key
        """
        # print(f"cache get: {loc_name}")
        return self.cache_data[loc_name]

    def check(self, loc_name: str) -> bool:
        """
        The method checks if there is a key with a value in the cache dictionary.
        :param loc_name: the name of the location as a key.
        :return: boolean depending on whether there is a key or not.
        """
        # print(loc_name)
        # time.sleep(1)
        is_inside = loc_name in self.cache_data.keys()
        print(f"cache check: {loc_name} -> {is_inside}")
        return is_inside
