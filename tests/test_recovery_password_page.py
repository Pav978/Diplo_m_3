from pages.main_page import MainPage
from pages.recovery_password_page import RecoveryPasswordPage
from pages.personal_account_page import PersonalAccountPage
from data import UserData
import allure
from conftest import *

class TestRecoveryPassPage:

    @allure.title('Проверка перехода по "Восстановить пароль"')
    @allure.description("Проверка уперехода с главной страницы на страницу по клику 'Восстановить пароль'")
    def test_click_recovery_pass(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_recovery_button()
        recovery_page = RecoveryPasswordPage(driver)
        assert recovery_page.check_recovery_page_title()

    @allure.title("Проверка перехода по 'Восстановить'")
    @allure.description("Проверка клика по кнопке 'Восстановить'")
    def test_enter_data_click_recover(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_recovery_button()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.set_email(UserData.USER_EMAIL)
        recovery_page.click_button_recovery()
        assert recovery_page.check_recovery_pass_title()

    @allure.title("Проверка кнопки скрытия пароля ")
    @allure.description("Проверка клика на иконку скрытия пароля")
    def test_click_button_hiding_password(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_recovery_button()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.set_email(UserData.USER_EMAIL)
        recovery_page.click_button_recovery()
        recovery_page.set_new_password(UserData.NEW_PASSWORD)
        old_state = recovery_page.get_password_input_state()
        recovery_page.click_show_password_button()
        new_state = recovery_page.get_password_input_state()
        assert (old_state is False and new_state is True)
