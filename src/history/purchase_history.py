from __future__ import annotations
from tkinter.messagebox import showerror, showinfo
import customtkinter as ctk
from PIL import Image

from src.history.config_purchase_history import *
from src.top.top_lvl_pages import ConfirmationClearScrollPlace, ConfirmationPage, ViewListPurchaseHistory
from src.load.save_and_load_data import SaveAndLoadData as sld



class ScrollPurchaseHistory(ctk.CTkScrollableFrame):
    """
    Класс- контейнер, формирует область со скролом для работы с добавленными товарами
    """



class ButtonsMenuPurchaseHistory(ctk.CTkFrame):
    """
    Класс- контейнер, формирует область с кнопками, отвечающими за функционал страницы
"""


class PurchaseHistory(ctk.CTkToplevel):
    """
    Мэйн класс страницы, в себе формирует основные контейнеры (фреймы), содержащие остальные виджеты страницы, а так же основную логику страницы
    """