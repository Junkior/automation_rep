from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

###Отображение страницы товара

# Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Залогиньтесь
my_account_btn = driver.find_element(By.ID, "menu-item-50")
my_account_btn.click()
login_email_field = driver.find_element(By.ID, "username")
login_email_field.send_keys("oxample_test@gmail.com")
login_password_field = driver.find_element(By.ID, "password")
login_password_field.send_keys("_6Words_!")
# Нажмите на вкладку "Shop"
shop_menu_btn = driver.find_element(By.ID, "menu-item-40")
shop_menu_btn.click()
# Откройте книгу "HTML 5 Forms"
html5_book_btn = driver.find_element(By.CSS_SELECTOR, ".masonry-done li:nth-child(3)>a>img")
html5_book_btn.click()
# Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
book_header = driver.find_element(By.TAG_NAME, "h1")
book_header_txt = book_header.text
assert book_header_txt == "HTML5 Forms"

###

### Количество товаров в категории

# Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Залогиньтесь
my_account_btn = driver.find_element(By.ID, "menu-item-50")
my_account_btn.click()
login_email_field = driver.find_element(By.ID, "username")
login_email_field.send_keys("oxample_test@gmail.com")
login_password_field = driver.find_element(By.ID, "password")
login_password_field.send_keys("_6Words_!")
# Нажмите на вкладку "Shop"
shop_menu_btn = driver.find_element(By.ID, "menu-item-40")
shop_menu_btn.click()
#Откройте категорию "HTML"
html_category_btn = driver.find_element(By.CSS_SELECTOR, ".cat-item-19>a")
html_category_btn.click()
# Добавьте тест, что отображается три товара
products = driver.find_elements(By.CSS_SELECTOR, ".masonry-done li")
assert len(products) == 3







