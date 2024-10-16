from __future__ import annotations

import customtkinter as ctk
from PIL import Image
from tkinter.messagebox import showerror

from src.create.create_list import CreateList
from src.open.open_list import OpenList
from src.templates.templates import Templates
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


    def __load_checkbox_shopping_lists(self) -> None:
        """
        Обходит загруженные из файла данные и устанавливает в скролл фрейм чекбоксы с текстом,
        Взятым из названий списков покупок, а так же добавляет те же данные в список чекбоксов
        """
        for list_name in self.__main_window.load_data.keys():

            shopping_list = ctk.CTkCheckBox(self, text=f'{list_name}', font=ft_sl, hover_color=hc_sl, fg_color=fgc_sl, border_width=bw_sl)
            shopping_list.grid(sticky="w", padx=(10, 0), pady=10)

            self.__list_checkboxes.append(shopping_list)


    def add_new_checkbox(self, list_name: str) -> None:
        """
        Добавляет новый чекбокс в скролл фрейм с текстом полученным текстом, а так же добавляет те же данные в список чекбоксов
        :param list_name: Принимает название списка покупок
        :return: None
        """
        shopping_list = ctk.CTkCheckBox(self, text=f'{list_name}', font=ft_sl, hover_color=hc_sl, fg_color=fgc_sl, border_width=bw_sl)
        shopping_list.grid(sticky="w", padx=(10, 0), pady=10)

        self.__list_checkboxes.append(shopping_list)


    def set_new_text_for_checkbox(self, checkbox: ctk.CTkCheckBox,  new_text: str) -> None:
        """
        Устанавливает новый текст для чекбокса если он не существует
        :param checkbox: Принимает ссылку на чекбокс
        :param new_text: Принимает новый текст для чекбокса
        :return: None
        """
        if checkbox is not None:
            checkbox.configure(text=new_text)


    def create_list_select_checkboxes(self) -> list[ctk.CTkCheckBox]:
        """
        Обходит список чекбоксов скролл фрейма и формирует новый список только из активных чекбоксов
        :return: Возвращает список активных чекбоксов
        """
        list_select_checkboxes = [checkbox for checkbox in self.__list_checkboxes if checkbox.get() == 1]

        return list_select_checkboxes


    def create_list_text_select_checkbox(self) -> list [str]:
        """
        Обходит список чекбоксов скролл фрейма и формирует новый список из текста только активных чекбоксов
        :return: Возвращает список текста активных чекбоксов
        """
        list_select_texts = [checkbox.cget("text") for checkbox in self.__list_checkboxes if checkbox.get() == 1]

        return list_select_texts


    def delete_checkbox(self) -> None:
        """
        Внутри себя вызывает другую функцию, при помощи которой, получает список активных чекбоксов
        Обходит этот список и удаляет его элементы из скролл фрейма и из списка чекбоксов
        """
        for checkbox in self.create_list_select_checkboxes():
            checkbox.destroy()
            self.__list_checkboxes.remove(checkbox)


    def check_selected_checkbox(self) -> bool:
        """
        Обходит список чекбоксов, определяет активный чекбокс если такой имеется вернет True,
        Если в списке нет активных чекбоксов то возвращает False
        """
        for checkbox in self.__list_checkboxes:
            if checkbox.get() == 1:
                return True
        return False


    def get_selected_checkbox(self) -> (str, ctk.CTkCheckBox) or (None, None):
        """
        Обходит список чекбоксов, определяет активный чекбокс если такой имеется и возвращает кортеж из его текста и самого чекбокса,
        Если в списке нет активных чекбоксов то возвращает кортеж (None, None)
        :return:
        """
        for checkbox in self.__list_checkboxes:
            if checkbox.get() == 1:
                return checkbox.cget("text"), checkbox
        return None, None


    def reset_checkboxes(self) -> None:
        """
        Снимает галочки со всех чекбоксов.
        """
        for checkbox in self.__list_checkboxes:
            if self.check_selected_checkbox():
                checkbox.deselect()


    def __get_count_checkboxes(self) -> int:
        """
        Возвращает количество чекбоксов в скролл фрейме
        """
        return len(self.__list_checkboxes)


    def __get_list_checkboxes(self) -> list [ctk.CTkCheckBox]:
        """
        Возвращает список чекбоксов
        """
        return self.__list_checkboxes

    list_checkboxes = property(__get_list_checkboxes)

    count_checkboxes = property(__get_count_checkboxes)



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


    def __config_label_add_list(self) -> None:
        """
        Формирует в себе Лейбл - текстовую строку, отвечающую за описание кнопки добавления списка покупок, а так же устанавливает ее параметры и стили
        """
        self.__label_add_list = ctk.CTkLabel(self, text_color=tc, text=tt_lal, font=ft_lal)
        self.__label_add_list.place(relx=0.1, rely=0.14)


    def __config_add_list_button(self) -> None:
        """
        Формирует в себе кнопку, отвечающую за добавление списка покупок, а так же устанавливает ее параметры и стили
        """
        self.__add_list_image = ctk.CTkImage(light_image=Image.open(path_round_button), size=size_alb)
        self.__add_list = ctk.CTkButton(self, image=self.__add_list_image, width=wh_alb, height=ht_alb, text=tt_alb, fg_color=fgc_alb, hover_color=hc_alb)
        self.__add_list.place(relx=0.04, rely=0.1)
        self.__add_list.configure(command=self.__main_window.add_list_button_click_handler)


    def __config_menu_buttons(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же устанавливает его параметры и стили
        """
        self.__open_list = ctk.CTkButton(self, text=ol_tt, width=wh_m, fg_color=fgc_m, height=ht_m, text_color=tc_m,
                                         border_width=bw_m, hover_color=hc_m,font=ft_m)
        self.__open_list.place(relx=0.05, rely=0.65)
        self.__open_list.configure(command=self.__main_window.open_list_button_click_handler)

        self.__edit_list = ctk.CTkButton(self, text=el_tt, width=wh_m, fg_color=fgc_m, height=ht_m, text_color=tc_m,
                                         border_width=bw_m, hover_color=hc_m, font=ft_m)
        self.__edit_list.place(relx=0.375, rely=0.65)
        self.__edit_list.configure(command=self.__main_window.edit_list_button_click_handler)

        self.__del_list = ctk.CTkButton(self, text=dl_tt, width=wh_m, fg_color=fgc_m, height=ht_m, text_color=tc_m,
                                        border_width=bw_m, hover_color=hc_m, font=ft_m)
        self.__del_list.place(relx=0.705, rely=0.65)
        self.__del_list.configure(command=self.__main_window.del_list_button_click_handler)

        self.__cancel_btn = ctk.CTkButton(self, text=cl_tt, width=wh_m, fg_color=fgc_m, height=ht_m, text_color=tc_m,
                                       border_width=bw_m, hover_color=hc_m, font=ft_m)
        self.__cancel_btn.place(relx=0.705, rely=0.1)
        self.__cancel_btn.configure(command=self.__main_window.cancel_button_click_handler)



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

        self.protocol("WM_DELETE_WINDOW", Templates.on_closing)

    def __config_window(self) -> None:
        """
        Формирует параметры и стили главного окна приложения
        """
        self.title(ttl)
        self.geometry(gt)
        self.resizable(rsb_wh, rsb_ht)


    def __config_scroll_frame(self) -> None:
        """
        Формирует параметры и стили контейнера для добавления спсисков покупок
        """
        self.__scroll_all_lists = ScrollAllLists(self, master=self, width=wh_sf, height=ht_sf, fg_color=fgc_sf, corner_radius=cr_sf)
        self.__scroll_all_lists.place(relx=0.04, rely=0.05)


    def __config_menu_buttons(self) -> None:
        """
        Формирует параметры и стили контейнера кнопок
        """
        self.__meny_btn_all_lists = MenuButtonsAllLists(self,  master=self, width=wh_bf, height=ht_bf, fg_color=fgc_bf, corner_radius=cr_sf)
        self.__meny_btn_all_lists.place(relx=0, rely=0.6)


    def __config_logo(self) -> None:
        """
        Формирует параметры и стили главного логотипа приложения
        """
        self.__logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size_l)
        self.__image_label = ctk.CTkLabel(self, image=self.__logo, text=tt_l)
        self.__image_label.place(relx=0.69, rely=0.05)


    def add_list_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке добавления список покупок
        """
        self.__create_shopping_list_page = CreateList(self)

        self.__scroll_all_lists.reset_checkboxes()

        self.withdraw()


    def open_list_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке открытия списка покупок
        """
        assert self.__scroll_all_lists.count_checkboxes != 0, showerror('Ошибка', 'Файл пуст. Открывать нечего')

        if not self.__scroll_all_lists.check_selected_checkbox():
            showerror('Ошибка', 'Выберите список чтобы открыть его')
            return

        if len(self.__scroll_all_lists.create_list_select_checkboxes()) != 1:
            showerror('Ошибка', 'Одновременно открыть можно только 1 список')
            return

        self.__open_list_page = OpenList(self, self.__scroll_all_lists)

        self.__scroll_all_lists.reset_checkboxes()

        self.withdraw()


    def edit_list_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке редактирования списка покупок
        """
        assert self.__scroll_all_lists.count_checkboxes != 0, showerror('Ошибка', 'Файл пуст. Редактировать нечего нечего')

        if not self.__scroll_all_lists.check_selected_checkbox():
            showerror('Ошибка', 'Выберите список для редактирования')
            return

        if len(self.__scroll_all_lists.create_list_select_checkboxes()) != 1:
            showerror('Ошибка', 'Одновременно редактировать можно только 1 список')
            return

        self.__edit_name_shopping_list_page = EditNameShoppingList(self, self.__scroll_all_lists)

        self.__edit_name_shopping_list_page.grab_set()


    def del_target_condition(self):
        """
        Внутри себя вызывает другую функцию, при помощи которой, получает список текстов активных чекбоксов
        Т.к. каждый элемент списка текстов активных чекбоксов является ключем словаря __load_data
        Поэтому в цикле удаляет каждый ключ, который содержится в списке текстов активных чекбоксов и затем перезаписывает данные
        """
        for key in self.__scroll_all_lists.create_list_text_select_checkbox():

            remove_elem = self.__load_data.get(key)

            if remove_elem is not None:
                self.__load_data_purchase_history[key] = remove_elem
                self.__load_data.pop(key, None)

        sld.write_data_in_shopping_lists(self.__load_data)
        sld.write_data_in_purchase_history(self.__load_data_purchase_history)


    def del_list_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке удаления списка покупок
        """
        assert self.__scroll_all_lists.count_checkboxes != 0, showerror('Ошибка', 'Файл пуст. Удалять нечего')

        if not self.__scroll_all_lists.check_selected_checkbox():
            showerror('Ошибка', 'Выберите список для удаления')
            return

        self.__confirmation_request_page = ConfirmationPage(self, self.__scroll_all_lists)

        self.__confirmation_request_page.grab_set()


    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на главную страницу
        """
        self.__main_window.deiconify()

        self.destroy()


    def __get_scroll_frame(self) -> ScrollAllLists:
        """
        Возвращает экземпляр ScrollAllLists, который используется для отображения списков покупок
        """
        return self.__scroll_all_lists


    def __get_create_shopping_list_page(self) -> CreateList:
        """
        Возвращает экземпляр CreateList, который используется для создания нового списка покупок
        """
        return self.__create_shopping_list_page


    def __get_load_data(self) -> dict:
        """
        Возвращает словарь с данными из файла shopping_lists.json
        """
        return self.__load_data


    def __get_load_data_purchase_history(self) -> dict:
        """
        Возвращает данные из файла purchase_history.json
        """
        return self.__load_data_purchase_history



    load_data = property(__get_load_data)

    load_data_purchase_history = property(__get_load_data_purchase_history)

    scroll_all_lists = property(__get_scroll_frame)

    create_shopping_list_page = property(__get_create_shopping_list_page)



