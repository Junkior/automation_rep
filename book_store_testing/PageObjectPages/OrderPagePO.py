from selenium import webdriver
from book_store_testing.Locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class OrderPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.first_name = driver.find_element(*Locator.first_name)
        self.last_name = driver.find_element(*Locator.last_name)
        self.order_email_field = driver.find_element(*Locator.order_email_field)
        self.phone = driver.find_element(*Locator.phone)
        self.country_selector = driver.find_element(*Locator.country_selector)
        self.country_selector_search_field = driver.find_element(*Locator.country_selector_search_field)
        self.address = driver.find_element(*Locator.address)
        self.city = driver.find_element(*Locator.city)
        self.state = driver.find_element(*Locator.state)
        self.zip_code = driver.find_element(*Locator.zip_code)
        self.check_payments_radiobtn = driver.find_element(*Locator.check_payments_radio)
        self.place_order_btn = driver.find_element(*Locator.place_order_btn)
        self.success_order_message = Locator.success_order_message
        self.payment_method = Locator.payment_method

    def wait_first_name_presence(self):
        self.wait.until(
            EC.presence_of_element_located(Locator.first_name)
        )

    def set_first_name_field(self, name_text="Mike"):
        self.first_name.send_keys(name_text)

    def set_last_name_field(self, last_name_text="Portnoy"):
        self.last_name.send_keys(last_name_text)

    def set_email_field(self, email_field_text="oxample@gmail.com"):
        self.order_email_field.send_keys(email_field_text)

    def set_phone_field(self, phone_number="9006665531"):
        self.phone.send_keys(phone_number)

    def set_country(self, country_name="Armenia"):
        self.country_selector.click()
        self.country_selector_search_field.send_keys(country_name)
        self.country_selector_search_field.send_keys(Keys.ENTER)

    def set_address(self, address_text="Fake adress"):
        self.address.send_keys(address_text)

    def set_city(self, city_name="Lars"):
        self.city.send_keys(city_name)

    def set_state(self, state_name="Fake state"):
        self.state.send_keys(state_name)

    def set_zipcode(self, zip_code_text="123456"):
        self.zip_code.send_keys(zip_code_text)

    def scroll_by(self, horizontal=0, vertical=600):
        self.driver.execute_script(f"window.scrollBy({horizontal}, {vertical});")

    def set_payment_to_check_payments(self):
        self.check_payments_radiobtn.click()

    def click_place_order(self):
        self.place_order_btn.click()

    def check_success_order_message(self, order_message="Thank you. Your order has been received." ):
        self.wait.until(
            EC.text_to_be_present_in_element(self.success_order_message, order_message)
        )

    def check_payment_methode_check_payments(self):
        self.wait.until(
            EC.text_to_be_present_in_element(self.payment_method, "Check Payments")
        )
