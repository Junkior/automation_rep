import time

from selenium import webdriver
from book_store_testing.PageObjectPages.ShopPagePO import ShopPage
from book_store_testing.PageObjectPages.StartPagePO import StartPage
from book_store_testing.PageObjectPages.RegScreenPO import RegScreen
from book_store_testing.PageObjectPages.LoggedScreenPO import LoggedPage
from book_store_testing.PageObjectPages.AndroidQuickStartBookPO import AndroidQuickBook
from book_store_testing.DriverSettings import DriverSet
browser = DriverSet.browser()
###
# Открыть http://practice.automationtesting.in/
start_page = StartPage(browser)
start_page.goToMyAccount()
# Залогиниться
reg_page = RegScreen(browser)
reg_page.setEmailLoginField("oxample_test@gmail.com")
reg_page.setPasswordLoginField("_6Words_!")
reg_page.clickLoginButton()
# Нажать на вкладку "Shop"
logged_page = LoggedPage(browser)
logged_page.go_to_shop()
#  Добавить тест, что в селекторе выбран вариант сортировки по умолчанию
shop_page = ShopPage(browser)
shop_page.checkDefaultSelectorOption()
# Отсортировать товары по цене от большей к меньшей
shop_page.sortByDescending()
# Добавить тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
shop_page = ShopPage(browser)
shop_page.checkDescendingSort()
###
browser.quit()
###
browser = DriverSet.browser()
### Отображение, скидка товара

# Открыть http://practice.automationtesting.in/
start_page = StartPage(browser)
# Залогиниться
start_page.goToMyAccount()
reg_page = RegScreen(browser)
reg_page.login_to_account()
# Нажать на вкладку "Shop"
logged_page = LoggedPage(browser)
logged_page.go_to_shop()
# Открыть книгу "Android Quick Start Guide"
shop_page = ShopPage(browser)
shop_page.openAndroidQuickStartBook()
# Добавить тест, что содержимое старой цены = "₹600.00"
android_quick_start_page = AndroidQuickBook(browser)
android_quick_start_page.check_old_price()
# Добавить тест, что содержимое новой цены = "₹450.00"
android_quick_start_page.check_new_price()
# Нажать на обложку книги
android_quick_start_page.click_on_book_cover()
# Закрыть предпросмотр
android_quick_start_page.wait_close_btn()
android_quick_start_page.close_preview_book_cover()
###
browser.quit()
###
