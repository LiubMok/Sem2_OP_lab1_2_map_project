class ArgCont:
    def __init__(self, year: int, coord: tuple, file_path: str) -> None:
        self._year = year
        self._coord = coord
        self._file_path = file_path

    def get_year(self) -> int:
        return self._year

    def get_coord(self) -> tuple:
        return self._coord

    def get_file_full_path(self) -> str:
        return self._file_path
