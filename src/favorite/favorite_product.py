from __future__ import annotations

from tkinter.messagebox import showerror

import customtkinter as ctk
from PIL import Image

from src.favorite.config_favorite_products import *
from src.load.save_and_load_data import SaveAndLoadData as sld
from src.top.top_lvl_pages import ConfirmationClearScrollPlace, ConfirmationPage, AddProduct


class ScrollFavoriteProducts(ctk.CTkScrollableFrame):
    """
    Класс- контейнер, формирует область со скролом для добавления товаров
    """



class MenuButtonsFavoriteProducts(ctk.CTkFrame):
    """
    Класс- контейнер, формирует область с кнопками, отвечающими за функционал страницы
    """



class FavoriteProducts(ctk.CTkToplevel):
    """
    Мэйн класс страницы, в себе формирует основные контейнеры (фреймы), содержащие остальные виджеты страницы, а так же основную логику страницы
    """