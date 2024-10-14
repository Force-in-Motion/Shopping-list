import customtkinter as ctk
from PIL import Image
from tkinter.messagebox import showerror

from src.top.config_top_level_pages import *
from src.load.save_and_load_data import SaveAndLoadData as sld
from src.templates.templates import Templates

class AddNewCategory(ctk.CTkToplevel):
    """
    Класс, описывающий функционал окна верхнего уровня и его виджеты
    """
    def __init__(self, main_window, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.__main_window = main_window
        self.__list_categories = sld.read_categories()

        self.__input_field = None

        self.__config_logo()
        self.__config_window()
        self.__config_input_field()
        self.__config_menu_buttons()