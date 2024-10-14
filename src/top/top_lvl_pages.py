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