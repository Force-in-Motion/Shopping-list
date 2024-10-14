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


    @staticmethod
    def check_file_favorites_products() -> bool:
        """
        Проверяет наличие файла txt по указанному пути, в данном случае в папке
        :return: True или False
        """
        file = path_dir + r'\favorites_products.json'
        if os.path.isfile(file):
            return True
        else:
            return False


    @staticmethod
    def check_file_purchase_history() -> bool:
        """
        Проверяет наличие файла txt по указанному пути, в данном случае в папке
        :return: True или False
        """
        file = path_dir + r'\purchase_history.json'
        if os.path.isfile(file):
            return True
        else:
            return False


    @staticmethod
    def read_data_with_shopping_lists() -> dict:
        """
        Считывает и возвращает данные из файла shopping_lists.json
        """
        with open(path_dir + r'\shopping_lists.json', 'r') as f:
            load_data = json.load(f)
            return load_data


    @staticmethod
    def write_data_in_shopping_lists(load_data) -> bool:
        """
        Записывает полученные данные в файл shopping_lists.json
        Возвращает True
        """
        with open(path_dir + r'\shopping_lists.json', 'w') as f:
            json.dump(load_data, f, ensure_ascii=False, indent=4)
            return True


    @staticmethod
    def read_data_with_favorites_products() -> dict:
        """
        Считывает и возвращает данные из файла favorites_products.json
        """
        with open(path_dir + r'\favorites_products.json', 'r') as f:
            load_data = json.load(f)
            return load_data


    @staticmethod
    def write_data_in_favorites_products(load_data) -> bool:
        """
        Записывает полученные данные в файл favorites_products.json
        Возвращает True
        """
        with open(path_dir + r'\favorites_products.json', 'w') as f:
            json.dump(load_data, f, ensure_ascii=False, indent=4)
            return True