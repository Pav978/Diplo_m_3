from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
from pages.base_page import BasePage
from urls import Urls
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
    @allure.step("Открываем 'Stellar Burger'")
    def open(self):
        self.open_page(Urls.BASE_URL)

    @allure.step("CLick 'Лента заказов' в загловке")
    def click_list_order_button(self):
        list_order_button = self.wait_and_find_element(MainPageLocators.LIST_ORDER_BTN)
        self.click_element(list_order_button)


    @allure.step("Click 'Ингредиенту'")
    def click_ingredient_button(self):
        ingredients_list = self.wait_and_find_element(MainPageLocators.INGREDIENT_LIST)
        ingredients = ingredients_list.find_elements(*MainPageLocators.INGREDIENT_ITEM)
        second_ingredient = ingredients[1]
        self.click_element(second_ingredient)

    @allure.step("Click по кнопке закрытия всплывающего окна")
    def close_ingredient_card(self):
        x_button = self.wait_and_find_element(MainPageLocators.X_BUTTON)
        self.click_element(x_button)

    @allure.step("Перетащить элемент(хлеб) в блюдо")
    def add_bun_in_order(self):
        source = self.wait_and_find_element(MainPageLocators.BUN_INGREDIENT)
        target = self.wait_and_find_element(MainPageLocators.BURGER_ORDER)
        drag_and_drop(self.driver, source, target)

    @allure.step("Перетащить элемент(соус) в блюдо")
    def add_sauce_in_order(self):
        source = self.wait_and_find_element(MainPageLocators.SAUCE_INGREDIENT)
        target = self.wait_and_find_element(MainPageLocators.BURGER_ORDER)
        drag_and_drop(self.driver, source, target)

    @allure.step("Перетащить элемент(мясо) в блюдо")
    def add_meat_in_order(self):
        source = self.wait_and_find_element(MainPageLocators.MEAT_INGREDIENT)
        target = self.wait_and_find_element(MainPageLocators.BURGER_ORDER)
        drag_and_drop(self.driver, source, target)

    @allure.step("Кликн 'Оформить заказ'")
    def click_create_order_button(self):
        account_button = self.wait_and_find_element(MainPageLocators.CREATE_ORDER_BTN)
        self.click_element(account_button)

    @allure.step("проверить работу счётчика")
    def get_count_ingredient(self):
        counter_element = self.wait_and_find_element(MainPageLocators.COUNTER)
        return counter_element.text

    @allure.step("генерируем почту для авторизации")
    def get_user_email(self, user_response):
        email = user_response["email"]
        return email

    @allure.step("генерируем пароль для авторизации")
    def get_user_password(self, user_response):
        password = user_response["password"]
        return password

    @allure.step("Клик 'Личный кабинет'")
    def click_account_button(self):
        account_button = self.wait_and_find_element(MainPageLocators.BUTTON_ACCOUNT)
        self.click_element(account_button)


    @allure.step("Клик кнопки закрытия всплывающего окна")
    def click_order_card_x_button(self):
        x_button = self.wait_and_find_element(MainPageLocators.CLOSE_WINDOW_BTN)
        self.click_element(x_button)


    @allure.step("Получить номер оформленного заказа")
    def get_new_order_number(self):
        WebDriverWait(self.driver, 10).until(lambda driver: self.wait_and_find_element(MainPageLocators.NUMBER_NEW_ORDER).text != '9999')
        new_order_number_element = self.wait_and_find_element(MainPageLocators.NUMBER_NEW_ORDER)
        new_order_number = new_order_number_element.text
        return int(new_order_number)

    @allure.step("Проверить вывод информации об ингредиенте")
    def check_ingredient_title(self):
        if self.is_element_present(MainPageLocators.INGREDIENT_TITLE) == True:
            return True

    @allure.step("Проверить скрытие информации об ингредиенте")
    def check_main_page_title(self):
        if self.is_element_present(MainPageLocators.TITLE_MAIN_PAGE) == True:
            return True

    @allure.step("Ожидание открытия страницы")
    def find_main_page_title(self):
        return self.wait_and_find_element(MainPageLocators.TITLE_MAIN_PAGE)

    @allure.step("Ожидание открытия деталей заказа")
    def find_create_order_description(self):
        return self.wait_and_find_element(MainPageLocators.CREATE_ORDER_DESCRIPTION)


    @allure.step("Сравнить'")
    def check_order_list_url(self):
        return self.driver.current_url == (Urls.BASE_URL + Urls.LIST_ORDER_PAGE)