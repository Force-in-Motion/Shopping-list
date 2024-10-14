import json
import os
import os.path

class SaveAndLoadData:

    @staticmethod
    def create_folder() -> None:
        """
        Проверяет наличие папки по указанному адресу, если папка отсутствует то создает ее
        """
        if not os.path.isdir(path_dir):
            os.mkdir(path_dir)


    @staticmethod
    def check_file_shopping_lists() -> bool:
        """
        Проверяет наличие файла txt по указанному пути, в данном случае в папке
        :return: True или False
        """
        file = path_dir + r'\shopping_lists.json'
        if os.path.isfile(file):
            return True
        else:
            return False