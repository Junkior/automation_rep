from selenium import webdriver
from book_store_testing.Locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class ShopPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.html5_book_btn = driver.find_element(*Locator.html5_book_btn)
        self.html_category_btn = driver.find_element(*Locator.html_category_btn)
        self.products_list_locator = driver.find_elements(*Locator.products_list_locator)
        self.shop_page_default_option_locator = driver.find_element(*Locator.shop_page_default_option_filter_locator)
        self.shop_page_filter_selector = driver.find_element(*Locator.shop_page_filter_selector)
        self.android_quick_guide_book_locator = driver.find_element(*Locator.android_quick_guide_book_locator)
        self.js_book_locator = driver.find_element(*Locator.js_book_locator)
        self.price_desc_option = driver.find_element(*Locator.price_desc_option)

    def openHtml5Book(self):
        self.html5_book_btn.click()

    def setCategoryToHtml(self):
        self.html_category_btn.click()

    def checkNumberOfProducts(self):
        assert len(self.products_list_locator) == 3

    def checkDefaultSelectorOption(self):
        option_default = self.shop_page_default_option_locator.get_attribute("selected")
        assert option_default is not None

    def sortByDescending(self):
        Select(self.shop_page_filter_selector).select_by_value("price-desc")

    def checkDescendingSort(self):
        desc_option = self.price_desc_option.get_attribute("selected")
        assert  desc_option is not None

    def openAndroidQuickStartBook(self):
        self.android_quick_guide_book_locator.click()

    def open_js_book(self):
        self.js_book_locator.click()
