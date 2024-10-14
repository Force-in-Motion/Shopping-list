import pytest
import customtkinter as ctk

from src.create.create_list import ScrollCreateList, CreateList, ConfigCreateList
from src.start.main_page import MainPage


start_window = MainPage()

create_list = CreateList(start_window)

scroll_create_list = ScrollCreateList(create_list, create_list)

config_create_list = ConfigCreateList(create_list, create_list)

checkbox = ctk.CTkCheckBox(scroll_create_list)



@pytest.fixture(scope='session')
def fills_list_checkboxes():
    """
    Заполняет список чекбоксами, подготавливая среду для тестирования
    """
    checkbox_1 = ctk.CTkCheckBox(scroll_create_list, text='кочерга, 4, Инструменты')
    checkbox_1.select()

    checkbox_2 = ctk.CTkCheckBox(scroll_create_list, text='скакалка, 4, Спорт. Товары')
    checkbox_2.deselect()

    checkbox_3 = ctk.CTkCheckBox(scroll_create_list, text='леска, 4, Рыбалка')
    checkbox_3.deselect()

    checkbox_4 = ctk.CTkCheckBox(scroll_create_list, text='ружье, 4, Охота')
    checkbox_4.select()

    checkbox_5 = ctk.CTkCheckBox(scroll_create_list, text='ружье, 4, Охота')
    checkbox_5.select()

    checkbox_6 = ctk.CTkCheckBox(scroll_create_list, text='ружье, 4, Охота')
    checkbox_6.deselect()

    checkbox_7 = ctk.CTkCheckBox(scroll_create_list, text='ружье, 4, Охота')
    checkbox_7.select()

    return scroll_create_list.list_checkboxes.extend([checkbox_1, checkbox_2, checkbox_3, checkbox_4, checkbox_5, checkbox_6, checkbox_7])



@pytest.fixture
def fills_config_data_products():
    create_list.data_create_list.name_product.insert(0, 'Cherry')

    create_list.data_create_list.count_product.insert(0, '5')

    create_list.data_create_list.category.set('Рыбалка')

    expected_product = ['Cherry', '5', 'Рыбалка']

    return expected_product


#================================================================ ScrollCreateList ======================================================================

data_test_scl_create_checkbox = [( 'ананас', 4, 'Продукты питания', None),
                                 ( 'кочерга', 4, 'Инструменты', None),
                                 ( 'скакалка', 4, 'Спорт. Товары', None),
                                 ( 'леска', 4, 'Рыбалка', None),
                                 ( 'ружье', 4, 'Охота', None)]

@pytest.mark.SCL_create_checkbox
@pytest.mark.parametrize('val1, val2, val3, expect_result', data_test_scl_create_checkbox)
def test_create_checkbox(val1, val2, val3, expect_result):
    """
    Проверяет создание нового чекбокса в скролле фрейма и проверяет, что чекбокс добавлен в список
    """
    count_checkboxes_in_list = len(scroll_create_list.list_checkboxes)

    assert scroll_create_list.create_checkbox(val1, val2, val3) is None

    assert len(scroll_create_list.list_checkboxes) == count_checkboxes_in_list + 1



data_test_scl_set_new_text_for_checkbox = [(checkbox, 'ананас, 4, Продукты питания', None),
                                           (checkbox, 'кочерга, 9, Инструменты', None),
                                           (checkbox, 'скакалка, 48, Спорт. Товары', None),
                                           (checkbox, 'леска, 14, Рыбалка', None),
                                           (checkbox, 'ружье, 25, Охота', None),]

@pytest.mark.SCL_set_text_checkbox
@pytest.mark.parametrize('val1, val2, expect_result', data_test_scl_set_new_text_for_checkbox)
def test_set_new_text_for_checkbox(val1, val2, expect_result):
    """
    Проверяет установку нового текста для чекбокса и проверяет, что текст изменился
    """
    old_text_checkbox = val1.cget("text")

    assert scroll_create_list.set_new_text_for_checkbox(val1, val2) is None

    assert val1.cget("text")!= old_text_checkbox


@pytest.mark.SCL_list_select_checkboxes
def test_create_list_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции фильтрации чекбоксов и создания списка активных чекбоксов, а так же тип элементов списка
    """
    result = scroll_create_list.create_list_select_checkboxes()

    for i in result:
        assert type(i) == ctk.CTkCheckBox

    assert len(result) == 4


@pytest.mark.SCL_list_text_select_checkboxes
def test_create_list_text_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции фильтрации чекбоксов и создания списка текстов активных чекбоксов, а так же тип элементов списка
    """
    result = scroll_create_list.create_list_text_select_checkbox()

    for i in result:
        assert type(i) == str

    assert len(result) == 4


