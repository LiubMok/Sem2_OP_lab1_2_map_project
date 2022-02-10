"""
A module that acts as a cache.
"""

from csv import DictWriter


class CacheGeolocationManagerList:
    """
    A class that creates, complements, or checks for already
    added coordinates in the cache dictionary.
    """

    def __init__(self) -> None:
        """
        Creating custom classes allows us to define new types of objects with particular
        attributes and functionalities specific to our work needs.
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
        # print(f"cache check: {loc_name} -> {is_inside}")
        return is_inside


class CacheGeolocationManagerFileSave:
    """
    Class for saving or checking info in cache file.
    """

    def __init__(self) -> None:
        """
        Creating custom classes allows us to define new types of objects with particular
        attributes and functionalities specific to our work needs.
        """
        self.get_count = 0

        self.saved_cache_filename = "saved_cache.csv"
        self.cache_data: dict = {}
        self._load_saved_cache()
        # print(self.cache_data)
        print(f"Loaded {len(self.cache_data)} cached lines")

    def add(self, loc_name, coord):
        """
        The method adds new unique data to the cache dictionary.
        :param loc_name: the name of the location as a key.
        :param coord: coordinates as values.
        """
        self.get_count += 1
        # print(f"location_checked -> {self.get_count} : cache add: {loc_name} -> {coord}")
        self._save_to_cache(loc_name, coord)
        self.cache_data[loc_name] = coord

    def get(self, loc_name):
        """
        The method returns the value of the dictionary by key.
        :param loc_name: the name of the location as a key
        :return: the value of the dictionary by key
        """
        # print(f"cache get: {loc_name}")
        self.get_count += 1
        return self.cache_data[loc_name]

    def check(self, loc_name):
        """
        The method checks if there is a key with a value in the cache dictionary.
        :param loc_name: the name of the location as a key.
        :return: boolean depending on whether there is a key or not.
        """
        is_inside = loc_name in self.cache_data.keys()
        # print(f"cache check: {loc_name} -> {is_inside}")
        return is_inside

    def _save_to_cache(self, movie_name, coord):
        """
        A method that writes a cache to a file for faster work in the future.
        :param movie_name: name of the film.
        :param coord: coordinates where film was taken.
        """
        field_names = ['NAME', 'LOCATION_COORD']

        line_to_save = {
            "NAME": movie_name,
            'LOCATION_COORD': f"{coord[0]}, {coord[1]}" if "None" not in coord else coord
        }

        with open(self.saved_cache_filename, 'a') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)
            dictwriter_object.writerow(line_to_save)
            f_object.close()

    def _load_saved_cache(self):
        """
        Method read cache file in the start of the program.
        """
        def clean(word):
            return word.replace("\'", "").replace("\"", "")

        with open(self.saved_cache_filename) as file:
            content = file.readlines()
        header = content[:1]
        rows = content[1:]
        for line in rows:
            if len(line) > 1:
                split_data = line.split(",")
                location_name = split_data[0]

                # If location can`t be founded -> value = None
                if "None" not in split_data[1]:
                    tuple_location_coord = (clean(split_data[1]), clean(split_data[2]))
                else:
                    tuple_location_coord = None

                self.cache_data[location_name] = tuple_location_coord
