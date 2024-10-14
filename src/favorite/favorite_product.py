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

    def __init__(self, main_window: FavoriteProducts, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window
        self.__list_checkboxes = []

        self.__load_checkbox_products()


    def __load_checkbox_products(self) -> None:
        """
        Загружает в скролл фрейм все продукты этого списка в виде чекбоксов
        """
        for elem in self.__main_window.load_data_favorites["f"]:
            self.__main_window.list_products.append(elem)

            product = ctk.CTkCheckBox(self, text=f'{elem}', font=ft_sl, hover_color=hc_sl,
                                      fg_color=fgc_sl, border_width=bw_sl)
            product.grid(sticky="w", padx=(10, 0), pady=10)

            self.__list_checkboxes.append(product)


    def create_checkbox(self, name_product: str, count_product: int, category: str) -> None:
        """
        Создает чекбокс в скролл фрейме с переданными данными в качестве текста
        :param name_product: Принимает название продукта
        :param count_product: Принимает количество продукта
        :param category: Принимает категорию продукта
        :return: None
        """
        product = ctk.CTkCheckBox(self, text=f'{name_product}, {count_product}, {category}', font=ft_sl,
                                  hover_color=hc_sl, fg_color=fgc_sl, border_width=bw_sl)
        product.grid(sticky="w", padx=(10, 0), pady=10)

        self.__list_checkboxes.append(product)


    def check_selected_checkbox(self) -> bool:
        """
        Обходит список чекбоксов, определяет активный чекбокс если такой имеется вернет True,
        Если в списке нет активных чекбоксов то возвращает False
        """
        for checkbox in self.__list_checkboxes:
            if checkbox.get() == 1:
                return True
        return False


    def create_list_select_checkboxes(self) -> list[ctk.CTkCheckBox]:
        """
        Обходит список чекбоксов скролл фрейма и формирует новый список только из активных чекбоксов
        :return: Возвращает список активных чекбоксов
        """
        list_select_checkboxes = [checkbox for checkbox in self.__list_checkboxes if checkbox.get() == 1]

        return list_select_checkboxes


    def create_list_text_select_checkbox(self) -> list[str]:
        """
        Обходит список чекбоксов скролл фрейма и формирует новый список из текста только активных чекбоксов
        :return: Возвращает список текста активных чекбоксов
        """
        list_select_texts = [checkbox.cget("text") for checkbox in self.__list_checkboxes if checkbox.get() == 1]

        return list_select_texts


    def delete_checkbox(self) -> None:
        """
        Путем вызова другого метода получает список активных чекбоксов
        Удаляет все полученные элементы списка ативных чекбоксов из скролл фрейма и из списка чекбоксов
        """
        for checkbox in self.create_list_select_checkboxes():
            checkbox.destroy()
            self.__list_checkboxes.remove(checkbox)


    def clear_scroll_frame(self) -> None:
        """
        Удаляет все чекбоксы из скролл фрейма.
        """
        for checkbox in self.__list_checkboxes:
            checkbox.destroy()
        self.__list_checkboxes.clear()


    def reset_checkboxes(self) -> None:
        """
        Снимает галочки со всех чекбоксов.
        """
        for checkbox in self.__list_checkboxes:
            checkbox.deselect()

    def __get_list_checkboxes(self) -> list[ctk.CTkCheckBox]:
        return self.__list_checkboxes

    def __get_count_checkboxes(self):
        """
        :return: Возвращает количество чекбоксов в списке
        """
        return len(self.__list_checkboxes)

    list_checkboxes = property(__get_list_checkboxes)
    count_checkboxes = property(__get_count_checkboxes)


class MenuButtonsFavoriteProducts(ctk.CTkFrame):
    """
    Класс- контейнер, формирует область с кнопками, отвечающими за функционал страницы
    """

    def __init__(self, main_window: FavoriteProducts, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window

        self.__add_product_label = None

        self.__config_label_add_product()
        self.__config_menu_buttons()

    def __config_label_add_product(self) -> None:
        """
        Формирует в себе текст, описывающий функционал кнопки добавления нового товара
        """
        self.__label_add_list = ctk.CTkLabel(self, text_color=tc_all, text=tt_all, font=ft_all)
        self.__label_add_list.place(relx=0.1, rely=0.14)

    def __config_menu_buttons(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же устанавливает их параметры и стили
        """
        self.__add_product_image = ctk.CTkImage(light_image=Image.open(path_round_button), size=size_ali)
        self.__add_product = ctk.CTkButton(self, image=self.__add_product_image, width=wh_alb, height=ht_alb,
                                           text=tt_alb, fg_color=fgc_alb, hover_color=hc_alb)
        self.__add_product.configure(command=self.__main_window.add_button_click_handler)
        self.__add_product.place(relx=0.04, rely=0.1)

        self.__del_product = ctk.CTkButton(self, text=tt_db, width=wh_db, fg_color=fgc_db, height=ht_db,
                                           text_color=tc_db,
                                           border_width=bw_db, hover_color=hc_db, font=ft_db)
        self.__del_product.configure(command=self.__main_window.del_button_click_handler)
        self.__del_product.place(relx=0.05, rely=0.65)

        self.__clear_btn = ctk.CTkButton(self, text=tt_cbt, width=wh_cb, fg_color=fgc_cb, height=ht_cb,
                                         text_color=tc_cb,
                                         border_width=bw_cb, hover_color=hc_cb, font=ft_cb)
        self.__clear_btn.configure(command=self.__main_window.clear_button_click_handler)
        self.__clear_btn.place(relx=0.375, rely=0.65)

        self.__cancel_btn = ctk.CTkButton(self, text=tt_cab, width=wh_cab, fg_color=fgc_cab, height=ht_cab,
                                          text_color=tc_cab, border_width=bw_cab, hover_color=hc_cab, font=ft_cab)
        self.__cancel_btn.configure(command=self.__main_window.cancel_button_click_handler)
        self.__cancel_btn.place(relx=0.705, rely=0.65)


class FavoriteProducts(ctk.CTkToplevel):
    """
    Мэйн класс страницы, в себе формирует основные контейнеры (фреймы), содержащие остальные виджеты страницы, а так же основную логику страницы
    """

    def __init__(self, main_window):
        super().__init__()
        self.__main_window = main_window
        self.__load_data_favorites = sld.read_data_with_favorites_products() if sld.check_file_favorites_products() else {"f": []}

        self.__scroll_favorite = None
        self.__menu_btn_favorite = None

        self.__list_products = []

        self.__add_product_page = None
        self.__confirmation_request_page = None
        self.__confirmation_clear_favorite_page = None

        self.__config_window()
        self.__config_logo()
        self.__config_scroll_frame()
        self.__config_menu_buttons()

    def __config_window(self) -> None:
        """
        Формирует параметры и стили главного окна приложения
        """
        self.title(ttl)
        self.geometry(gt)

    def __config_logo(self) -> None:
        """
        Формирует параметры и стили главного логотипа приложения
        """
        self.__logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size_l)
        self.__image_label = ctk.CTkLabel(self, image=self.__logo, text=tt_l)
        self.__image_label.place(relx=0.69, rely=0.05)

    def __config_scroll_frame(self) -> None:
        """
        Формирует параметры и стили контейнера для добавления покупок
        """
        self.__scroll_favorite = ScrollFavoriteProducts(self, master=self, width=wh_sp, height=ht_sp, fg_color=fgc_sp,
                                                        corner_radius=cr_sp)
        self.__scroll_favorite.place(relx=0.04, rely=0.05)

    def __config_menu_buttons(self) -> None:
        """
        Формирует параметры и стили контейнера кнопок
        """
        self.__menu_btn_favorite = MenuButtonsFavoriteProducts(self, master=self, width=wh_bm, height=ht_bm,
                                                               fg_color=fgc_bm, corner_radius=cr_bm)
        self.__menu_btn_favorite.place(relx=0, rely=0.6)

    def add_button_click_handler(self):
        """
        Обрабатывает клик по кнопке добавления товара
        """
        self.__add_product_page = AddProduct(self, self.__scroll_favorite)

        self.__add_product_page.grab_set()

    def del_target_condition(self) -> None:
        """
        Внутри себя вызывает другую функцию, при помощи которой, получает список текстов активных чекбоксов
        Т.к. каждый элемент списка текстов активных чекбоксов является ключем словаря __load_data
        Поэтому в цикле удаляет каждый ключ, который содержится в списке текстов активных чекбоксов и затем перезаписывает данные
        """
        for product_to_remove in self.__scroll_favorite.create_list_text_select_checkbox():
            self.__list_products = [product for product in self.__list_products if product != product_to_remove]

        self.__load_data_favorites["f"] = self.__list_products

        sld.write_data_in_favorites_products(self.__load_data_favorites)

    def del_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке удаления выделенного товара
        """
        assert self.__scroll_favorite.count_checkboxes != 0, showerror('Ошибка', 'Список пуст. Удалять нечего')

        if not self.__scroll_favorite.check_selected_checkbox():
            showerror('Ошибка', 'Выберите товар для удаления')
            return

        self.__confirmation_request_page = ConfirmationPage(self, self.__scroll_favorite)

        self.__confirmation_request_page.grab_set()

    def clear_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке удаления всего товара в избранном
        """
        assert self.__scroll_favorite.count_checkboxes != 0, showerror('Ошибка', 'Список пуст. Удалять нечего')

        self.__confirmation_clear_favorite_page = ConfirmationClearScrollPlace(self, self.__scroll_favorite)

        self.__confirmation_clear_favorite_page.grab_set()

    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата в предыдущее меню
        """
        self.__main_window.deiconify()

        self.destroy()

    def __get_scroll_favorite(self) -> ScrollFavoriteProducts:
        """
        Возвращает объект класса ScrollFavoriteProducts
        """
        return self.__scroll_favorite

    def __get_load_data_favorites(self) -> dict:
        """
        Возвращает словарь с данными из файла favorites_products.json
        """
        return self.__load_data_favorites

    def __get_list_products(self) -> list[str]:
        """
        Возвращает список продуктов из избранного
        """
        return self.__list_products

    list_products = property(__get_list_products)
    load_data_favorites = property(__get_load_data_favorites)
    scroll_favorite = property(__get_scroll_favorite)