@pytest.mark.SCL_delete_checkbox
def test_delete_checkbox(fills_list_checkboxes):
    """
    Проверяет удаление чекбокса из скролл фрейма и проверяет, что чекбокс удален из списка
    """
    initial_count = scroll_create_list.count_checkboxes

    assert initial_count == 12

    scroll_create_list.delete_checkbox()

    current_count = scroll_create_list.count_checkboxes

    assert current_count == 8


@pytest.mark.SCL_check_select_checkboxes
def test_check_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции проверки чекбоксов и создания списка активных чекбоксов, а так же проверяет, что чекбоксы отмечены
    """
    for i in scroll_create_list.list_checkboxes:
        i.select()

    assert scroll_create_list.check_selected_checkbox() is True

    scroll_create_list.reset_checkboxes()

    assert scroll_create_list.check_selected_checkbox() is False


@pytest.mark.SCL_get_select_checkboxes
def test_get_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции получения чекбоксов и возвращения текста активных чекбоксов или вернет (None, None)
    """
    for i in scroll_create_list.list_checkboxes:
        i.select()

    text, elem = scroll_create_list.get_selected_checkbox()

    assert text == 'ананас, 4, Продукты питания'

    assert elem == scroll_create_list.list_checkboxes[0]

    for i in scroll_create_list.list_checkboxes:
        i.deselect()

    assert scroll_create_list.get_selected_checkbox() == (None, None)


@pytest.mark.SCL_reset_checkboxes
def test_reset_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции сброса чекбоксов и проверяет, что чекбоксы сняты с выбора
    """
    for i in scroll_create_list.list_checkboxes:
        i.select()

    assert scroll_create_list.check_selected_checkbox() is True

    scroll_create_list.reset_checkboxes()

    assert scroll_create_list.check_selected_checkbox() is False


@pytest.mark.SCL_count_checkboxes
def test_get_count_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции получения количества чекбоксов и проверяет, что оно верно считает чекбоксы
    """
    assert scroll_create_list.count_checkboxes == 8


# ================================================= CreateList ====================================================================================

@pytest.mark.CL_add_product_in_list
def test_add_product_in_list(fills_config_data_products):
    """
    Проверяет создание нового продукта в списке и проверяет, что продукт добавлен в список
    """
    assert create_list.add_product_button_click_handler() is None

    assert fills_config_data_products in create_list.list_products


@pytest.mark.CL_add_category_click_handler
def test_add_category_click_handler():
    """
    Проверяет создание новой категории в списке и проверяет, что категория добавлена в список
    """
    assert create_list.add_category_button_click_handler() is None


data_test_update_load_data_positive = [('Cherry, 5, Рыбалка',  'Карась, 5999999999999999999999999999999999, Рыбалка')]

@pytest.mark.parametrize('val1, val2', data_test_update_load_data_positive)
def test_update_load_data_with_params(val1, val2):
    """
    Проверяет работу функции замены старого текста на новый с параметрами
    """
    assert create_list.update_load_data(val1, val2) is True


@pytest.mark.CL_del_button_click_handler
def test_del_button_click_handler():
    """
    Проверяет удаление продукта из списка
    """
    assert create_list.del_button_click_handler() is None


@pytest.mark.CL_del_target_condition
def test_del_target_condition():
    """
    Проверяет удаление продукта из списка с условием
    """
    select_checkbox = scroll_create_list.list_checkboxes[0]
    select_checkbox.select()

    create_list.del_target_condition()

    assert select_checkbox not in create_list.list_products


@pytest.mark.CL_cancel_button_click_handler
def test_cancel_button_click_handler():
    """
    Проверяет работу метода возврата к главному окну и закрытия текущего
    """
    assert create_list.cancel_button_click_handler() == create_list.destroy()


@pytest.mark.CL_get_scroll_frame
def test_get_scroll_frame():
    """
    Проверяет тип получаемого значения
    """
    assert type(create_list.scroll_create_list) == ScrollCreateList


@pytest.mark.CL_get_list_products
def test_get_list_products():
    """
    Проверяет тип получаемого значения
    """
    assert type(create_list.list_products) == list


@pytest.mark.CL_get_data_create_list
def test_get_data_create_list():
    """
    Проверяет тип получаемого значения
    """
    assert type(create_list.data_create_list) == ConfigCreateList