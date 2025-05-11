from __future__ import annotations

from tkinter import END
from PIL import Image
import customtkinter as ctk
from tkinter.messagebox import showerror

from src.create.config_create_list import *
from src.load.save_and_load_data import SaveAndLoadData as sld
from src.top.top_lvl_pages import AddNewCategory, EditProduct, ConfirmationPage
from src.templates.templates import Templates


class ScrollCreateList(ctk.CTkScrollableFrame):
    """
    Класс- контейнер, формирует область со скроллом для добавления товаров
    """

    def __init__(self, main_window: CreateList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window
        self.__list_checkboxes = []


    def create_checkbox(self, name_product: str, count_product: int, category: str) -> None:
        """
        Создает чекбокс в скролл фрейме с переданными данными в качестве текста
        :param name_product: Принимает название продукта
        :param count_product: Принимает количество продукта
        :param category: Принимает категорию продукта
        :return: None
        """
        product = ctk.CTkCheckBox(self, text=f'{name_product}, {count_product}, {category}', font=ft_p,
                                         hover_color=hc_p, fg_color=fgc_p, border_width=bw_p)
        product.grid(sticky="w", padx=(10, 0), pady=10)

        self.__list_checkboxes.append(product)


    def set_new_text_for_checkbox(self, checkbox: ctk.CTkCheckBox,  new_text: str) -> None:
        """
        Устанавливает новый текст для чекбокса если он существует
        :param checkbox: Принимает ссылку на чекбокс
        :param new_text: Принимает новый текст для чекбокса
        :return: None
        """
        if checkbox is not None:
            checkbox.configure(text=new_text)


    def create_list_select_checkboxes(self) -> list [ctk.CTkCheckBox]:
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
        Путем вызова другого метода получает список активных чекбоксов
        Удаляет все полученные элементы списка ативных чекбоксов из скролл фрейма и из списка чекбоксов
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
        Обходит список чекбоксов, определяет активный чекбокс если такой имеется и возвращает кортеж из его текста и ссылки на него,
        :return: Если в списке нет активных чекбоксов то возвращает кортеж (None, None)
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


    def __get_list_checkboxes(self) -> list [ctk.CTkCheckBox]:
        """
        Возвращает список чекбоксов
        """
        return self.__list_checkboxes

    list_checkboxes = property(__get_list_checkboxes)
    count_checkboxes = property(__get_count_checkboxes)



class ConfigCreateList(ctk.CTkFrame):
    """
    Класс- контейнер для виджетов, которые формируют конфигурацию и составляющие списка покупок,
    Такие как название списка, название товара, категория и его количество, а так же логотип приложения
    """
    def __init__(self, main_window: CreateList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window

        self.__name_shopping_list = None
        self.__name_product = None
        self.__count_product = None
        self.__category_product = None

        self.__label_add_product = None

        self.__list_categories = sld.read_categories()

        self.__config_logo()
        self.__config_input_fields()
        self.__config_category_list()
        self.__config_buttons_add()
        self.__config_label_add_product()

    def __config_logo(self) -> None:
        """
        Формирует параметры и стили главного логотипа приложения
        """
        self.__logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size_l)
        self.__image_label = ctk.CTkLabel(self, image=self.__logo, text=tt_l)
        self.__image_label.place(relx=0.72, rely=0.14)


    def __config_input_fields(self) -> None:
        """
        Формирует в себе поля ввода данных пользователя
        """
        self.__name_shopping_list = ctk.CTkEntry(self, placeholder_text=tt_nsl, placeholder_text_color=ptc_nsl,
                                              width=wh_nsl, height=ht_nsl, fg_color=fgc_nsl, font=ft_nsl, text_color=ptc_nsl)
        self.__name_shopping_list.place(relx=0.036, rely=0.17)

        self.__name_product = ctk.CTkEntry(self, placeholder_text=pht_np, placeholder_text_color=phtc_np,
                                              width=wh_np, height=ht_np, fg_color=fgc_np, font=ft_np, text_color=ptc_nsl)
        self.__name_product.place(relx=0.035, rely=0.45)

        self.__count_product = ctk.CTkEntry(self, placeholder_text=pht_cp, placeholder_text_color=phtc_cp,
                                              width=wh_cp, height=ht_cp, fg_color=fgc_cp, font=ft_cp, text_color=ptc_nsl)
        self.__count_product.place(relx=0.33, rely=0.45)


    def __config_category_list(self) -> None:
        """
        Формирует в себе категории товара
        """
        self.__category_product = ctk.CTkComboBox(self,  text_color=tc_c,  width=wh_c, height=ht_c, fg_color=fgc_c, font=ft_c,
                                        state=st_c, button_color=bc_c, )
        self.__category_product.configure(values=self.__list_categories.get("cs"))
        self.__category_product.place(relx=0.457, rely=0.45)


    def __config_label_add_product(self) -> None:
        """
        Формирует в себе текст, описывающий функционал кнопки добавления нового товара
        """
        self.__label_add_product = ctk.CTkLabel(self, text=tt_apl, font=ft_apl)
        self.__label_add_product.place(relx=0.1, rely=0.75)


    def __config_buttons_add(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за добавление нового товара и добавление новой категории, а так же устанавливает их параметры и стили
        """
        self.__add_product_image = ctk.CTkImage(light_image=Image.open(path_round_button), size=size_api)
        self.__add_product = ctk.CTkButton(self, image=self.__add_product_image, width=wh_apb, height=ht_apb, text=tt_apb,
                                                fg_color=fgc_apb, hover_color=hc_apb)
        self.__add_product.configure(command=self.__main_window.add_product_button_click_handler)
        self.__add_product.place(relx=0.035, rely=0.7)

        self.__add_category_image = ctk.CTkImage(light_image=Image.open(path_round_button), size=size_aci)
        self.__add_category = ctk.CTkButton(self, image=self.__add_category_image, width=wh_acb, height=ht_acb, text=tt_acb,
                                                fg_color=fgc_acb, hover_color=hc_acb)
        self.__add_category.configure(command=self.__main_window.add_category_button_click_handler)
        self.__add_category.place(relx=0.64, rely=0.45)


    def __get_name_shopping_list(self) -> ctk.CTkEntry:
        """
        :return: Возвращает объект класса CTkEntry для названия списка покупок
        """
        return self.__name_shopping_list


    def __get_name_product(self) -> ctk.CTkEntry:
        """
        :return: Возвращает объект класса CTkEntry для названия товара
        """
        return self.__name_product


    def __get_count_product(self) -> ctk.CTkEntry:
        """
        :return: Возвращает объект класса CTkEntry для количества товара
        """
        return self.__count_product


    def __get_category_product(self) -> ctk.CTkComboBox:
        """
        :return: Возвращает объект класса CTkComboBox для категории товара
        """
        return self.__category_product


    name_shopping_list = property(__get_name_shopping_list)
    name_product = property(__get_name_product)
    count_product = property(__get_count_product)
    category = property(__get_category_product)



class MenuButtonsCreateList(ctk.CTkFrame):
    """
    Класс- контейнер, формирует область с кнопками, отвечающими за функционал страницы
    """
    def __init__(self, main_window: CreateList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window

        self.__config_menu_buttons()


    def __config_menu_buttons(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же устанавливает их параметры и стили
        """
        self.__save_lst = ctk.CTkButton(self, text=tt_s, width=wh_bm, fg_color=fgc_bm, height=ht_bm, text_color=tc_bm,
                                      border_width=bw_bm, hover_color=hc_bm, font=ft_bm)
        self.__save_lst.configure(command=self.__main_window.save_button_click_handler)
        self.__save_lst.place(relx=0.05, rely=0.2)

        self.__edit_product = ctk.CTkButton(self, text=tt_e, width=wh_bm, fg_color=fgc_bm, height=ht_bm, text_color=tc_bm,
                                      border_width=bw_bm, hover_color=hc_bm, font=ft_bm)
        self.__edit_product.configure(command=self.__main_window.edit_button_click_handler)
        self.__edit_product.place(relx=0.375, rely=0.2)

        self.__del_product = ctk.CTkButton(self, text=tt_d, width=wh_bm, fg_color=fgc_bm, height=ht_bm, text_color=tc_bm,
                                     border_width=bw_bm, hover_color=hc_bm, font=ft_bm)
        self.__del_product.configure(command=self.__main_window.del_button_click_handler)
        self.__del_product.place(relx=0.705, rely=0.2)



class CreateList(ctk.CTkToplevel):
    """
    Мэйн класс страницы, в себе формирует контейнеры (фреймы), содержащие остальные виджеты страницы,
    А так же содержит основную логику, отвечающую за функционал страницы
    """
    def __init__(self, main_window):
        super().__init__()
        self.__main_window = main_window

        self.__load_data = sld.read_data_with_shopping_lists() if sld.check_file_shopping_lists() else {}

        self.__confirmation_request_page = None
        self.__edit_product_page = None
        self.__add_category_page = None

        self.__data_create_list = None
        self.__scroll_create_list = None
        self.__menu_btn_create_list = None

        self.__list_products = []

        self.__config_window()
        self.__config_create_list()
        self.__config_scroll_frame()
        self.__config_menu_buttons()
        self.__config_cancel_button()

        self.protocol("WM_DELETE_WINDOW", Templates.on_closing)


    def __config_window(self) -> None:
        """
        Формирует параметры и стили главного окна приложения
        """
        self.title(ttl)
        self.geometry(gt)
        self.resizable(rb_wh, rb_ht)


    def __config_scroll_frame(self) -> None:
        """
        Формирует параметры и стили контейнера для добавления товаров
        """
        self.__scroll_create_list = ScrollCreateList(self, master=self, width=wh_sf, height=ht_sf, fg_color=fgc_sf, corner_radius=cr_sf)
        self.__scroll_create_list.pack(pady=10, padx=(0, 280))


    def __config_create_list(self) -> None:
        """
        Формирует параметры и стили контейнера для добавления элементов товара, а так же кнопок добавления товара и добавления новой категории
        """
        self.__data_create_list = ConfigCreateList(self, master=self, width=wh_ccl, height=ht_ccl, fg_color=fgc_ccl,
                                                   corner_radius=cr_ccl)
        self.__data_create_list.pack()
        self.__data_create_list.pack_propagate(False)


    def __config_menu_buttons(self) -> None:
        """
        Формирует параметры и стили контейнера основного меню кнопок страницы
        """
        self.__menu_btn_create_list = MenuButtonsCreateList(self, master=self, width=w_bm, height=h_bm, fg_color=fg_bm, corner_radius=cr_bm)
        self.__menu_btn_create_list.pack()
        self.__menu_btn_create_list.pack_propagate(False)


    def __config_cancel_button(self):
        """
        Формирует параметры и стили кнопки возврата на предыдущую страницу
        """
        self.__cancel_btn = ctk.CTkButton(self, text=tt_c, width=wh_bm, fg_color=fgc_bm,height=ht_bm, text_color=tc_bm,
                                         border_width=bw_bm, hover_color=hc_bm, font=ft_bm)
        self.__cancel_btn.configure(command=self.cancel_button_click_handler)
        self.__cancel_btn.place(relx=0.705, rely=0.6)


    def add_product_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке добавления товара в список, при наступлении исключения - выбрасывает окно с ошибкой
        """
        assert self.__data_create_list.name_product.get() != '' and self.__data_create_list.count_product.get() != '' and self.__data_create_list.category.get() != '', showerror('Ошибка', 'Заполните все поля')

        assert self.__data_create_list.count_product.get().isdigit(), showerror('Ошибка', 'Количество товара может быть только целым числом')

        if Templates.checks_presence_element(self.__data_create_list.name_product.get(), self.__list_products):
            showerror('Ошибка', 'Такой продукт уже есть в списке')

            return

        self.__scroll_create_list.create_checkbox(self.__data_create_list.name_product.get(), self.__data_create_list.count_product.get(), self.__data_create_list.category.get())

        product = [self.__data_create_list.name_product.get(), self.__data_create_list.count_product.get(), self.__data_create_list.category.get()]

        self.__list_products.append(product)

        self.data_create_list.name_product.delete(0, END)
        self.data_create_list.count_product.delete(0, END)


    def add_category_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке добавления новой категории товара
        """
        self.__add_category_page = AddNewCategory(self)

        self.__add_category_page.grab_set()


    def update_load_data(self, old_text: str, new_text: str) -> bool:
        """
        Обходит матрицу продуктов, сравнивает полученный текст и текст из чекбокса, если они совпадают то меняет по индесу старый продукт на новый
        :param old_text: Старый текст чекбокса, до редактирования
        :param new_text: Новый текст чекбокса, после редактирования
        """
        old_text = old_text.split(', ')
        new_text = new_text.split(', ')

        for index, elem in enumerate(self.__list_products):
            if elem == old_text:
                self.__list_products[index] = new_text
                return True
        return False


    def edit_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке редактирования товара, при наступлении исключения - выбрасывает окно с ошибкой
        """
        assert self.__scroll_create_list.count_checkboxes != 0, showerror('Ошибка', 'Список товаров пуст, редактировать нечего')

        if not self.__scroll_create_list.check_selected_checkbox():
            showerror('Ошибка', 'Выберите товар для редактирования')
            return

        if len(self.__scroll_create_list.create_list_select_checkboxes()) != 1:
            showerror('Ошибка', 'Одновременно редактировать можно только 1 товар')
            return

        self.__edit_product_page = EditProduct(self, self.__scroll_create_list)

        self.__edit_product_page.grab_set()


    def del_target_condition(self) -> None:
        """
        При помощи метода create_list_text_select_checkbox получает список текстов активных чекбоксов
        Каждый элемент списка сплитуется по запятым и на следующем этапе цикла формируется новая матрица self.__list_products на основе старой
        Но уже с теми элементами, которые не равны тем, что находятся в списке активных чекбоксов
        """
        for text in self.scroll_create_list.create_list_text_select_checkbox():

            product_to_remove = text.split(', ')

            self.__list_products = [product for product in self.__list_products if product != product_to_remove]


    def del_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке удаления товара, при наступлении исключения - выбрасывает окно с ошибкой
        """
        assert self.__scroll_create_list.count_checkboxes != 0, showerror('Ошибка', 'Список товаров пуст, удалять нечего')

        if not self.__scroll_create_list.check_selected_checkbox():
            showerror('Ошибка', 'Выберите товар для удаления')
            return

        self.__confirmation_request_page = ConfirmationPage(self, self.__scroll_create_list)

        self.__confirmation_request_page.grab_set()


    def save_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке сохранения списка покупок, при наступлении исключения - выбрасывает окно с ошибкой
        """
        from src.lists.all_lists import AllLists

        assert self.__scroll_create_list.count_checkboxes != 0, showerror('Ошибка', 'Добавьте товар или нажмите "Отмена"')

        assert self.__data_create_list.name_shopping_list.get() != '', showerror('Ошибка', 'Добавьте название списка покупок или нажмите "Отмена"')

        sld.create_folder()

        self.__load_data[self.__data_create_list.name_shopping_list.get()] = self.__list_products

        if isinstance(self.__main_window, AllLists):
            self.__main_window.scroll_all_lists.add_new_checkbox(self.__data_create_list.name_shopping_list.get())

        sld.write_data_in_shopping_lists(self.__load_data)

        self.__main_window.deiconify()

        self.destroy()


    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        self.__main_window.deiconify()

        self.destroy()


    def __get_scroll_frame(self) -> ScrollCreateList:
        """
        :return: Возвращает объект класса ScrollCreateList
        """
        return self.__scroll_create_list


    def __get_list_products(self) -> list[list[str]]:
        """
        :return: Возвращает список продуктов в виде матрицы
        """
        return self.__list_products

    def __get_data_create_list(self) -> ConfigCreateList:
        """
        :return: Возвращает объект класса ConfigCreateList
        """
        return self.__data_create_list

    data_create_list = property(__get_data_create_list)
    scroll_create_list = property(__get_scroll_frame)
    list_products = property (__get_list_products)
