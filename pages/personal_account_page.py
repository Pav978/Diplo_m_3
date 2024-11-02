from pages.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountLocators
import allure
from urls import Urls


class PersonalAccountPage(BasePage):
    @allure.step("Ввод email")
    def set_email(self, email):
        input_email = self.wait_and_find_element(PersonalAccountLocators.FIELD_EMAIL)
        input_email.send_keys(email)

    @allure.step("Ввод password")
    def set_password(self, password):
        input_password = self.wait_and_find_element(PersonalAccountLocators.FIELD_PASSWORD)
        input_password.send_keys(password)

    @allure.step("Click 'Войти'")
    def click_enter_button(self):
        enter_button = self.wait_and_find_element(PersonalAccountLocators.ENTER_BUTTON)
        self.click_element(enter_button)

    @allure.step("Клик 'История заказов' в Личном кабинете")
    def click_order_history_btn(self):
        order_history_btn = self.wait_and_find_element(PersonalAccountLocators.ORDER_HISTORY_BTN)
        self.click_element(order_history_btn)

    @allure.step("Клик 'Выход' в 'Личном Кабинете'")
    def click_exit_btn(self):
        exit_btn = self.wait_and_find_element(PersonalAccountLocators.EXIT_BTN)
        self.click_element(exit_btn)

    @allure.step("Вывод номера последнего заказа")
    def get_order_number(self):
        element = self.wait_and_find_element(PersonalAccountLocators.ORDER_NUMBER_IN_HISTORY)
        return element.text

    @allure.step("Клик 'Восстановить пароль'")
    def click_recovery_button(self):
        recovery_button = self.wait_and_find_element(PersonalAccountLocators.RECOVERY_BUTTON)
        self.click_element(recovery_button)

    @allure.step("Ожидание открытия личного кабинета")
    def check_account_description(self):
        if self.is_element_present(PersonalAccountLocators.DESCRIPTION_ACCOUNT) == True:
            return True

    @allure.step("Ожидания открытия окна авторизация")
    def find_login_page_title(self):
        if self.is_element_present(PersonalAccountLocators.TITLE_LOGIN_PAGE) == True:
            return True

    @allure.step("Сравнить URL страниц")
    def check_order_history_page_url(self):
        return self.driver.current_url == (Urls.BASE_URL + Urls.ORDER_HISTORY_URL)

    @allure.step("Сравнить URL тадресом страницы входа в аккаунт")
    def check_login_page_url(self):
        return self.driver.current_url == (Urls.BASE_URL + Urls.LOGIN_URL)