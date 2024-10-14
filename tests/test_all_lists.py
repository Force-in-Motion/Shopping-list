import pytest
import customtkinter as ctk

from src.start.main_page import MainPage
from src.create.create_list import CreateList
from src.lists.all_lists import ScrollAllLists, AllLists


start_window = MainPage()

all_lists = AllLists(start_window)

scroll_all_lists = ScrollAllLists(all_lists, all_lists)

checkbox = ctk.CTkCheckBox(scroll_all_lists)


@pytest.fixture(scope='session')
def fills_list_checkboxes():
    """
    Заполняет список чекбоксами, подготавливая среду для тестирования
    """
    checkbox_1 = ctk.CTkCheckBox(scroll_all_lists, text='кочерга, 4, Инструменты')
    checkbox_1.select()

    checkbox_2 = ctk.CTkCheckBox(scroll_all_lists, text='скакалка, 4, Спорт. Товары')
    checkbox_2.deselect()

    checkbox_3 = ctk.CTkCheckBox(scroll_all_lists, text='леска, 4, Рыбалка')
    checkbox_3.deselect()

    checkbox_4 = ctk.CTkCheckBox(scroll_all_lists, text='ружье, 4, Охота')
    checkbox_4.select()

    checkbox_5 = ctk.CTkCheckBox(scroll_all_lists, text='ружье, 4, Охота')
    checkbox_5.select()

    checkbox_6 = ctk.CTkCheckBox(scroll_all_lists, text='ружье, 4, Охота')
    checkbox_6.deselect()

    checkbox_7 = ctk.CTkCheckBox(scroll_all_lists, text='ружье, 4, Охота')
    checkbox_7.select()

    return scroll_all_lists.list_checkboxes.extend([checkbox_1, checkbox_2, checkbox_3, checkbox_4, checkbox_5, checkbox_6, checkbox_7])



# ================================================================= ScrollAllLists ======================================================================

data_test_sal_add_new_checkbox = [('AAAAA', None),
                                 ('213124', None),
                                 ('dd32ddd', None),
                                 ('sdffsdf', None),
                                 ('ананас', None)]

@pytest.mark.SAL_add_new_checkbox
@pytest.mark.parametrize('val, expect_result', data_test_sal_add_new_checkbox)
def test_add_new_checkbox(val, expect_result):
    """
    Проверяет создание нового чекбокса в скролле фрейма и проверяет, что чекбокс добавлен в список
    """
    count_checkboxes_in_list = scroll_all_lists.count_checkboxes

    assert scroll_all_lists.add_new_checkbox(val) is None

    assert scroll_all_lists.count_checkboxes == count_checkboxes_in_list + 1


data_test_scl_set_new_text_for_checkbox = [(checkbox, 'ананас', None),
                                           (checkbox, 'кочерга', None),
                                           (checkbox, 'скакалка', None),
                                           (checkbox, 'леска', None),
                                           (checkbox, 'ружье', None),]

@pytest.mark.SAL_set_text_checkbox
@pytest.mark.parametrize('val1, val2, expect_result', data_test_scl_set_new_text_for_checkbox)
def test_set_new_text_for_checkbox(val1, val2, expect_result):
    """
    Проверяет установку нового текста для чекбокса и проверяет, что текст изменился
    """
    old_text_checkbox = val1.cget("text")

    assert scroll_all_lists.set_new_text_for_checkbox(val1, val2) is None

    assert val1.cget("text")!= old_text_checkbox


@pytest.mark.SAL_list_select_checkboxes
def test_create_list_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции фильтрации чекбоксов и создания списка активных чекбоксов, а так же тип элементов списка
    """
    result = scroll_all_lists.create_list_select_checkboxes()

    for i in result:
        assert type(i) == ctk.CTkCheckBox

    assert len(result) == 4


@pytest.mark.SAL_list_text_select_checkboxes
def test_create_list_text_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции фильтрации чекбоксов и создания списка текстов активных чекбоксов, а так же тип элементов списка
    """
    result = scroll_all_lists.create_list_text_select_checkbox()

    for i in result:
        assert type(i) == str

    assert len(result) == 4


