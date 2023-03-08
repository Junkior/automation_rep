import time

from selenium import webdriver
from book_store_testing.PageObjectPages.ShopPagePO import ShopPage
from book_store_testing.PageObjectPages.StartPagePO import StartPage
from book_store_testing.PageObjectPages.RegScreenPO import RegScreen
from book_store_testing.PageObjectPages.LoggedScreenPO import LoggedPage
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

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

driver.quit()