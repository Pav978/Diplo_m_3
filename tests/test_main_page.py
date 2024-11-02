import burger_api
from pages.main_page import MainPage
from pages.order_page import OrderListPage
from pages.personal_account_page import PersonalAccountPage
import allure
from conftest import *


class TestMainPage:
    @allure.title("Проверка клика кнопки 'Конструктор'")
    @allure.description("Проверка перехода по кнопке 'Конструктор'")
    def test_click_button_constructor_open_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        order_list_page = OrderListPage(driver)
        main_page.click_list_order_button()
        order_list_page.click_constructor_button()
        current_url = order_list_page.check_main_page_url()
        assert current_url == True


    @allure.title("Проверка перехода по клику по  'Лента заказов'")
    @allure.description("Проверка успешного перехода из заголовка сайта по кнопке 'Лента заказов'")
    def test_click_button_list_order(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_list_order_button()
        current_url = main_page.check_order_list_url()
        assert current_url == True

    @allure.title("Проверка вывода деталей всплывающим окном")
    @allure.description("Проверка открытия всплывающего окна с деталями")
    def test_open_window_ing(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient_button()
        assert main_page.check_ingredient_title() == True

    @allure.title("Проверка закрытия окна с деталями")
    @allure.description("Проверка закрытия с помощью иконки (Х) всплывающего окна с деталями")
    def test_close_ing(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient_button()
        main_page.close_ingredient_card()
        assert main_page.check_main_page_title() == True

    @allure.title("Проверка работы счетчика при добавлении ингредиента")
    @allure.description("Проверка счётчика ингредиента при добавлении в конструктор бургера")
    def test_counter_add_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        count_before = main_page.get_count_ingredient()
        main_page.add_bun_in_order()
        count_after = main_page.get_count_ingredient()
        assert count_before == '0' and count_after == '2'

    @allure.title("Проверка оформления заказа авторизованным пользователем")
    @allure.description("Заказ оформлен ")
    def test_create_order_authorized_user(self, driver):
        user_data = burger_api.create_user_body()
        user_response = burger_api.create_user(user_data)
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.set_email(email)
        personal_account_page.set_password(password)
        personal_account_page.click_enter_button()
        main_page.find_main_page_title()
        main_page.add_bun_in_order()
        main_page.add_sauce_in_order()
        main_page.add_meat_in_order()
        main_page.click_create_order_button()
        description_create_order = main_page.find_create_order_description()
        access_token = burger_api.get_access_token(user_response)
        burger_api.delete_user(access_token)
        assert description_create_order.text == "Ваш заказ начали готовить"

