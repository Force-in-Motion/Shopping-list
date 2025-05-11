import customtkinter as ctk
import pytest

from src.favorite.favorite_product import ScrollFavoriteProducts, FavoriteProducts
from src.start.main_page import MainPage


start_window = MainPage()

favorite = FavoriteProducts(start_window)

scroll_favorite = ScrollFavoriteProducts(favorite, favorite)


@pytest.fixture(scope='session')
def fills_list_checkboxes():
    """
    Заполняет список чекбоксами, подготавливая среду для тестирования
    """
    checkbox_1 = ctk.CTkCheckBox(scroll_favorite, text='кочерга, 4, Инструменты')
    checkbox_1.select()

    checkbox_2 = ctk.CTkCheckBox(scroll_favorite, text='скакалка, 4, Спорт. Товары')
    checkbox_2.deselect()

    checkbox_3 = ctk.CTkCheckBox(scroll_favorite, text='леска, 4, Рыбалка')
    checkbox_3.deselect()

    checkbox_4 = ctk.CTkCheckBox(scroll_favorite, text='ружье, 4, Охота')
    checkbox_4.select()

    checkbox_5 = ctk.CTkCheckBox(scroll_favorite, text='ружье, 4, Охота')
    checkbox_5.select()

    checkbox_6 = ctk.CTkCheckBox(scroll_favorite, text='ружье, 4, Охота')
    checkbox_6.deselect()

    checkbox_7 = ctk.CTkCheckBox(scroll_favorite, text='ружье, 4, Охота')
    checkbox_7.select()

    return scroll_favorite.list_checkboxes.extend([checkbox_1, checkbox_2, checkbox_3, checkbox_4, checkbox_5, checkbox_6, checkbox_7])


# ================================================================ ScrollFavoriteProducts ======================================================================


data_test_fp_create_checkbox = [('ананас', 4, 'Продукты питания', None),
                                ('кочерга', 4, 'Инструменты', None),
                                ('скакалка', 4, 'Спорт. Товары', None),
                                ('леска', 4, 'Рыбалка', None),
                                ('ружье', 4, 'Охота', None)]


@pytest.mark.SFP_create_checkbox
@pytest.mark.parametrize('val1, val2, val3, expect_result', data_test_fp_create_checkbox)
def test_create_checkbox(val1, val2, val3, expect_result):
    """
    Проверяет создание нового чекбокса в скролле фрейма и проверяет, что чекбокс добавлен в список
    """
    count_checkboxes_in_list = len(scroll_favorite.list_checkboxes)

    assert scroll_favorite.create_checkbox(val1, val2, val3) is None

    assert len(scroll_favorite.list_checkboxes) == count_checkboxes_in_list + 1


@pytest.mark.SFP_list_select_checkboxes
def test_create_list_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции фильтрации чекбоксов и создания списка активных чекбоксов, а так же тип элементов списка
    """

    result = scroll_favorite.create_list_select_checkboxes()

    for i in result:
        assert type(i) == ctk.CTkCheckBox

    assert len(result) == 4


@pytest.mark.SFP_list_text_select_checkboxes
def test_create_list_text_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции фильтрации чекбоксов и создания списка текстов активных чекбоксов, а так же тип элементов списка
    """
    result = scroll_favorite.create_list_text_select_checkbox()

    for i in result:
        assert type(i) == str

    assert len(result) == 4


@pytest.mark.SFP_delete_checkbox
def test_delete_checkbox():
    """
    Проверяет удаление чекбокса из скролл фрейма и проверяет, что чекбокс удален из списка
    """
    initial_count = scroll_favorite.count_checkboxes

    assert initial_count == 12

    scroll_favorite.delete_checkbox()

    current_count = scroll_favorite.count_checkboxes

    assert current_count == 8


@pytest.mark.SFP_check_select_checkboxes
def test_check_select_checkboxes():
    """
    Проверяет работу функции проверки выбора чекбоксов
    """
    for i in scroll_favorite.list_checkboxes:
        i.select()

    assert scroll_favorite.check_selected_checkbox() is True

    scroll_favorite.reset_checkboxes()

    assert scroll_favorite.check_selected_checkbox() is False


@pytest.mark.SFP_reset_checkboxes
def test_reset_checkboxes():
    """
    Проверяет работу функции сброса чекбоксов и что все чекбоксы не выбраны
    """
    for i in scroll_favorite.list_checkboxes:
        i.select()

    assert scroll_favorite.check_selected_checkbox() is True

    scroll_favorite.reset_checkboxes()

    assert scroll_favorite.check_selected_checkbox() is False


@pytest.mark.SFP_clear_scroll_frame
def test_clear_scroll_frame():
    """
    Проверяет работу функции очистки скролл фрейма и проверяет, что чекбоксы удалены из списка
    """
    initial_count = scroll_favorite.count_checkboxes

    assert initial_count == 8

    scroll_favorite.clear_scroll_frame()

    current_count = scroll_favorite.count_checkboxes

    assert current_count == 0


@pytest.mark.SFP_get_list_checkboxes
def test_get_list_checkboxes():
    """
    Проверяет возвращаемое значение
    """
    assert type(scroll_favorite.list_checkboxes) == list


@pytest.mark.SFP_count_checkboxes
def test_get_count_checkboxes():
    """
    Проверяет работу функции получения количества чекбоксов и проверяет, что оно верно считает чекбоксы
    """
    assert scroll_favorite.count_checkboxes == 0


# ================================================================ FavoriteProducts ======================================================================

@pytest.mark.FP_add_product
def test_add_product():
    """
    Проверяет возвращаемое значение
    """

    assert favorite.add_button_click_handler() is None


@pytest.mark.FP_del_target_condition
def test_del_target_condition():
    """
    Проверяет удаление элементов соглавно условия
    """
    scroll_favorite.create_checkbox('ананас', 4, 'Продукты питания')

    select_checkbox = scroll_favorite.list_checkboxes[0]
    select_checkbox.select()

    assert favorite.del_target_condition() is None

    assert select_checkbox not in favorite.list_products


@pytest.mark.FP_cancel_button_click_handler
def test_cancel_button_click_handler():
    """
    Проверяет работу метода возврата к главному окну и закрытия текущего
    """
    assert favorite.cancel_button_click_handler() == favorite.destroy()


@pytest.mark.FP_get_scroll_favorite
def test_get_scroll_favorite():
    """
    Проверяет возвращаемое значение
    """

    assert type(favorite.scroll_favorite) == ScrollFavoriteProducts


@pytest.mark.FP_load_data_favorites
def test_load_data_favorites():
    """
    Проверяет возвращаемое значение
    """

    assert type(favorite.load_data_favorites) is dict


@pytest.mark.FP_get_list_products
def test_get_list_products():
    """
    Проверяет возвращаемое значение
    """

    assert type(favorite.list_products) is list