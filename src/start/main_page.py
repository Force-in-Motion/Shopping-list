import customtkinter as ctk
from PIL import Image
import sys

from src.start.config_main_page import *
from src.lists.all_lists import *
from src.create.create_list import *
from src.favorite.favorite_product import *
from src.history.purchase_history import *
from src.open.open_list import *


class MainFrame(ctk.CTkFrame):
    """
    Класс, реализующий главное окно приложения
    """
    def __init__(self, main_window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window

        self.__config_logo()
        self.__config_menu_buttons()
        self.__config_exit_button()


    def __config_menu_buttons(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за общий функционал приложения, а так же устанавливает его параметры и стили
        """
        self.__add_list = ctk.CTkButton(self, text=al_tt, width=wh_al, fg_color=fgc_mf, border_color=bc_mf,
                                      height=ht_mf, text_color=tc_mf, border_width=bw_m, hover_color=hc_mf, font=ft_mf)
        self.__add_list.place(relx=0.05, rely=0.2)
        self.__add_list.configure(command=self.__main_window.add_list_button_click_handler)

        self.__my_lists = ctk.CTkButton(self, text=ml_tt, width=wh_mf, fg_color=fgc_mf, border_color=bc_mf,
                                      height=ht_mf, text_color=tc_mf, border_width=bw_mf, hover_color=hc_mf, font=ft_mf)
        self.__my_lists.place(relx=0.05, rely=0.55)
        self.__my_lists.configure(command=self.__main_window.all_lists_button_click_handler)

        self.__favorites = ctk.CTkButton(self, text=f_tt, width=wh_mf, fg_color=fgc_mf, border_color=bc_mf,
                                       height=ht_mf, text_color=tc_mf, border_width=bw_mf, hover_color=hc_mf, font=ft_mf)
        self.__favorites.place(relx=0.38, rely=0.55)
        self.__favorites.configure(command=self.__main_window.favorites_button_click_handler)

        self.__history = ctk.CTkButton(self, text=h_tt, width=wh_mf, fg_color=fgc_mf, hover_color=hc_mf,
                                     height=ht_mf, text_color=tc_mf, border_width=bw_mf, border_color=bc_mf, font=ft_mf)
        self.__history.place(relx=0.7, rely=0.55)
        self.__history.configure(command=self.__main_window.history_button_click_handler)


    def __config_exit_button(self) -> None:
        """
        Формирует в себе кнопку, отвечающую за выход из приложения и устанавливает ее в указанное место окна, а так же устанавливает его параметры и стили
        """
        self.__exit = ctk.CTkButton(self, text=e_tt, width=wh_e, height=ht_e, fg_color=fgc_e, hover_color=hc_e, text_color=tc_e, font=ft_e)
        self.__exit.place(relx=0.38, rely=0.85)
        self.__exit.configure(command=sys.exit)


    def __config_logo(self) -> None:
        """
        Устанавливает логотип приложения в указанное место окна, а так же устанавливает его параметры и стили
        """
        self.__logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size)
        self.__image_label = ctk.CTkLabel(self, image=self.__logo, text=l_tt)
        self.__image_label.place(relx=0.7, rely=0.1)



class MainPage(ctk.CTk):
    """
    Мэйн класс приложения, в себе формирует основной контейнер (фрейм), содержащий остальные виджеты страницы
    """
    def __init__(self):
        super().__init__()
        self.__load_data = sld.read_data_with_shopping_lists() if sld.check_file_shopping_lists() else {}

        self.__add_list_page = None
        self.__all_lists_page = None
        self.__history_page = None
        self.__favorite_products_page = None

        self.__config_window()
        self.__config_main_frame()

        self.protocol("WM_DELETE_WINDOW", Templates.on_closing)

    def __config_window(self) -> None:
        """
        Формирует параметры и стили главного окна приложения
        """
        self.title(ttl_mp)
        self.geometry(gmt)
        self.resizable(rsb_wh, rsb_ht)


    def __config_main_frame(self):
        """
        Формирует основной контейнер (фрейм) содержащий остальные виджеты страницы
        """
        self.__main_frame = MainFrame(self, master=self, width=wh_f, height=ht_f, fg_color=fgc_f, corner_radius=cr_f)
        self.__main_frame.pack()
        self.__main_frame.pack_propagate(False)


    def add_list_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке добавления список покупок
        """
        self.__add_list_page = CreateList(self)

        self.withdraw()


    def all_lists_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке "мои списки"
        """
        self.__all_lists_page = AllLists(self)

        self.withdraw()


    def favorites_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке "избранное"
        """
        self.__favorite_products_page = FavoriteProducts(self)

        self.withdraw()


    def history_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке "история покупок"
        """
        self.__history_page = PurchaseHistory(self)

        self.withdraw()


    @classmethod
    def run_program(cls) -> None:
        """
        Запускает главное окно приложения
        """
        page = cls()
        page.lift()
        page.attributes('-topmost', True)
        page.mainloop()

