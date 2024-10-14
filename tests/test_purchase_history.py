import pytest
import customtkinter as ctk

from src.history.purchase_history import ScrollPurchaseHistory, PurchaseHistory
from src.start.main_page import MainPage


start_window = MainPage()

history = PurchaseHistory(start_window)

scroll_history = ScrollPurchaseHistory(history, history)




@pytest.fixture(scope='session')
def fills_list_checkboxes():
    """
    Заполняет список чекбоксами, подготавливая среду для тестирования
    """
    checkbox_1 = ctk.CTkCheckBox(scroll_history, text='кочерга')
    checkbox_1.select()

    checkbox_2 = ctk.CTkCheckBox(scroll_history, text='скакалка')
    checkbox_2.deselect()

    checkbox_3 = ctk.CTkCheckBox(scroll_history, text='леска')
    checkbox_3.deselect()

    checkbox_4 = ctk.CTkCheckBox(scroll_history, text='ружье')
    checkbox_4.select()

    checkbox_5 = ctk.CTkCheckBox(scroll_history, text='ружье')
    checkbox_5.select()

    checkbox_6 = ctk.CTkCheckBox(scroll_history, text='ружье')
    checkbox_6.deselect()

    checkbox_7 = ctk.CTkCheckBox(scroll_history, text='ружье')
    checkbox_7.select()

    return scroll_history.list_checkboxes.extend([checkbox_1, checkbox_2, checkbox_3, checkbox_4, checkbox_5, checkbox_6, checkbox_7])


@pytest.fixture
def fills_history_lists_products():
    """
    Заполняет список продуктами, подготавливая среду для тестирования
    """
    history.load_data_purchase_history['1'] = ['кочерга', 4, 'Инструменты']

    history.load_data_purchase_history['2'] = ['лопата', 7, 'Инструменты']

    history.load_data_purchase_history['3'] = ['савок', 14, 'Инструменты']

    history.load_data_purchase_history['4'] = ['ананас', 778, 'Инструменты']

    history.load_data_purchase_history['5'] = ['ведро', 499, 'Инструменты']



#================================================================ ScrollPurchaseHistory ======================================================================

@pytest.mark.SPH_list_select_checkboxes
def test_create_list_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции фильтрации чекбоксов и создания списка активных чекбоксов, а так же тип элементов списка
    """
    result = scroll_history.create_list_select_checkboxes()

    for i in result:
        assert type(i) == ctk.CTkCheckBox

    assert len(result) == 4


@pytest.mark.SPH_list_text_select_checkboxes
def test_create_list_text_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции фильтрации чекбоксов и создания списка текстов активных чекбоксов, а так же тип элементов списка
    """
    result = scroll_history.create_list_text_select_checkbox()

    for i in result:
        assert type(i) == str

    assert len(result) == 4


@pytest.mark.SPH_delete_checkbox
def test_delete_checkbox():
    """
    Проверяет удаление чекбокса из скролл фрейма и проверяет, что чекбокс удален из списка
    """

    assert scroll_history.count_checkboxes == 7

    scroll_history.delete_checkbox()

    assert scroll_history.count_checkboxes == 3


@pytest.mark.SPH_get_select_checkboxes
def test_get_select_checkboxes():
    """
    Проверяет работу функции получения чекбоксов и возвращения текста активных чекбоксов или вернет (None, None)
    """
    for i in scroll_history.list_checkboxes:
        i.select()

    text, elem = scroll_history.get_selected_checkbox()

    assert text == 'скакалка'

    assert elem == scroll_history.list_checkboxes[0]

    for i in scroll_history.list_checkboxes:
        i.deselect()

    assert scroll_history.get_selected_checkbox() == (None, None)


@pytest.mark.SPH_check_select_checkboxes
def test_check_select_checkboxes():
    """
    Проверяет работу функции проверки чекбоксов и создания списка активных чекбоксов, а так же проверяет, что чекбоксы отмечены
    """
    for i in scroll_history.list_checkboxes:
        i.select()

    assert scroll_history.check_selected_checkbox() is True

    scroll_history.reset_checkboxes()

    assert scroll_history.check_selected_checkbox() is False


@pytest.mark.SPH_reset_checkboxes
def test_reset_checkboxes():
    """
    Проверяет работу функции сброса чекбоксов и проверяет, что чекбоксы сняты с выбора
    """
    for i in scroll_history.list_checkboxes:
        i.select()

    assert scroll_history.check_selected_checkbox() is True

    scroll_history.reset_checkboxes()

    assert scroll_history.check_selected_checkbox() is False


@pytest.mark.SPH_clear_scroll_frame
def test_clear_scroll_frame():
    """
    Проверяет работу функции очистки скролл фрейма и проверяет, что чекбоксы удалены из списка
    """
    assert scroll_history.count_checkboxes == 3

    scroll_history.clear_scroll_frame()

    assert scroll_history.count_checkboxes == 0


@pytest.mark.SPH_count_checkboxes
def test_get_count_checkboxes():
    """
    Проверяет работу функции получения количества чекбоксов и проверяет, что оно верно считает чекбоксы
    """
    assert scroll_history.count_checkboxes == 0


@pytest.mark.SPH_get_list_checkboxes
def test_get_list_checkboxes():
    """
    Проверяет возвращаемое значение
    """
    assert type(scroll_history.list_checkboxes) == list


# ======================================================================PurchaseHistory ======================================================================

@pytest.mark.PH_del_target_condition
def test_del_target_condition():
    """
    Проверяет удаление продукта из списка с условием
    """

    scroll_history.list_checkboxes.append(ctk.CTkCheckBox(scroll_history, text='ружье'))

    select_checkbox = scroll_history.list_checkboxes[0]
    select_checkbox.select()

    assert history.del_target_condition() is None

    assert select_checkbox not in history.load_data_purchase_history


@pytest.mark.PH_cancel_button
def test_cancel_button_click_handler():
    """
    Проверяет обработку кнопки отмены
    """
    assert history.cancel_button_click_handler() == history.destroy()


@pytest.mark.PH_get_load_data_purchase_history
def test_get_load_data_purchase_history():
    """
    Проверяет получение загруженных продуктов из истории
    """
    assert type(history.load_data_purchase_history) == dict


@pytest.mark.PH_get_load_data
def test_get_load_data():
    """
    Проверяет возвращаемое значение
    """

    assert type(history.load_data) is dict