import time

from selenium import webdriver
from book_store_testing.PageObjectPages.ShopPagePO import ShopPage
from book_store_testing.PageObjectPages.StartPagePO import StartPage
from book_store_testing.PageObjectPages.RegScreenPO import RegScreen
from book_store_testing.PageObjectPages.LoggedScreenPO import LoggedPage
from book_store_testing.PageObjectPages.AndroidQuickStartBookPO import AndroidQuickBook
from book_store_testing.DriverSettings import DriverSet
from book_store_testing.PageObjectPages.CartPagePO import CartPage


driver = DriverSet.browser()
###
# Открыть http://practice.automationtesting.in/
start_page = StartPage(driver)
start_page.goToMyAccount()
# Залогиниться
reg_page = RegScreen(driver)
reg_page.setEmailLoginField("oxample_test@gmail.com")
reg_page.setPasswordLoginField("_6Words_!")
reg_page.clickLoginButton()
# Нажать на вкладку "Shop"
logged_page = LoggedPage(driver)
logged_page.go_to_shop()
#  Добавить тест, что в селекторе выбран вариант сортировки по умолчанию
shop_page = ShopPage(driver)
shop_page.checkDefaultSelectorOption()
# Отсортировать товары по цене от большей к меньшей
shop_page.sortByDescending()
# Добавить тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
shop_page = ShopPage(driver)
shop_page.checkDescendingSort()
###
driver.quit()
###
driver = DriverSet.browser()
### Отображение, скидка товара

# Открыть http://practice.automationtesting.in/
start_page = StartPage(driver)
# Залогиниться
start_page.goToMyAccount()
reg_page = RegScreen(driver)
reg_page.login_to_account()
# Нажать на вкладку "Shop"
logged_page = LoggedPage(driver)
logged_page.go_to_shop()
# Открыть книгу "Android Quick Start Guide"
shop_page = ShopPage(driver)
shop_page.openAndroidQuickStartBook()
# Добавить тест, что содержимое старой цены = "₹600.00"
android_quick_start_page = AndroidQuickBook(driver)
android_quick_start_page.check_old_price()
# Добавить тест, что содержимое новой цены = "₹450.00"
android_quick_start_page.check_new_price()
# Нажать на обложку книги
android_quick_start_page.click_on_book_cover()
# Закрыть предпросмотр
android_quick_start_page.wait_close_btn()
android_quick_start_page.close_preview_book_cover()
###
driver.quit()
###
driver = DriverSet.browser()
### Проверка цены в корзине
# Открыть http://practice.automationtesting.in/
start_page = StartPage(driver)
# Нажать на вкладку "Shop"
start_page.go_to_shop()
# Добавить в корзину книгу которая есть в наличии
shop_page = ShopPage(driver)
shop_page.add_js_book_to_cart()
#
driver.refresh()
#
shop_page = ShopPage(driver)
# Проверить что количество товаров в корзине = 1
shop_page.check_cart_items_amount(1)
# Проверить что сумма товаров в корзине равна 350.00
shop_page.check_cart_items_sum("350.00")
# Открыть корзину
shop_page.go_to_cart()
# Проверить что цена в subtotal равна 350.00
cart_page = CartPage(driver)
cart_page.check_subtotal_price("350.00")
# Проверить что цена в total равна 357.00
cart_page.check_total_price("357.00")
###
driver.quit()