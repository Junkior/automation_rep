from book_store_testing.Locators import Locator
from selenium.webdriver.common.by import By
from selenium import webdriver
class StartPage(object):
    def __init__(self, driver):
        self.driver = driver

        self.startpage_url = driver.get("http://practice.automationtesting.in/")
        self.read_more_btn = driver.find_element(*Locator.read_more_btn)
        self.my_account_btn = driver.find_element(*Locator.my_account_btn)
        self.shop_btn = driver.find_element(*Locator.shop_btn)

    def clickReadMoreButton(self):
        self.read_more_btn.click()


    def goToStartPage(self):
        self.startpage_url

    def goToMyAccount(self):
        self.my_account_btn.click()

    def go_to_shop(self):
        self.shop_btn.click()
