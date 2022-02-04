from modules.arg_manager import ArgManager
from modules.coord_manager import CoordManager
from modules.html_creator import HtmlCreator
from modules.location_file_parse import LocationFileParser
from modules.location_manager import LocationManager


def main():
    args = ArgManager().get_args()
    file_parse = LocationFileParser(args.get_file_full_path())
    data = file_parse.get_parsed_data()
    rating = LocationManager(args.get_year(), data, CoordManager()).get_location_rating()
    HtmlCreator(rating).create()


if __name__ == '__main__':
    main()
