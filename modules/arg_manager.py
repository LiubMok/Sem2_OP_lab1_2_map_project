import argparse as arg

from containers.arg_cont import ArgCont


class ArgManager:
    def _parse_arg(self):
        pass

    def get_args(self) -> ArgCont:
        parser = arg.ArgumentParser()
        parser.add_argument('year', type=str, help='the year when film was taken.')
        parser.add_argument('latitude', type=float, help='first part of coordinate(широта).')
        parser.add_argument('longitude', type=float, help='second part of coordinates(довгота).')
        parser.add_argument('data_file_path', type=str, help='name of file with data base.')
        argps = parser.parse_args()
        year = argps.year
        latitude = argps.latitude
        longitude = argps.longitude
        data_path = argps.data_file_path
        print((latitude, longitude))
        arg_container = ArgCont(year, (latitude, longitude), data_path)
        return arg_container
