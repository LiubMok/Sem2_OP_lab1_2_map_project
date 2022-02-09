"""The main module which includes a call to all other
modules and start the program
"""

from modules.arg_manager import ArgManager
from modules.cache_geolocation_manager import CacheGeolocationManagerList
from modules.coord_manager import CoordManager
from modules.geolocation_manager import GeoManager
from modules.html_creator import HtmlCreator
from modules.location_file_parse import LocationFileParser
from modules.location_manager import LocationManager


def main():
    """
    The main function that receives startup data and calls child modules.
    """
    args = ArgManager().get_args()
    file_parse = LocationFileParser(args.get_file_full_path())
    parsed_data = file_parse.get_parsed_data()
    rating = LocationManager(
        args.get_year(),
        parsed_data,
        args.get_coord(),
        GeoManager(CacheGeolocationManagerList()),
        CoordManager()
    ).get_location_rating()
    HtmlCreator(rating, args.get_coord()).create()


if __name__ == '__main__':
    main()
