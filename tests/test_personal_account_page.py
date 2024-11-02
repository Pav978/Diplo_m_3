from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
import allure
import burger_api
from conftest import *

class TestPersonalAccountPage:
    @allure.title("Проверка перехода в личный кабинет пользователя")
    @allure.description("Проверка перехода в 'Личный кабинет' по клику 'Личный кабинет'")
    def test_click_personal_account_success(self, driver):
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
        main_page.click_account_button()
        access_token = burger_api.get_access_token(user_response)
        burger_api.delete_user(access_token)
        assert personal_account_page.check_account_description()


    @allure.title("Проверка перехода в раздел 'История заказов'")
    @allure.description("Проверка перехода в 'История заказов' в личном кабинете")
    def test_click_history_orders(self, driver):
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
        main_page.click_account_button()
        personal_account_page.click_order_history_btn()
        access_token = burger_api.get_access_token(user_response)
        burger_api.delete_user(access_token)
        current_url = personal_account_page.check_order_history_page_url()
        assert current_url == True

    @allure.title("Проверка выхода из личного кабинета")
    @allure.description("Проверка выхода из ЛК по клику 'Выход'")
    def test_click_exit(self, driver):
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
        main_page.click_account_button()
        personal_account_page.click_exit_btn()
        personal_account_page.find_login_page_title()
        access_token = burger_api.get_access_token(user_response)
        burger_api.delete_user(access_token)
        current_url = personal_account_page.check_login_page_url()
        assert current_url == True