import codecs


class LocationFileParser:
    def __init__(self, file_f_path):
        self._file_path = file_f_path

    def get_utf_encoded_file(self) -> str:
        blockSize = 1048576
        with codecs.open(self._file_path, "r", encoding="mbcs") as sourceFile:
            with codecs.open("data_base.txt", "w", encoding="UTF-8") as targetFile:
                while True:
                    contents = sourceFile.read(blockSize)
                    if not contents:
                        break
                    targetFile.write(contents)
        return "data_base.txt"

    def get_parsed_data(self):
        file = open(self.get_utf_encoded_file(), 'r', encoding='utf-8')
        lines = file.readlines()[14:-1]
        final = []
        for line in lines:
            new_l = line.rstrip('\n').split('\t')
            new_line = new_l[0].split(' (')
            result = [new_line[0], new_line[1][:4], new_l[-2].replace(',', ';') if new_l[-1].endswith(')') else new_l[-1].replace(',', ';')]
            final.append(result)

        with open('location_base.csv', 'w', encoding='utf-8') as file_2:
            file_2.write('Film,Year,Location\n')
            for l_ine in final:
                for element in l_ine:
                    if l_ine[-1] == element:
                        file_2.write(element)
                    else:
                        file_2.write(element + ',')
                file_2.write('\n')
        return 'location_base.csv'
