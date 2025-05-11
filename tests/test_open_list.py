import pytest
import customtkinter as ctk

from src.lists.all_lists import ScrollAllLists, AllLists
from src.open.open_list import ScrollOpenListProducts, OpenList
from src.start.main_page import MainPage


start_window = MainPage()

all_lists = AllLists(start_window)

scroll_all_lists = ScrollAllLists(all_lists, all_lists)

open = OpenList(all_lists, scroll_all_lists)

scroll_open_list = ScrollOpenListProducts(open, open)



@pytest.fixture(scope='session')
def fills_list_checkboxes():
    """
    Заполняет список чекбоксами, подготавливая среду для тестирования
    """
    checkbox_1 = ctk.CTkCheckBox(scroll_open_list, text='кочерга')
    checkbox_1.select()

    checkbox_2 = ctk.CTkCheckBox(scroll_open_list, text='скакалка')
    checkbox_2.deselect()

    checkbox_3 = ctk.CTkCheckBox(scroll_open_list, text='леска')
    checkbox_3.deselect()

    checkbox_4 = ctk.CTkCheckBox(scroll_open_list, text='ружье')
    checkbox_4.select()

    checkbox_5 = ctk.CTkCheckBox(scroll_open_list, text='ружье')
    checkbox_5.select()

    checkbox_6 = ctk.CTkCheckBox(scroll_open_list, text='ружье')
    checkbox_6.deselect()

    checkbox_7 = ctk.CTkCheckBox(scroll_open_list, text='ружье')
    checkbox_7.select()

    return scroll_open_list.list_checkboxes.extend([checkbox_1, checkbox_2, checkbox_3, checkbox_4, checkbox_5, checkbox_6, checkbox_7])


@pytest.fixture
def setup_checkboxes():
    checkbox = ctk.CTkCheckBox(scroll_open_list, text='Test List')
    checkbox.select()
    scroll_open_list.list_checkboxes.append(checkbox)


#================================================================ ScrollOpenListProducts ======================================================================

data_test_scl_create_checkbox = [( 'ананас', 4, 'Продукты питания', None),
                                 ( 'кочерга', 4, 'Инструменты', None),
                                 ( 'скакалка', 4, 'Спорт. Товары', None),
                                 ( 'леска', 4, 'Рыбалка', None),
                                 ( 'ружье', 4, 'Охота', None)]

@pytest.mark.SOL_create_checkbox
@pytest.mark.parametrize('val1, val2, val3, expect_result', data_test_scl_create_checkbox)
def test_create_checkbox(val1, val2, val3, expect_result):
    """
    Проверяет создание нового чекбокса в скролле фрейма и проверяет, что чекбокс добавлен в список
    """
    count_checkboxes_in_list = len(scroll_open_list.list_checkboxes)

    assert scroll_open_list.create_checkbox(val1, val2, val3) is None

    assert len(scroll_open_list.list_checkboxes) == count_checkboxes_in_list + 1


@pytest.mark.SOL_list_select_checkboxes
def test_create_list_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции фильтрации чекбоксов и создания списка активных чекбоксов, а так же тип элементов списка
    """
    result = scroll_open_list.create_list_select_checkboxes()

    for i in result:
        assert type(i) == ctk.CTkCheckBox

    assert len(result) == 4


@pytest.mark.SOL_list_text_select_checkboxes
def test_create_list_text_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции фильтрации чекбоксов и создания списка текстов активных чекбоксов, а так же тип элементов списка
    """
    result = scroll_open_list.create_list_text_select_checkbox()

    for i in result:
        assert type(i) == str

    assert len(result) == 4


@pytest.mark.SOL_delete_checkbox
def test_delete_checkbox():
    """
    Проверяет удаление чекбокса из скролл фрейма и проверяет, что чекбокс удален из списка
    """
    initial_count = scroll_open_list.count_checkboxes

    assert initial_count == 12

    scroll_open_list.delete_checkbox()

    current_count = scroll_open_list.count_checkboxes

    assert current_count == 8


