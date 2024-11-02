from pages.base_page import BasePage
from locators.recovery_password_page_locators import RecoveryPassPageLocators
import allure

class RecoveryPasswordPage(BasePage):
    @allure.step("Ввод email")
    def set_email(self, email):
        input_email = self.wait_and_find_element(RecoveryPassPageLocators.FIELD_EMAIL)
        input_email.send_keys(email)

    @allure.step("Клик 'Восстановить'")
    def click_button_recovery(self):
        recovery_button = self.wait_and_find_element(RecoveryPassPageLocators.BUTTON_RECOVERY)
        self.click_element(recovery_button)

    @allure.step("Ввод нового пароля")
    def set_new_password(self, password):
        input_password = self.wait_and_find_element(RecoveryPassPageLocators.FIELD_NEW_PASSWORD)
        input_password.send_keys(password)

    @allure.step("Клик кнопки отображения скрытого пароля")
    def click_show_password_button(self):
        eye_button = self.wait_and_find_element(RecoveryPassPageLocators.EYE_BUTTON)
        self.click_element(eye_button)

    @allure.step('Ожидания вывода пароля')
    def get_password_input_state(self):
        input_password = self.wait_and_find_element(RecoveryPassPageLocators.FIELD_NEW_PASSWORD)
        return input_password.get_attribute("type") == "text"

    @allure.step("ОЖидание открытия экрана восстановления пароля")
    def check_recovery_page_title(self):
        if self.is_element_present(RecoveryPassPageLocators.RECOVER_TITLE) == True:
            return True

    @allure.step("Проверка открытия экрана восстановления пароля")
    def check_recovery_pass_title(self):
        if self.is_element_present(RecoveryPassPageLocators.RECOVER_TITLE) == True:
            return True