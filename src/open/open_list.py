from __future__ import annotations

from PIL import Image
import customtkinter as ctk
from tkinter.messagebox import showerror, showinfo


from src.lists.all_lists import *
from src.load.save_and_load_data import SaveAndLoadData as sld
from src.open.config_open_list import *
from src.top.top_lvl_pages import AddProduct, EditProduct, ConfirmationPage



class ScrollOpenListProducts(ctk.CTkScrollableFrame):
    """
    Класс- контейнер, формирует область со скролом для работы с добавленными товарами либо для добавления новых
    """

    def __init__(self, main_window: OpenList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window
        self.__list_checkboxes = []

        self.__list_name = None

        self.__load_checkbox_products()



class MenuButtonsOpenList(ctk.CTkFrame):
    """
    Класс- контейнер, формирует область с кнопками, отвечающими за функционал страницы
    """

    def __init__(self, main_window: OpenList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window
        self.__label_add_product = None

        self.__config_menu_buttons()
        self.__config_label_add_product_in_list()
        self.__config_label_add_product_in_favorite()



class OpenList(ctk.CTkToplevel):
    """
    Мэйн класс страницы, в себе формирует основные контейнеры (фреймы), содержащие остальные виджеты страницы
    """

    def __init__(self, main_window: AllLists, scroll_all_lists: ScrollAllLists):
        super().__init__()
        self.__main_window = main_window

        self.__load_data = sld.read_data_with_shopping_lists() if sld.check_file_shopping_lists() else {}
        self.__load_data_favorites = sld.read_data_with_favorites_products() if sld.check_file_favorites_products() else {
            "f": []}
        self.__list_categories = sld.read_categories()

        self.__scroll_all_lists = scroll_all_lists

        self.__list_products = []

        self.__category_product = None
        self.__scroll_open_list = None
        self.__menu_btn_open_list = None

        self.__add_product_page = None
        self.__edit_product_page = None
        self.__confirmation_request_page = None

        self.__config_window()
        self.__config_logo()
        self.__config_menu_buttons()
        self.__config_scroll_frame()
        self.__config_menu_sorted()