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
        self.price_desc_option = driver.find_element(*Locator.price_desc_option)
        self.js_book_add_to_cart = driver.find_element(*Locator.js_book_add_to_cart)
        self.items_cart = driver.find_element(*Locator.items_cart)
        self.cart_price = driver.find_element(*Locator.cart_price)
        self.cart_btn = driver.find_element(*Locator.cart_btn)

    def openHtml5Book(self):
        self.html5_book_btn.click()

    def setCategoryToHtml(self):
        self.html_category_btn.click()

    def checkNumberOfProducts(self):
        assert len(self.products_list_locator) == 3

    def checkDefaultSelectorOption(self):
        assert self.shop_page_default_option_locator.get_attribute("selected") is not None
        print("Выбран метод сортировки по умолчанию")

    def sortByDescending(self):
        Select(self.shop_page_filter_selector).select_by_value("price-desc")

    def checkDescendingSort(self):
        assert self.price_desc_option.get_attribute("selected") is not None
        print("Выбран метод сортировки по убыванию цены")
    def openAndroidQuickStartBook(self):
        self.android_quick_guide_book_locator.click()

    def add_js_book_to_cart(self):
        self.js_book_add_to_cart.click()


    """Сравнивает количество товаров в корзине с количеством указанным в amount"""
    def check_cart_items_amount(self, amount):
            assert self.items_cart.text == f"{amount} Item" ##НЕ ЗАБУДЬ ДОБАВИТЬ ITEM->ITEMS


    """Сравнивает сумму товаров в корзине с суммой указанной в items_sum, сумму указывать с .00"""
    def check_cart_items_sum(self, items_sum):
        cart_items_sum_text = self.cart_price.text
        if '₹' in cart_items_sum_text:
            cart_items_sum_text = cart_items_sum_text[1:]
        assert cart_items_sum_text == items_sum

    def go_to_cart(self):
        self.cart_btn.click()
