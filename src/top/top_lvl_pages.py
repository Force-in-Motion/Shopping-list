import customtkinter as ctk
from PIL import Image
from tkinter.messagebox import showerror

from src.top.config_top_level_pages import *
from src.load.save_and_load_data import SaveAndLoadData as sld
from src.templates.templates import Templates



class AddNewCategory(ctk.CTkToplevel):
    """
    Класс, описывающий функционал окна верхнего уровня и его виджеты
    """
    def __init__(self, main_window, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.__main_window = main_window
        self.__list_categories = sld.read_categories()

        self.__input_field = None

        self.__config_logo()
        self.__config_window()
        self.__config_input_field()
        self.__config_menu_buttons()


    def __config_window(self) -> None:
        """
        Формирует параметры и стили главного окна приложения
        """
        self.geometry(gt_cw_anc)
        self.title(ttl_cw_anc)
        self.resizable(wh_rzb, ht_rzb)


    def __config_input_field(self) -> None:
        """
        Формирует в себе поля ввода данных пользователя
        """
        self.__input_field = ctk.CTkEntry(self, placeholder_text=pht_if, placeholder_text_color=phtc_if,
                                          width=wh_if, height=ht_if, fg_color=fgc_if, font=ft_if, text_color=tc_nsl)
        self.__input_field.place(relx=0.05, rely=0.2)


    def __config_logo(self) -> None:
        """
        Формирует параметры и стили главного логотипа приложения
        """
        self.__logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size_ltl)
        self.__image_label = ctk.CTkLabel(self, image=self.__logo, text=tt_l)
        self.__image_label.place(relx=0.67, rely=0.1)

    def __config_menu_buttons(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же устанавливает его параметры и стили
        """
        self.__save_btn = ctk.CTkButton(self, text=tt_sb, width=wh_sb, fg_color=fgc_sb, height=ht_sb,
                                        text_color=tc_sb, border_width=bw_sb, hover_color=hc_sb, font=ft_sb)
        self.__save_btn.configure(command=self.save_button_click_handler)
        self.__save_btn.place(relx=0.05, rely=0.7)

        self.__cancel_btn = ctk.CTkButton(self, text=tt_cb, width=wh_cb, fg_color=fgc_cb, height=ht_cb,
                                          text_color=tc_cb, border_width=bw_cb, hover_color=hc_cb, font=ft_cb)
        self.__cancel_btn.configure(command=self.cancel_button_click_handler)
        self.__cancel_btn.place(relx=0.62, rely=0.7)

    def save_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке сохранения списка покупок
        """
        assert self.input_data != '', showerror('Ошибка', 'Пустая строка не может быть принята')

        self.__list_categories["cs"].append(self.input_data)

        sld.write_categories(self.__list_categories)

        self.__main_window.deiconify()

        self.__main_window.data_create_list.category.configure(values=self.__list_categories.get("cs"))

        self.destroy()

    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        self.__main_window.deiconify()

        self.destroy()


    def __get_input_field_data(self) -> str:
        """
        Возвращает данные из поля ввода пользователя
        """
        return self.__input_field.get()

    input_data = property(__get_input_field_data)


class EditNameShoppingList(AddNewCategory):
    """
    Класс, описывающий функционал окна верхнего уровня и его виджеты
    """
    def __init__(self, main_window, scroll_all_lists, *args, **kwargs):
        super().__init__(main_window, *args, **kwargs)
        self.__main_window = main_window
        self.__scroll_all_lists = scroll_all_lists

        self.title(ttl_ensl)

    def save_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке сохранения списка покупок
        """
        assert self.input_data != '', showerror('Ошибка', 'Пустая строка не может быть принята')

        text, checkbox = self.__scroll_all_lists.get_selected_checkbox()

        self.__scroll_all_lists.set_new_text_for_checkbox(checkbox, self.input_data)

        if text in self.__main_window.load_data:
            self.__main_window.load_data[self.input_data] = self.__main_window.load_data.pop(text)

            sld.write_data_in_shopping_lists(self.__main_window.load_data)

            self.__scroll_all_lists.reset_checkboxes()

        self.__main_window.deiconify()

        self.destroy()

    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        self.__scroll_all_lists.reset_checkboxes()

        self.__main_window.deiconify()

        self.destroy()


class EditProduct(ctk.CTkToplevel):
    """
    Класс, описывающий функционал окна верхнего уровня и его виджеты
    """
    def __init__(self, main_window, scroll_frame, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window
        self.__scroll_frame = scroll_frame

        self.__name_product = None
        self.__count_product = None
        self.__category_product = None

        self.__list_categories = sld.read_categories()

        self.__config_window()
        self.__config_logo()
        self.__config_input_fields()
        self.__config_menu_buttons()
        self.__config_category_list()

    def __config_window(self) -> None:
        """
        Формирует параметры и стили главного окна приложения
        """
        self.geometry(gt_cw_ap)
        self.title(ttl_cw_ap)

    def __config_input_fields(self) -> None:
        """
        Формирует в себе поля ввода данных пользователя
        """
        self.__name_product = ctk.CTkEntry(self, placeholder_text=pht_np, placeholder_text_color=phtc_np,
                                         width=wh_np, height=ht_np, fg_color=fgc_np, font=ft_np, text_color=tc_np)
        self.__name_product.place(relx=0.04, rely=0.2)

        self.__count_product = ctk.CTkEntry(self, placeholder_text=pht_cp, placeholder_text_color=phtc_cp,
                                          width=wh_cp, height=ht_cp, fg_color=fgc_cp, font=ft_cp, text_color=tc_cp)
        self.__count_product.place(relx=0.373, rely=0.2)

    def __config_category_list(self) -> None:
        """
        Формирует в себе список, доступных по умолчанию, категорий товара
        :return:
        """
        self.__category_product = ctk.CTkComboBox(self,  text_color=tc_c,  width=wh_c, height=ht_c, fg_color=fgc_c, font=ft_c,
                                        state=st_c, button_color=bc_c)
        self.__category_product.configure(values=self.__list_categories.get("cs"))
        self.__category_product.place(relx=0.52, rely=0.2)

    def __config_logo(self) -> None:
        """
        Формирует параметры и стили главного логотипа приложения
        """
        self.__logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size_ltl)
        self.__image_label = ctk.CTkLabel(self, image=self.__logo, text=tt_l)
        self.__image_label.place(relx=0.75, rely=0.1)


    def __config_menu_buttons(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же устанавливает его параметры и стили
        """
        self.__save_btn = ctk.CTkButton(self, text=tt_sb, width=wh_sb, fg_color=fgc_sb,
                                         height=ht_sb, text_color=tc_sb, border_width=bw_sb, hover_color=hc_sb,
                                         font=ft_sb)
        self.__save_btn.configure(command=self.save_button_click_handler)
        self.__save_btn.place(relx=0.04, rely=0.7)

        self.__cancel_btn = ctk.CTkButton(self, text=tt_cb, width=wh_cb, fg_color=fgc_cb,
                                      height=ht_cb, text_color=tc_cb, border_width=bw_cb, hover_color=hc_cb,
                                      font=ft_cb)
        self.__cancel_btn.configure(command=self.cancel_button_click_handler)
        self.__cancel_btn.place(relx=0.71, rely=0.7)


    def edit_data_checkbox(self) -> None:
        """
        Обновляет текст в загруженных списках покупок, соответствующий текущему пункту из чекбокса
        """
        new_text = f'{self.name_product}, {self.count_product}, {self.category}'

        old_text, check_box = self.__scroll_frame.get_selected_checkbox()

        self.__main_window.update_load_data(old_text, new_text)

        self.__scroll_frame.set_new_text_for_checkbox(check_box, new_text)


    def save_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке сохранения списка покупок
        """
        assert self.name_product != '' and self.count_product != '' and self.category != '', showerror('Ошибка', 'Заполните все поля')

        assert self.count_product.isdigit(), showerror('Ошибка', 'Количество товара может быть только целым числом')

        self.edit_data_checkbox()

        self.__scroll_frame.reset_checkboxes()

        self.__main_window.deiconify()

        self.destroy()


    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        self.__main_window.deiconify()

        self.__scroll_frame.reset_checkboxes()

        self.destroy()

    def __get_name_product(self) -> str:
        """
        Возвращает текущее значение поля ввода имени товара
        """
        return self.__name_product.get()

    def __get_count_product(self) -> int:
        """
        Возвращает количество товара
        """
        return self.__count_product.get()

    def __get_category_product(self) -> str:
        """
        Возвращает, введенную пользователем, категорию
        """
        return self.__category_product.get()


    name_product = property(__get_name_product)
    count_product = property(__get_count_product)
    category = property(__get_category_product)


class AddProduct(EditProduct):
    """
    Класс, описывающий функционал окна верхнего уровня и его виджеты
    """
    def __init__(self, main_window, scroll_frame, *args, **kwargs):
        super().__init__(main_window, scroll_frame, *args, **kwargs)

        self.__main_window = main_window
        self.__scroll_frame = scroll_frame


    def save_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке сохранения списка покупок
        """
        from src.favorite.favorite_product import FavoriteProducts

        assert self.name_product != '' and self.count_product != '' and self.category != '', showerror('Ошибка', 'Заполните все поля')

        assert self.count_product.isdigit(), showerror('Ошибка', 'Количество товара может быть только целым числом')

        if Templates.checks_presence_element(self.name_product, self.__main_window.list_products):
            showerror('Ошибка', 'Такой продукт уже есть в списке')
            return

        self.__scroll_frame.create_checkbox(self.name_product, self.count_product, self.category)

        product = [self.name_product, self.count_product, self.category]

        if isinstance(self.__main_window, FavoriteProducts):

            self.__main_window.load_data_favorites["f"].append(', '.join(product))

            sld.write_data_in_favorites_products(self.__main_window.load_data_favorites)

            self.__main_window.deiconify()

            self.destroy()

            return

        self.__main_window.list_products.append(product)

        self.__main_window.load_data[self.__scroll_frame.list_name] = self.__main_window.list_products

        sld.write_data_in_shopping_lists(self.__main_window.load_data)

        self.__main_window.deiconify()

        self.destroy()


class ConfirmationPage(ctk.CTkToplevel):
    """
    Класс, описывающий функционал окна верхнего уровня и его виджеты
    """
    def __init__(self,  main_window, scroll_frame, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window
        self.__scroll_frame = scroll_frame

        self.__label_confirm = None

        self.__config_window()
        self.__config_label_confirm()
        self.__config_menu_buttons()


    def __config_window(self) -> None:
        """
        Формирует параметры и стили главного окна приложения
        """
        self.title(ttl_cp)
        self.geometry(gt_cp)


    def __config_label_confirm(self) -> None:
        """
        Формирует в себе текст, описывающий назначение окна
        """
        self.__label_confirm = ctk.CTkLabel(self, width=wh_cl, height=ht_cl, text=tt_cl, text_color=tc_cl, font=ft_cl)
        self.__label_confirm.place(relx=0.3, rely=0.1)


    def __config_menu_buttons(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же устанавливает его параметры и стили
        """
        self.__confirm_btn = ctk.CTkButton(self, width=wh_cmb, height=ht_cmb, text=tt_cmb, fg_color=fgc_cmb,
                                         text_color=tc_cmb, border_width=bw_cmb, hover_color=hc_cmb, font=ft_cmb)
        self.__confirm_btn.configure(command=self.confirm_button_click_handler)
        self.__confirm_btn.place(relx=0.05, rely=0.6)

        self.__cancel_btn = ctk.CTkButton(self, text=tt_clb, width=wh_clb, fg_color=fgc_clb, height=ht_clb,
                                              text_color=tc_clb, border_width=bw_clb, hover_color=hc_clb, font=ft_clb)
        self.__cancel_btn.configure(command=self.cancel_button_click_handler)
        self.__cancel_btn.place(relx=0.64, rely=0.6)


    def confirm_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке сохранения списка покупок
        """
        self.__main_window.del_target_condition()

        self.__scroll_frame.delete_checkbox()

        self.__main_window.deiconify()

        self.destroy()


    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        self.__scroll_frame.reset_checkboxes()

        self.__main_window.deiconify()

        self.destroy()


class ConfirmationClearScrollPlace(ConfirmationPage):
    """
    Класс, описывающий функционал окна верхнего уровня и его виджеты
    """
    def __init__(self,  main_window, scroll_frame, *args, **kwargs):
        super().__init__(main_window, scroll_frame, *args, **kwargs)
        self.__main_window = main_window
        self.__scroll_frame = scroll_frame


    def confirm_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке сохранения списка покупок
        """
        from src.favorite.favorite_product import FavoriteProducts

        self.__scroll_frame.clear_scroll_frame()

        if isinstance(self.__main_window, FavoriteProducts):
            self.__main_window.load_data_favorites["f"].clear()

            sld.write_data_in_favorites_products(self.__main_window.load_data_favorites)

            self.__main_window.deiconify()

            self.destroy()

            return

        self.__main_window.load_data_purchase_history.clear()

        sld.write_data_in_purchase_history(self.__main_window.load_data_purchase_history)

        self.__main_window.deiconify()

        self.destroy()

        return


class ViewListPurchaseHistory(ctk.CTkToplevel):
    """
    Класс, описывающий объект, который открывает выбранный список и демонстрирует его содержимое
    """
    def __init__(self,  main_window, scroll_frame, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__main_window = main_window
        self.__scroll_frame = scroll_frame
        self.__load_purchase_history = sld.read_data_with_purchase_history() if sld.check_file_purchase_history() else {}

        self.__scroll_view_list_history = None

        self.__config_window()
        self.__config_scroll_frame()
        self.__config_cancel_button()
        self.__load_checkbox_products()


    def __config_window(self) -> None:
        """
        Формирует параметры и стили главного окна приложения
        """
        self.title(ttl_olph)
        self.geometry(gt_olph)


    def __config_scroll_frame(self) -> None:
        """
        Формирует параметры и стили области просмотра списка покупок
        """
        self.__scroll_view_list_history = ctk.CTkScrollableFrame(self, width=wh_solf, height=ht_solf, fg_color=fgc_solf, corner_radius=cr_solf)
        self.__scroll_view_list_history.place(relx=0.05, rely=0.05)