import customtkinter as ctk
from PIL import Image
import sys

from src.start.config_main_page import *
from src.lists.all_lists import *
from src.create.create_list import *
from src.favorite.favorite_product import *
from src.history.purchase_history import *
from src.open.open_list import *


class MainFrame(ctk.CTkFrame):
    """
    Класс, реализующий главное окно приложения
    """
    def __init__(self, main_window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window

        self.__config_logo()
        self.__config_menu_buttons()
        self.__config_exit_button()



class MainPage(ctk.CTk):
    """
    Мэйн класс приложения, в себе формирует основной контейнер (фрейм), содержащий остальные виджеты страницы
    """
    def __init__(self):
        super().__init__()
        self.__load_data = sld.read_data_with_shopping_lists() if sld.check_file_shopping_lists() else {}

        self.__add_list_page = None
        self.__all_lists_page = None
        self.__history_page = None
        self.__favorite_products_page = None

        self.__config_window()
        self.__config_main_frame()