@pytest.mark.SOL_get_select_checkboxes
def test_get_select_checkboxes():
    """
    Проверяет работу функции получения чекбоксов и возвращения текста активных чекбоксов или вернет (None, None)
    """
    for i in scroll_open_list.list_checkboxes:
        i.select()

    text, elem = scroll_open_list.get_selected_checkbox()

    assert text == 'скакалка'

    assert elem == scroll_open_list.list_checkboxes[0]

    for i in scroll_open_list.list_checkboxes:
        i.deselect()

    assert scroll_open_list.get_selected_checkbox() == (None, None)


@pytest.mark.SOL_check_select_checkboxes
def test_check_select_checkboxes():
    """
    Проверяет работу функции проверки чекбоксов и создания списка активных чекбоксов, а так же проверяет, что чекбоксы отмечены
    """
    for i in scroll_open_list.list_checkboxes:
        i.select()

    assert scroll_open_list.check_selected_checkbox() is True

    scroll_open_list.reset_checkboxes()

    assert scroll_open_list.check_selected_checkbox() is False


@pytest.mark.SOL_reset_checkboxes
def test_reset_checkboxes():
    """
    Проверяет работу функции сброса чекбоксов и проверяет, что чекбоксы сняты с выбора
    """
    for i in scroll_open_list.list_checkboxes:
        i.select()

    assert scroll_open_list.check_selected_checkbox() is True

    scroll_open_list.reset_checkboxes()

    assert scroll_open_list.check_selected_checkbox() is False


@pytest.mark.SOL_return_all_checkboxes
def test_return_all_checkboxes():
    """
    Проверяет работу функции возврата всех чекбоксов и проверяет, что они вернутся в исходное состояние
    """
    assert scroll_open_list.count_checkboxes == 0

    scroll_open_list.return_all_checkboxes()

    assert scroll_open_list.count_checkboxes == len(open.list_products)


@pytest.mark.SOL_count_checkboxes
def test_get_count_checkboxes():
    """
    Проверяет работу функции получения количества чекбоксов и проверяет, что оно верно считает чекбоксы
    """
    assert scroll_open_list.count_checkboxes == 0


@pytest.mark.SOL_get_list_checkboxes
def test_get_list_checkboxes():
    """
    Проверяет возвращаемое значение
    """
    assert type(scroll_open_list.list_checkboxes) == list



@pytest.mark.SOL_get_list_name
def test_get_list_name():
    """
    Проверяет возвращаемое значение
    """
    assert type(scroll_open_list.list_name) == str

#
# ============================================================= OpenList ======================================================================

data_test_update_load_data = [( 'ананас, 4, Продукты питания', 'кочерга, 4, Инструменты', None),
                                 ( 'скакалка, 4, Спорт. Товары', 'леска, 4, Рыбалка', None)]

@pytest.mark.OL_update_load_data
@pytest.mark.parametrize('val1, val2, expect_result', data_test_update_load_data)
def test_update_load_data(val1, val2, expect_result):
    """
    Проверяет изменение загрузки списка товаров в окне OpenList
    """
    assert open.update_load_data(val1, val2) == expect_result

    assert open.load_data[0] == val2


@pytest.mark.OL_del_target_condition
def test_del_target_condition():
    """
    Проверяет удаление продукта из списка с условием
    """

    scroll_open_list.list_checkboxes.append(ctk.CTkCheckBox(scroll_open_list, text='ружье'))

    select_checkbox = scroll_open_list.list_checkboxes[0]
    select_checkbox.select()

    assert open.del_target_condition() is None

    assert select_checkbox not in open.load_data


@pytest.mark.OL_cancel_button
def test_cancel_button_click_handler():
    """
    Проверяет обработку кнопки отмены
    """
    assert open.cancel_button_click_handler() == open.destroy()


@pytest.mark.OL_get_load_data
def test_get_load_data():
    """
    Проверяет возвращаемое значение
    """

    assert type(open.load_data) is dict


@pytest.mark.OL_scroll_all_lists
def test_get_scroll_all_lists():
    """
    Проверяет возвращаемое значение
    """

    assert type(open.scroll_all_lists) == ScrollAllLists


@pytest.mark.OL_list_products
def test_get_list_products():
    """
    Проверяет возвращаемое значение
    """

    assert type(open.list_products) == list


@pytest.mark.OL_get_category_product
def test_get_category_product():
    """
    Проверяет возвращаемое значение
    """

    assert type(open.category_product) == str