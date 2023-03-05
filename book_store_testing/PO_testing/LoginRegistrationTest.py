from selenium import webdriver
from book_store_testing.PageObjectPages.StartPagePO import StartPage
from book_store_testing.PageObjectPages.RegScreenPO import RegScreen
from book_store_testing.PageObjectPages.LoggedScreenPO import LoggedPage
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)



start_page = StartPage(driver)
### Регистрация аккаунта

# Открыть http://practice.automationtesting.in/
start_page.goToStartPage()
# Нажать на вкладку "My Account Menu"
start_page.goToMyAccount()
#
reg_screen = RegScreen(driver)
#
# Ввести email для регистрации в разделе "Register"
reg_screen.setEmailRegistrationField("oxample_test@gmail.com")
# Ввести password  для регистрации в разделе "Register"
reg_screen.setPasswordRegistrationField("_6Words_!")
# Нажать на кнопку "Register"
reg_screen.clickRegistrationButton()
###

### Логин в систему

start_page  = StartPage(driver)
# Открыть http://practice.automationtesting.in/
start_page.goToStartPage()
# Нажать на вкладку "My Account Menu"
start_page.goToMyAccount()
#
reg_screen = RegScreen(driver)
#
# Ввести email для регистрации в разделе "Login"
reg_screen.setEmailLoginField("oxample_test@gmail.com")
# Ввести login для регистрации в разделе "Login"
reg_screen.setPasswordLoginField("_6Words_!")
# Нажать на кнопку "Login"
reg_screen.clickLoginButton()
#
logged_screen = LoggedPage(driver)
#
# Добавить проверку, что на странице есть элемент "Logout"
logged_screen.checkPresenceOfElement()
###
driver.quit()