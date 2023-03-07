from book_store_testing.Locators import Locator
from selenium.webdriver.common.by import By
from selenium import webdriver

class RubyBookPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.review_tab_btn = driver.find_element(*Locator.review_tab_btn)
        self.five_stars_button = driver.find_element(*Locator.five_stars_button)
        self.review_field = driver.find_element(*Locator.review_field)
        self.name_field = driver.find_element(*Locator.name_field)
        self.email_field = driver.find_element(*Locator.email_field)
        self.submit_btn = driver.find_element(*Locator.submit_btn)

    def clickReviewsButton(self):
        self.review_tab_btn.click()

    def setFiveStars(self):
        self.five_stars_button.click()

    def setReview(self, review_text):
        self.review_field.send_keys(review_text)

    def setName(self, name):
        self.name_field.send_keys(name)

    def setEmail(self, email):
        self.email_field.send_keys(email)

    def clickSubmitButton(self):
        self.submit_btn.click()






