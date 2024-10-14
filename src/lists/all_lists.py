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



