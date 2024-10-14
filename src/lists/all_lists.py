from __future__ import annotations

import customtkinter as ctk
from PIL import Image
from tkinter.messagebox import showerror

from src.create.create_list import CreateList
from src.open.open_list import OpenList
from src.top.top_lvl_pages import ConfirmationPage, EditNameShoppingList
from src.load.save_and_load_data import SaveAndLoadData as sld
from src.lists.config_all_lists import *


class ScrollAllLists(ctk.CTkScrollableFrame):
    """
    Класс- контейнер, формирует область со скролом для добавления списков покупок
    """
    def __init__(self, main_window: AllLists, *args,  **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window
        self.__list_checkboxes = []

        self.__load_checkbox_shopping_lists()



class MenuButtonsAllLists(ctk.CTkFrame):
    """
    Класс- контейнер, формирует область с кнопками, отвечающими за функционал страницы
    """
    def __init__(self, main_window: AllLists, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window

        self.__label_add_list = None

        self.__config_label_add_list()
        self.__config_add_list_button()
        self.__config_menu_buttons()


class AllLists(ctk.CTkToplevel):
    """
    Мэйн класс страницы, в себе формирует основной контейнер (фрейм), содержащий остальные виджеты страницы, а так же основную логику страницы
    """
    def __init__(self, main_window):
        super().__init__()
        self.__main_window = main_window

        self.__load_data = sld.read_data_with_shopping_lists() if sld.check_file_shopping_lists() else {}
        self.__load_data_purchase_history = sld.read_data_with_purchase_history() if sld.check_file_purchase_history() else {}

        self.__create_shopping_list_page = None
        self.__confirmation_request_page = None
        self.__edit_name_shopping_list_page = None
        self.__open_list_page = None

        self.__scroll_all_lists = None
        self.__meny_btn_all_lists = None

        self.__config_window()
        self.__config_logo()
        self.__config_scroll_frame()
        self.__config_menu_buttons()