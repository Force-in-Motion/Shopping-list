from __future__ import annotations

import customtkinter as ctk
from tkinter.messagebox import showerror
from tkinter import END
from PIL import Image

from src.create.config_create_list import *
from src.load.save_and_load_data import SaveAndLoadData as sld
from src.top.top_lvl_pages import AddNewCategory, EditProduct, ConfirmationPage
from src.templates.templates import Templates



class ScrollCreateList(ctk.CTkScrollableFrame):
    """
    Класс- контейнер, формирует область со скроллом для добавления товаров
    """


class ConfigCreateList(ctk.CTkFrame):
    """
    Класс- контейнер для виджетов, которые формируют конфигурацию и составляющие списка покупок,
    Такие как название списка, название товара, категория и его количество, а так же логотип приложения
    """


class MenuButtonsCreateList(ctk.CTkFrame):
    """
    Класс- контейнер, формирует область с кнопками, отвечающими за функционал страницы
    """



class CreateList(ctk.CTkToplevel):
    """
    Мэйн класс страницы, в себе формирует контейнеры (фреймы), содержащие остальные виджеты страницы,
    А так же содержит основную логику, отвечающую за функционал страницы
    """