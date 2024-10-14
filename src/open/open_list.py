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