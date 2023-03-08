from selenium import webdriver
from selenium.webdriver.common.by import By
from book_store_testing.Locators import Locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoggedPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.element_presence_check_locator = Locator.element_presence_check
        self.wait = WebDriverWait(driver, 10)
        self.shop_btn = driver.find_element(*Locator.shop_btn)


    def checkPresenceOfElement(self):
       self.wait.until(
            EC.presence_of_element_located(self.element_presence_check_locator)
        )

    def go_to_shop(self):
        self.shop_btn.click()

