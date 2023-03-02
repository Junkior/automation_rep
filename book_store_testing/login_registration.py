import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

### Регистрация аккаунта

# Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Нажмите на вкладку "My Account Menu"
my_account_btn = driver.find_element(By.ID, "menu-item-50")
my_account_btn.click()
# В разделе "Register", введите email для регистрации
email_field = driver.find_element(By.ID, "reg_email")
email_field.send_keys("oxample_test@gmail.com")
# В разделе "Register", введите пароль для регистрации
password_field = driver.find_element(By.ID, "reg_password")
password_field.send_keys("_6Words_!")
# Нажмите на кнопку "Register"
registration_btn = driver.find_element(By.NAME, "register")
registration_btn.click()
###


### Логин в систему


# Откройте http://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")
# Нажмите на вкладку "My Account Menu"
my_account_btn = driver.find_element(By.ID, "menu-item-50")
my_account_btn.click()
# В разделе "Login", введите email для логина
login_email_field = driver.find_element(By.ID, "username")
login_email_field.send_keys("oxample_test@gmail.com")
# В разделе "Login", введите пароль для логина
login_password_field = driver.find_element(By.ID, "password")
login_password_field.send_keys("_6Words_!")
# Нажмите на кнопку "Login"
login_btn = driver.find_element(By.NAME, "login")
login_btn.click()
# Добавьте проверку, что на странице есть элемент "Logout"
logout_element_check = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation>ul li:nth-child(6)>a"))
)
###

