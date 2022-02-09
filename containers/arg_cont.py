"""
This module serves as a contour for input information.
"""


class ArgCont:
    """
    The class contains a set of methods that return various information.
    """
    def __init__(self, year: int, coord: tuple, file_path: str) -> None:
        """
        Creating custom classes allows us to define new types of objects with particular
        attributes and functionalities specific to our work needs.
        :param year: year when film should be taken.
        :param coord: coordinates to which we should find distance.
        :param file_path: path to the file where is all info about films.
        """
        self._year = year
        self._coord = coord
        self._file_path = file_path

    def get_year(self) -> int:
        """
        Typical getter for self._year
        :return: year when film should be taken.
        """
        return self._year

    def get_coord(self) -> tuple:
        """
        Typical getter for self._coord
        :return: coordinates to which we should find distance.
        """
        return self._coord

    def get_file_full_path(self) -> str:
        """
        Typical getter for self._file_path
        :return:path to the file where is all info about films
        """
        return self._file_path
