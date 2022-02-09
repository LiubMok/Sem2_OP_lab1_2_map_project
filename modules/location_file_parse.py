import codecs
import time

from containers.data_cont import DataCont


class LocationFileParser:
    def __init__(self, file_f_path):
        self._file_path = file_f_path

    # def get_utf_encoded_file(self) -> str:
    #     blockSize = 1048576
    #     with codecs.open(self._file_path, "r", encoding="mbcs") as sourceFile:
    #         with codecs.open("data_base.txt", "w", encoding="UTF-8") as targetFile:
    #             while True:
    #                 contents = sourceFile.read(blockSize)
    #                 if not contents:
    #                     break
    #                 targetFile.write(contents)
    #     return "data_base.txt"

    def get_parsed_data(self):
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
                    # time.sleep(1)
                    result_list.append(DataCont(result[0], result[1], result[2]))
                except IndexError:
                    print("error")

            # with open('location_base.csv', 'w', encoding='utf-8') as file_2:
            #     file_2.write('Film,Year,Location\n')
            #     for l_ine in final:
            #         for element in l_ine:
            #             if l_ine[-1] == element:
            #                 file_2.write(element)
            #             else:
            #                 file_2.write(element + ',')
            #         file_2.write('\n')
            return result_list
