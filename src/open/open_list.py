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


    def __load_checkbox_products(self) -> None:
        """
        Внутри себя вызывает другую функцию, при помощи которой, получает текст нажатого чекбокса и ссылку на него
        Сравнивает полученные данные через цикл с загруженными данными из файла, таким образом находит, отмеченный чекбоксом, список
        И загружает в скролл фрейм все продукты этого списка в виде чекбоксов
        """
        text, checkbox = self.__main_window.scroll_all_lists.get_selected_checkbox()

        self.__list_name = text

        self.__list_checkboxes.clear()

        for elem in self.__main_window.load_data[text]:
            self.__main_window.list_products.append(elem)

        for elem in self.__main_window.list_products:
            product = ctk.CTkCheckBox(self, text=f'{', '.join(elem)}', font=ft_sl, hover_color=hc_sl,
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


    def return_all_checkboxes(self) -> None:
        """
        Возвращает все скрытые чекбоксы в скролл фрейм
        """
        for elem in self.__main_window.list_products:
            product = ctk.CTkCheckBox(self, text=f'{", ".join(elem)}', font=ft_sl,
                                      hover_color=hc_sl, fg_color=fgc_sl, border_width=bw_sl)
            product.grid(sticky="w", padx=(10, 0), pady=10)

            self.__list_checkboxes.append(product)


    def load_checkboxes_for_selected_category(self, sorted_products: list[list]) -> None:
        """
        Загружает во фпейм только те чекбоксы, у которых есть выбранная категория
        """
        for elem in sorted_products:
            product = ctk.CTkCheckBox(self, text=f'{', '.join(elem)}', font=ft_sl,
                                      hover_color=hc_sl, fg_color=fgc_sl, border_width=bw_sl)
            product.grid(sticky="w", padx=(10, 0), pady=10)

            self.__list_checkboxes.append(product)


    def update_checkbox_place(self, selected_category: str) -> None:
        """
        Сортирует чекбоксы по выбранной категории, если товар с выбранной категорией есть в скролле то уберутся все чекбоксы кроме тех
        У которых есть выбранная категория, если же выбранной категории нет в списке, то отобразятся все товары списка, со всеми категориями
        """
        self.clear_scroll_frame()

        sorted_products = [elem for elem in self.__main_window.list_products if selected_category in elem]

        if not sorted_products:
            showerror('Ошибка', 'Товары с выбранной категорией отсутствуют')

            self.return_all_checkboxes()

        self.load_checkboxes_for_selected_category(sorted_products)


    def set_new_text_for_checkbox(self, checkbox, new_text) -> None:
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


    def create_list_text_select_checkbox(self) -> list[str]:
        """
        Обходит список чекбоксов скролл фрейма и формирует новый список из текста только активных чекбоксов
        :return: Возвращает список текста активных чекбоксов
        """
        list_select_texts = [checkbox.cget("text") for checkbox in self.__list_checkboxes if checkbox.get() == 1]

        return list_select_texts


    def delete_checkbox(self) -> None:
        """
        Внутри себя вызывает другую функцию, при помощи которой, получает список активных чекбоксов
        Обходит этот список и удаляет его из этого списка, а так же из скролл фрейма и из списка чекбоксов
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


    def check_selected_checkbox(self) -> bool:
        """
        Обходит список чекбоксов, определяет активный чекбокс если такой имеется вернет return,
        Если в списке нет активных чекбоксов то возвращает False
        """
        for checkbox in self.__list_checkboxes:
            if checkbox.get() == 1:
                return True
        return False


    def get_selected_checkbox(self) -> (str, ctk.CTkCheckBox) or (None, None):
        """
        Обходит список чекбоксов, определяет активный чекбокс если такой имеется и возвращает кортеж из его текста и ссылки на него,
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
            checkbox.deselect()


    def __get_count_checkboxes(self) -> int:
        """
        :return: Возвращает количество чекбоксов в списке
        """
        return len(self.__list_checkboxes)


    def __get_list_name(self) -> str:
        """
        :return: Возвращает имя списка
        """
        return self.__list_name


    def __get_list_checkboxes(self) -> list[ctk.CTkCheckBox]:
        """
        :return: Возвращает список чекбоксов во фрейме
        """
        return self.__list_checkboxes


    list_checkboxes = property(__get_list_checkboxes)
    list_name = property(__get_list_name)
    count_checkboxes = property(__get_count_checkboxes)



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


    def __config_label_add_product_in_list(self) -> None:
        """
        Формирует в себе текст, описывающий функционал кнопки добавления нового товара
        """
        self.__add_product_label_in_list = ctk.CTkLabel(self, text_color=tc_apl, text=tt_apl, font=ft_apl)
        self.__add_product_label_in_list.place(relx=0.1, rely=0.14)


    def __config_label_add_product_in_favorite(self) -> None:
        """
        Формирует в себе текст, описывающий функционал кнопки добавления нового товара
        """
        self.__add_product_label_in_favorite = ctk.CTkLabel(self, text_color=tc_f, text=tt_f, font=ft_f)
        self.__add_product_label_in_favorite.place(relx=0.44, rely=0.14)


    def __config_menu_buttons(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же устанавливает его параметры и стили
        """
        self.__add_product_image = ctk.CTkImage(light_image=Image.open(path_round_button), size=size_api)
        self.__add_product = ctk.CTkButton(self, image=self.__add_product_image, width=wh_ap, height=ht_ap, text=tt_ap,
                                           fg_color=fgc_ap, hover_color=hc_ap)
        self.__add_product.configure(command=self.__main_window.add_button_click_handler)
        self.__add_product.place(relx=0.04, rely=0.1)

        self.__image_favorite = ctk.CTkImage(light_image=Image.open(path_favorite_button), size=size_if)

        self.__favorite = ctk.CTkButton(self, image=self.__image_favorite, width=wh_bf, height=ht_bf, text=tt_bf,
                                        fg_color=fgc_bf, hover_color=hc_bf)
        self.__favorite.configure(command=self.__main_window.favorite_button_click_handler)
        self.__favorite.place(relx=0.38, rely=0.1)

        self.__edit_product = ctk.CTkButton(self, text=tt_ep, width=wh_ep, fg_color=fgc_ep, height=ht_ep,
                                            text_color=tc_ep, border_width=bw_ep, hover_color=hc_ep, font=ft_ep)
        self.__edit_product.configure(command=self.__main_window.edit_button_click_handler)
        self.__edit_product.place(relx=0.05, rely=0.65)

        self.__del_product = ctk.CTkButton(self, text=tt_dp, width=wh_dp, fg_color=fgc_dp, height=ht_dp,
                                           text_color=tc_dp, border_width=bw_dp, hover_color=hc_dp, font=ft_dp)
        self.__del_product.configure(command=self.__main_window.del_button_click_handler)
        self.__del_product.place(relx=0.375, rely=0.65)

        self.__cancel_btn = ctk.CTkButton(self, text=tt_cb, width=wh_cb, fg_color=fgc_cb, height=ht_cb,
                                          text_color=tc_cb, border_width=bw_cb, hover_color=hc_cb, font=ft_cb)
        self.__cancel_btn.configure(command=self.__main_window.cancel_button_click_handler)
        self.__cancel_btn.place(relx=0.705, rely=0.65)



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
        self.__logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size_l)
        self.__image_label = ctk.CTkLabel(self, image=self.__logo, text=tt_l)
        self.__image_label.place(relx=0.69, rely=0.05)


    def __config_scroll_frame(self) -> None:
        """
        Формирует параметры и стили контейнера для добавления товаров
        """
        self.__scroll_open_list = ScrollOpenListProducts(self, master=self, width=wh_sf, height=ht_sf, fg_color=fgc_sf,
                                                         corner_radius=cr_sf)
        self.__scroll_open_list.place(relx=0.04, rely=0.05)


    def __config_menu_buttons(self) -> None:
        """
        Формирует параметры и стили контейнера кнопок
        """
        self.__menu_btn_open_list = MenuButtonsOpenList(self, master=self, width=wh_mb, height=ht_mb, fg_color=fgc_mb,
                                                        corner_radius=cr_mb)
        self.__menu_btn_open_list.place(relx=0, rely=0.6)


    def __config_menu_sorted(self) -> None:
        """
        Формирует параметры и стили алгоритма сортировки товаров и ее визуал
        """
        self.__sort_label = ctk.CTkLabel(self, text_color=tc_slb, text=tt_slb, font=ft_slb)
        self.__sort_label.place(relx=0.69, rely=0.4)

        self.__category_product = ctk.CTkComboBox(self, text_color=tc_c, width=wh_c, height=ht_c, fg_color=fgc_c,
                                                  font=ft_c,
                                                  state=st_c, button_color=bc_c, )
        self.__category_product.configure(values=self.__list_categories.get("cs"))
        self.__category_product.place(relx=0.69, rely=0.47)
        self.__category_product.bind("<<ComboboxSelected>>", self.sort_button_click_handler)

        self.__sort_products_image = ctk.CTkImage(light_image=Image.open(path_glass_button), size=size_sp)
        self.__sort_products = ctk.CTkButton(self, image=self.__sort_products_image, text=tt_sp, width=wh_sp,
                                             fg_color=fgc_sp, height=ht_sp, hover_color=hc_sp)
        self.__sort_products.configure(command=self.sort_button_click_handler)
        self.__sort_products.place(relx=0.91, rely=0.46)


    def add_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке сохранения списка покупок
        """
        self.__add_product_page = AddProduct(self, self.__scroll_open_list)

        self.__add_product_page.grab_set()


    def update_load_data(self, old_text: str, new_text: str) -> None:
        """
        Обходит матрицу продуктов, сравнивает полученный текст из чекбокса, если они совпадают то меняет по индесу старый продукт на новый
        :param old_text: Старый текст чекбокса, до редактирования
        :param new_text: Новый текст чекбокса, после редактирования
        """
        old_items = old_text.split(', ')
        new_items = new_text.split(', ')

        for index, elem in enumerate(self.__list_products):
            if elem == old_items:
                self.__list_products[index] = new_items

        self.__load_data[self.__scroll_open_list.list_name] = self.__list_products

        sld.write_data_in_shopping_lists(self.__load_data)


    def edit_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке редактирования товара
        """
        assert self.__scroll_open_list.count_checkboxes != 0, showerror('Ошибка', 'Файл пуст. Редактировать нечего')

        if not self.__scroll_open_list.check_selected_checkbox():
            showerror('Ошибка', 'Выберите товар для редактирования')
            return

        if len(self.__scroll_open_list.create_list_select_checkboxes()) != 1:
            showerror('Ошибка', 'Одновременно редактировать можно только 1 товар')
            return

        self.__edit_product_page = EditProduct(self, self.__scroll_open_list)

        self.__edit_product_page.grab_set()


    def sort_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке редактирования товара
        """
        assert self.__scroll_open_list.count_checkboxes != 0, showerror('Ошибка', 'Список пуст. Сортировать нечего')

        selected_category = self.__category_product.get()

        if not selected_category:
            showerror('Ошибка', 'Выберите категорию для сортировки')
            return

        self.__scroll_open_list.update_checkbox_place(selected_category)


    def del_target_condition(self) -> None:
        """
        Внутри себя вызывает другую функцию, при помощи которой, получает список текстов активных чекбоксов
        Т.к. каждый элемент списка текстов активных чекбоксов является ключем словаря __load_data
        Поэтому в цикле мы удаляем каждый ключ, который содержится в списке текстов активных чекбоксов и затем перезаписываем данные
        """
        for text in self.__scroll_open_list.create_list_text_select_checkbox():
            product_to_remove = text.split(', ')

            self.__list_products = [product for product in self.__list_products if product != product_to_remove]

        self.__load_data[self.__scroll_open_list.list_name] = self.__list_products

        sld.write_data_in_shopping_lists(self.__load_data)

    def del_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке удаления товара
        """
        assert self.__scroll_open_list.count_checkboxes != 0, showerror('Ошибка', 'Список пуст. Удалять нечего')

        if not self.__scroll_open_list.check_selected_checkbox():
            showerror('Ошибка', 'Выберите товар для удаления')
            return

        self.__confirmation_request_page = ConfirmationPage(self, self.__scroll_open_list)

        self.__confirmation_request_page.grab_set()


    def favorite_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке добавления товара в список избранного
        """
        assert self.__scroll_open_list.count_checkboxes != 0, showerror('Ошибка', 'Список пуст. Добавлять нечего')

        if not self.__scroll_open_list.check_selected_checkbox():
            showerror('Ошибка', 'Выберите товар для добавления')
            return

        list_select_texts = self.__scroll_open_list.create_list_text_select_checkbox()

        for elem in list_select_texts:

            if elem not in self.__load_data_favorites.get("f"):
                self.__load_data_favorites.get("f").append(elem)

        showinfo('Сообщение', 'Товар успешно добавлен в "Избранное"')

        sld.write_data_in_favorites_products(self.__load_data_favorites)

        self.__scroll_open_list.reset_checkboxes()


    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        self.__main_window.deiconify()

        self.destroy()


    def __get_scroll_all_lists(self) -> ScrollAllLists:
        """
        Возвращает объект класса ScrollAllLists
        """
        return self.__scroll_all_lists


    def __get_list_products(self) -> list[list[str]]:
        """
        Возвращает текущий список продуктов
        """
        return self.__list_products


    def __get_load_data(self) -> dict:
        """
        Возвращает текущий словарь с данными о списках покупок
        """
        return self.__load_data


    def __get_category_product(self) -> ctk.CTkComboBox:
        """
        Возвращает объект класса CtkComboBox, который отвечает за категории продуктов
        """
        return self.__category_product


    category_product = property(__get_category_product)
    load_data = property(__get_load_data)
    list_products = property(__get_list_products)
    scroll_all_lists = property(__get_scroll_all_lists)
