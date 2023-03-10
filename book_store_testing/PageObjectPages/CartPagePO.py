from selenium import webdriver
from book_store_testing.Locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.subtotal_price_element = Locator.subtotal_price_element
        self.total_price_element = Locator.total_price_element
        self.remove_book_btn = driver.find_element(*Locator.remove_book_btn)
        self.undo_btn = Locator.undo_btn
        self.quantity_field = driver.find_element(*Locator.quantity_field)
        self.apply_coupon_btn = driver.find_element(*Locator.apply_coupon_btn)
        self.coupon_message_error = Locator.coupon_msg_error
        self.checkout_btn = driver.find_element(*Locator.checkout_btn)
        self.update_cart_btn = driver.find_element(*Locator.update_basket_btn)

    """Проверяет что сумма в субтотал равна сумме указанной в sub_price, сумму указывать с .00"""

    def check_subtotal_price(self, sub_price):
        self.wait.until(
            EC.text_to_be_present_in_element(self.subtotal_price_element, f"₹{sub_price}")
        )

    """Проверяет что сумма в тотал равна сумме указанной в tot_price, сумму указывать с .00"""

    def check_total_price(self, tot_price):
        self.wait.until(
            EC.text_to_be_present_in_element(self.total_price_element, f"₹{tot_price}")
        )

    def remove_book_from_cart(self):
        self.remove_book_btn.click()

    def wait_undo_button_appearance(self):
        self.wait.until(
            EC.presence_of_element_located(self.undo_btn)
        )

    def click_undo_btn(self):
        self.driver.find_element(*self.undo_btn).click()

    """Очищает поле quantity и вписывает количество переданное в параметр quantity_amount"""

    def set_quantity_field_amount(self, quantity_amount):
        self.quantity_field.clear()
        self.quantity_field.send_keys(quantity_amount)

    def update_cart(self):
        self.update_cart_btn.click()

    """Сравнивает количество товаров взятых из значения value со значением переданным в параметр check_amount"""

    def check_quantity_field_amount(self, check_amount):
        assert self.quantity_field.get_attribute("value") == check_amount

    def click_apply_coupon(self):
        self.apply_coupon_btn.click()

    """Сверяет текст ошибки с текстом ошибки переданным в error_text(есть значение по умолчанию)"""

    def check_coupon_message_error(self, error_text="Please enter a coupon code."):
        assert self.driver.find_element(*self.coupon_message_error).text == error_text

