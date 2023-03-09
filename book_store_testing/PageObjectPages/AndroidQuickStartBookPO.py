from selenium import webdriver
from selenium.webdriver.common.by import By
from book_store_testing.Locators import Locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AndroidQuickBook(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.old_price = driver.find_element(*Locator.old_price)
        self.new_price = driver.find_element(*Locator.new_price)
        self.book_cover = driver.find_element(*Locator.book_cover)


    def check_old_price(self):
        old_price_text = self.old_price.text
        if '₹' in old_price_text:
            old_price_text = old_price_text[1:]
        assert old_price_text == "600.00"

    def check_new_price(self):
        new_price_text = self.new_price.text
        if '₹' in new_price_text:
            new_price_text = new_price_text[1:]
        assert new_price_text == "450.00"

    def click_on_book_cover(self):
        self.book_cover.click()

    def wait_close_btn(self):
        self.wait.until(
            EC.presence_of_element_located(Locator.close_btn_locator)
        )

    def close_preview_book_cover(self):
        self.driver.find_element(*Locator.close_btn_locator).click()

