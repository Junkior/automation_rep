from selenium import webdriver
from book_store_testing.Locators import Locator
from selenium.webdriver.common.by import By

class RegScreen(object):
    def __init__(self, driver):
        self.driver = driver
        self.email_field_registration = driver.find_element(By.ID, Locator.email_field_registration)
        self.password_field_registration = driver.find_element(By.ID, Locator.password_field_registration)
        self.registration_btn = driver.find_element(By.NAME, Locator.registration_btn)
        self.login_email_field = driver.find_element(By.ID, Locator.login_email_field)
        self.login_password_field = driver.find_element(By.ID, Locator.login_password_field)
        self.login_btn = driver.find_element(By.NAME, Locator.login_btn)
        self.shop_btn = driver.find_element(*Locator.shop_btn)


    def setEmailRegistrationField(self, email_registration):
        self.email_field_registration.send_keys(email_registration)

    def setPasswordRegistrationField(self, password_registration):
        self.password_field_registration.send_keys(password_registration)

    def clickRegistrationButton(self):
        self.registration_btn.click()

    def setEmailLoginField(self, email_login):
        self.login_email_field.send_keys(email_login)

    def setPasswordLoginField(self, password_login):
        self.login_password_field.send_keys(password_login)

    def clickLoginButton(self):
        self.login_btn.click()

    def clickShopButton(self):
        self.shop_btn.click()




