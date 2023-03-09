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
