from pages.base_page import BasePage
from locators.order_list_page_locators import OrderListPageLocators
import allure
from urls import Urls


class OrderListPage(BasePage):

    @allure.step("вывод деталей заказа")
    def click_order_card(self):
        order_card = self.wait_and_find_element(OrderListPageLocators.ORDER_CARD)
        self.click_element(order_card)


    @allure.step("Вывод номера последнего заказа")
    def get_order_number(self):
        element = self.wait_and_find_element(OrderListPageLocators.ORDER_NUMBER_IN_HISTORY)
        return element.text

    @allure.step("Вывод счётчика заказа в ленте заказов")
    def get_orders_counter(self):
        number = self.wait_and_find_element(OrderListPageLocators.ORDER_COUNTER)
        return int(number.text)

    @allure.step("Клик 'Конструктор' в заголовке")
    def click_constructor_button(self):
        constructor_button = self.wait_and_find_element(OrderListPageLocators.CONSTRUCTOR_BTN)
        self.click_element(constructor_button)

    @allure.step("Вывод счётчика за сегодня в ленте заказов")
    def get_orders_counter_today(self):
        number = self.wait_and_find_element(OrderListPageLocators.ORDER_COUNTER_TODAY)
        return int(number.text)

    @allure.step("Вывод номера заказа в 'В работе' в ленте заказов")
    def get_order_in_works_number(self):
        number_in_works = self.wait_and_find_element(OrderListPageLocators.ORDER_IN_WORK)
        return int(number_in_works.text)

    @allure.step("Вывод окна деталями заказа")
    def check_open_window_with_order_details(self):
        return self.is_element_present(OrderListPageLocators.INGREDIENT_IN_ORDER)

    @allure.step("Сравнить URL")
    def check_main_page_url(self):
        return self.driver.current_url == Urls.BASE_URL
