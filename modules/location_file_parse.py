"""
This module decodes the input file and parses its information.
"""
import codecs
import time

from containers.data_cont import DataCont


class LocationFileParser:
    """
    The class that processes the input file.
    """
    def __init__(self, file_f_path):
        """
        Creating custom classes allows us to define new types of objects with particular
        attributes and functionalities specific to our work needs.
        :param file_f_path: path to the input file.
        """
        self._file_path = file_f_path

    def get_parsed_data(self) -> list:
        """
        The method that decodes and parses the file +
        generates a list of easy-to-handle information.
        :return: the file is rewritten in the list.
        """
        with codecs.open(self._file_path, "r", encoding="mbcs") as file:
            lines = file.readlines()[14:-1]
            result_list = []
            for line in lines:
                without_new_line = line.rstrip('\n').split('\t')
                new_line = without_new_line[0].split(' (')
                try:
                    result = [new_line[0], new_line[1][:4], without_new_line[-2]
                        .replace(',', ';') if without_new_line[-1]
                        .endswith(')') else without_new_line[-1]
                        .replace(',', ';')]
                    # print(result)
                    result_list.append(DataCont(result[0], result[1], result[2]))
                except IndexError:
                    print("error")
            return result_list
