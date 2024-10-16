from __future__ import annotations

import customtkinter as ctk
from PIL import Image
from tkinter.messagebox import showerror, showinfo

from src.history.config_purchase_history import *
from src.templates.templates import Templates
from src.top.top_lvl_pages import ConfirmationClearScrollPlace, ConfirmationPage, ViewListPurchaseHistory
from src.load.save_and_load_data import SaveAndLoadData as sld


class ScrollPurchaseHistory(ctk.CTkScrollableFrame):
    """
    Класс- контейнер, формирует область со скролом для работы с добавленными товарами
    """
    def __init__(self, main_window: PurchaseHistory, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window

        self.__list_checkboxes = []

        self.__load_checkbox_products()


    def __load_checkbox_products(self) -> None:
        """
        Внутри себя вызывает другую функцию, при помощи которой, получает текст нажатого чекбокса и ссылку на него
        Сравнивает полученные данные через цикл с загруженными данными из файла, таким образом находит, отмеченный чекбоксом, список
        И загружает в скролл фрейм все продукты этого списка в виде чекбоксов
        """

        for list_name in self.__main_window.load_data_purchase_history.keys():

            shopping_list = ctk.CTkCheckBox(self, text=f'{list_name}', font=ft_sl, hover_color=hc_sl, fg_color=fgc_sl, border_width=bw_sl)
            shopping_list.grid(sticky="w", padx=(10, 0), pady=10)

            self.__list_checkboxes.append(shopping_list)


    def create_list_select_checkboxes(self) -> list [ctk.CTkCheckBox] :
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


    def check_selected_checkbox(self) -> bool:
        """
        Обходит список чекбоксов, определяет активный чекбокс если такой имеется вернет True,
        Если в списке нет активных чекбоксов то возвращает False
        """
        for checkbox in self.__list_checkboxes:
            if checkbox.get() == 1:
                return True
        return False


    def get_selected_checkbox(self) -> (str, ctk.CTkCheckBox) or bool:
        """
        Обходит список чекбоксов, определяет активный чекбокс если такой имеется и возвращает кортеж из его текста и самого чекбокса,
        Если в списке нет активных чекбоксов то возвращает кортеж (None, None)
        :return:
        """
        for checkbox in self.__list_checkboxes:
            if checkbox.get() == 1:
                return checkbox.cget("text"), checkbox
        return None, None


    def delete_checkbox(self) -> None:
        """
        Внутри себя вызывает другую функцию, при помощи которой, получает список активных чекбоксов
        Обходит этот список и удаляет его элементы из скролл фрейма и из списка чекбоксов
        """
        for checkbox in self.create_list_select_checkboxes():
            checkbox.destroy()
            self.__list_checkboxes.remove(checkbox)


    def reset_checkboxes(self) -> None:
        """
        Снимает галочки со всех чекбоксов.
        """
        for checkbox in self.__list_checkboxes:
            if self.check_selected_checkbox():
                checkbox.deselect()


    def clear_scroll_frame(self) -> None:
        """
        Удаляет все чекбоксы из скролл фрейма.
        """
        for checkbox in self.__list_checkboxes:
            checkbox.destroy()
        self.__list_checkboxes.clear()


    def __get_count_checkboxes(self) -> int:
        """
        :return: Возвращает количество чекбоксов в списке
        """
        return len(self.__list_checkboxes)


    def __get_list_checkboxes(self) -> list [ctk.CTkCheckBox]:
        """
        Возвращает список чекбоксов
        """
        return self.__list_checkboxes

    list_checkboxes = property(__get_list_checkboxes)
    count_checkboxes = property(__get_count_checkboxes)



class ButtonsMenuPurchaseHistory(ctk.CTkFrame):
    """
    Класс- контейнер, формирует область с кнопками, отвечающими за функционал страницы
    """
    def __init__(self, main_window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window

        self.__label_open_list = None

        self.__config_menu_buttons()
        self.__config_label_open_list()
        self.__config_label_restore_list()


    def __config_label_open_list(self) -> None:
        """
        Формирует в себе текст, описывающий функционал кнопки добавления нового товара
        """
        self.__label_open_list = ctk.CTkLabel(self, text_color=tc_all, text=tt_all, font=ft_all)
        self.__label_open_list.place(relx=0.1, rely=0.14)


    def __config_label_restore_list(self) -> None:
        """
        Формирует в себе текст, описывающий функционал кнопки добавления нового товара
        """
        self.__label_open_list = ctk.CTkLabel(self, text_color=tc_rl, text=tt_rl, font=ft_rl)
        self.__label_open_list.place(relx=0.44, rely=0.14)


    def __config_menu_buttons(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же устанавливает их параметры и стили
        """
        self.__open_list_image_button = ctk.CTkImage(light_image=Image.open(path_round_button), size=size_ol)
        self.__open_list = ctk.CTkButton(self, image=self.__open_list_image_button, width=wh_ol, height=ht_ol,
                                            text=tt_ol, fg_color=fgc_ol, hover_color=hc_ol)
        self.__open_list.configure(command=self.__main_window.view_button_click_handler)
        self.__open_list.place(relx=0.04, rely=0.1)

        self.__restore_list_image_button = ctk.CTkImage(light_image=Image.open(path_reset_button), size=size_ol)
        self.__restore = ctk.CTkButton(self, image=self.__restore_list_image_button, width=wh_ol, height=ht_ol,
                                            text=tt_ol, fg_color=fgc_ol, hover_color=hc_ol)
        self.__restore.configure(command=self.__main_window.restore_button_click_handler)
        self.__restore.place(relx=0.38, rely=0.1)

        self.__del_product = ctk.CTkButton(self, text=tt_dp, width=wh_dp, fg_color=fgc_dp, height=ht_dp,
                                           text_color=tc_dp, border_width=bw_dp, hover_color=hc_dp, font=ft_dp)
        self.__del_product.configure(command=self.__main_window.del_button_click_handler)
        self.__del_product.place(relx=0.05, rely=0.65)

        self.__clear_history = ctk.CTkButton(self, text=tt_ch, width=wh_ch, fg_color=fgc_ch, height=ht_ch,
                                             text_color=tc_ch, border_width=bw_ch, hover_color=hc_ch, font=ft_ch)
        self.__clear_history.configure(command=self.__main_window.clear_button_click_handler)
        self.__clear_history.place(relx=0.375, rely=0.65)

        self.__cancel_btn = ctk.CTkButton(self, text=tt_cb, width=wh_cb, fg_color=fgc_cb,
                                        height=ht_cb, text_color=tc_cb, border_width=bw_cb, hover_color=hc_cb,
                                        font=ft_cb)
        self.__cancel_btn.configure(command=self.__main_window.cancel_button_click_handler)
        self.__cancel_btn.place(relx=0.705, rely=0.65)



class PurchaseHistory(ctk.CTkToplevel):
    """
    Мэйн класс страницы, в себе формирует основные контейнеры (фреймы), содержащие остальные виджеты страницы, а так же основную логику страницы
    """
    def __init__(self, main_window):
        super().__init__()
        self.__main_window = main_window

        self.__load_data_purchase_history = sld.read_data_with_purchase_history() if sld.check_file_purchase_history() else {}
        self.__load_data = sld.read_data_with_shopping_lists() if sld.check_file_shopping_lists() else {}

        self.__scroll_purchase_history = None
        self.__menu_btn_purchase_history = None

        self.__view_list_page = None
        self.__confirmation_request_page = None
        self.__confirmation_clear_page = None

        self.__config_window()
        self.__config_logo()
        self.__config_scroll_frame()
        self.__config_menu_buttons()

        self.protocol("WM_DELETE_WINDOW", Templates.on_closing)


    def __config_window(self) -> None:
        """
        Формирует параметры и стили главного окна приложения
        """
        self.title(ttl_cw)
        self.geometry(gt_cw)
        self.resizable(rzb_wh, rzb_ht)


    def __config_logo(self) -> None:
        """
        Формирует параметры и стили главного логотипа приложения
        """
        self.logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size_l)
        self.image_label = ctk.CTkLabel(self, image=self.logo, text=tt_l)
        self.image_label.place(relx=0.69, rely=0.05)


    def __config_scroll_frame(self) -> None:
        """
        Формирует параметры и стили контейнера для добавления товаров
        """
        self.__scroll_purchase_history = ScrollPurchaseHistory(self,  master=self, width=wh_sf, height=ht_sf, fg_color=fgc_sf, corner_radius=cr_sf)
        self.__scroll_purchase_history.place(relx=0.04, rely=0.05)


    def __config_menu_buttons(self) -> None:
        """
        Формирует параметры и стили контейнера кнопок
        """
        self.__menu_btn_purchase_history = ButtonsMenuPurchaseHistory(self, master=self, width=wh_mb, height=ht_mb, fg_color=fgc_mb, corner_radius=cr_mb)
        self.__menu_btn_purchase_history.place(relx=0, rely=0.6)


    def view_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке открытия и просмотра списка покупок
        """
        assert self.__scroll_purchase_history.count_checkboxes != 0, showerror('Ошибка', 'Файл пуст. Открывать нечего')

        if not self.__scroll_purchase_history.check_selected_checkbox():
            showerror('Ошибка', 'Выберите список чтобы открыть')
            return

        if len(self.__scroll_purchase_history.create_list_select_checkboxes()) != 1:
            showerror('Ошибка', 'Одновременно открыть можно только 1 список')
            return

        self.__view_list_page = ViewListPurchaseHistory(self, self.__scroll_purchase_history)

        self.__view_list_page.grab_set()

        self.__scroll_purchase_history.reset_checkboxes()


    def del_target_condition(self) -> None:
        """
        Внутри себя вызывает другую функцию, при помощи которой, получает список текстов активных чекбоксов
        Т.к. каждый элемент списка текстов активных чекбоксов является ключем словаря __load_data
        Поэтому в цикле удаляет каждый ключ, который содержится в списке текстов активных чекбоксов и затем перезаписывает данные
        """

        for key in self.__scroll_purchase_history.create_list_text_select_checkbox():

            self.__load_data_purchase_history.pop(key, None)

        sld.write_data_in_purchase_history(self.__load_data_purchase_history)


    def del_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке удаления товара
        """
        assert self.__scroll_purchase_history.count_checkboxes != 0, showerror('Ошибка', 'Список пуст. Удалять нечего')

        if not self.__scroll_purchase_history.check_selected_checkbox():
            showerror('Ошибка', 'Выберите товар для удаления')
            return

        self.__confirmation_request_page = ConfirmationPage(self, self.__scroll_purchase_history)
        self.__confirmation_request_page.grab_set()


    def clear_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке редактирования товара
        """
        assert self.__scroll_purchase_history.count_checkboxes != 0, showerror('Ошибка', 'Список пуст. Удалять нечего')

        self.__confirmation_clear_page = ConfirmationClearScrollPlace(self, self.__scroll_purchase_history)

        self.__confirmation_clear_page.grab_set()


    def restore_button_click_handler(self) -> None:
        """
        Внутри себя вызывает другую функцию, при помощи которой, получает список текстов активных чекбоксов
        Затем удаляет все данные хранящиеся в этом списке из __load_data_purchase_history и добавляет их в __load_data
        """
        assert self.__scroll_purchase_history.count_checkboxes != 0, showerror('Ошибка', 'Список пуст. Восстанавливать нечего')

        if not self.__scroll_purchase_history.check_selected_checkbox():
            showerror('Ошибка', 'Выберите список для восстановления')
            return

        for key in self.__scroll_purchase_history.create_list_text_select_checkbox():

            remove_elem = self.__load_data_purchase_history.get(key)

            if remove_elem is not None:
                self.__load_data[key] = remove_elem
                self.__load_data_purchase_history.pop(key, None)

        showinfo('Сообщение', 'Данные успешно восстановлены')

        sld.write_data_in_purchase_history(self.__load_data_purchase_history)
        sld.write_data_in_shopping_lists(self.__load_data)

        self.__scroll_purchase_history.delete_checkbox()


    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        self.__main_window.deiconify()

        self.destroy()

    def __get_load_data_purchase_history(self) -> dict:
        """
        Возвращает данные из файла purchase_history.json
        """
        return self.__load_data_purchase_history

    def __get_load_data(self) -> dict:
        """
        Возвращает данные из файла purchase_history.json
        """
        return self.__load_data


    load_data = property(__get_load_data)
    load_data_purchase_history = property(__get_load_data_purchase_history)