@pytest.mark.SAL_delete_checkbox
def test_delete_checkbox():
    """
    Проверяет удаление чекбокса из скролл фрейма и проверяет, что чекбокс удален из списка
    """

    assert scroll_all_lists.count_checkboxes == 12

    scroll_all_lists.delete_checkbox()

    assert scroll_all_lists.count_checkboxes == 8


@pytest.mark.SAL_get_select_checkboxes
def test_get_select_checkboxes():
    """
    Проверяет работу функции получения чекбоксов и возвращения текста активных чекбоксов или вернет (None, None)
    """
    for i in scroll_all_lists.list_checkboxes:
        i.select()

    text, elem = scroll_all_lists.get_selected_checkbox()

    assert text == 'AAAAA'

    assert elem == scroll_all_lists.list_checkboxes[0]

    for i in scroll_all_lists.list_checkboxes:
        i.deselect()

    assert scroll_all_lists.get_selected_checkbox() == (None, None)


@pytest.mark.SAL_check_select_checkboxes
def test_check_select_checkboxes():
    """
    Проверяет работу функции проверки чекбоксов и создания списка активных чекбоксов, а так же проверяет, что чекбоксы отмечены
    """
    for i in scroll_all_lists.list_checkboxes:
        i.select()

    assert scroll_all_lists.check_selected_checkbox() is True

    scroll_all_lists.reset_checkboxes()

    assert scroll_all_lists.check_selected_checkbox() is False


@pytest.mark.SAL_reset_checkboxes
def test_reset_checkboxes():
    """
    Проверяет работу функции сброса чекбоксов и проверяет, что чекбоксы сняты с выбора
    """
    for i in scroll_all_lists.list_checkboxes:
        i.select()

    assert scroll_all_lists.check_selected_checkbox() is True

    scroll_all_lists.reset_checkboxes()

    assert scroll_all_lists.check_selected_checkbox() is False


@pytest.mark.SAL_count_checkboxes
def test_get_count_checkboxes():
    """
    Проверяет работу функции получения количества чекбоксов и проверяет, что оно верно считает чекбоксы
    """
    assert scroll_all_lists.count_checkboxes == 8


@pytest.mark.SAL_get_list_checkboxes
def test_get_list_checkboxes():
    """
    Проверяет возвращаемое значение
    """
    assert type(scroll_all_lists.list_checkboxes) == list


# ======================================================================PurchaseHistory ======================================================================

@pytest.mark.AL_del_target_condition
def test_del_target_condition():
    """
    Проверяет удаление продукта из списка с условием
    """

    scroll_all_lists.list_checkboxes.append(ctk.CTkCheckBox(scroll_all_lists, text='ружье'))

    select_checkbox = scroll_all_lists.list_checkboxes[0]
    select_checkbox.select()

    assert all_lists.del_target_condition() is None

    assert select_checkbox not in all_lists.load_data_purchase_history


@pytest.mark.AL_cancel_button
def test_cancel_button_click_handler():
    """
    Проверяет обработку кнопки отмены
    """
    assert all_lists.cancel_button_click_handler() == all_lists.destroy()


@pytest.mark.AL_get_load_data_purchase_history
def test_get_load_data_purchase_history():
    """
    Проверяет получение загруженных продуктов из истории
    """
    assert type(all_lists.load_data_purchase_history) == dict


@pytest.mark.AL_get_load_data
def test_get_load_data():
    """
    Проверяет возвращаемое значение
    """
    assert type(all_lists.load_data) is dict


@pytest.mark.AL_get_scroll_frame
def test_get_scroll_frame():
    """
    Проверяет возвращаемое значение
    """
    assert type(all_lists.scroll_all_lists) is ScrollAllLists


@pytest.mark.AL_get_shopping_list_page
def test_get_create_shopping_list_page():
    """
    Проверяет возвращаемое значение
    """
    assert type(all_lists.create_shopping_list_page) is None or CreateList