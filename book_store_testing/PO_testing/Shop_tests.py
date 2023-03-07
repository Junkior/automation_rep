from selenium import webdriver
from book_store_testing.PageObjectPages.ShopPagePO import ShopPage
from book_store_testing.PageObjectPages.StartPagePO import StartPage
from book_store_testing.PageObjectPages.RegScreenPO import RegScreen
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

start_page = StartPage(driver)
start_page.goToStartPage()
start_page.goToMyAccount()
reg_screen = RegScreen(driver)
reg_screen.clickShopButton()
shop_page = ShopPage(driver)
shop_page.checkDefaultSelectorOption()
driver.quit()