from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

##Отображение страницы товара

# Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Залогиньтесь
my_account_btn = driver.find_element(By.ID, "menu-item-50")
my_account_btn.click()
login_email_field = driver.find_element(By.ID, "username")
login_email_field.send_keys("oxample_test@gmail.com")
login_password_field = driver.find_element(By.ID, "password")
login_password_field.send_keys("_6Words_!")
login_btn = driver.find_element(By.NAME, "login")
login_btn.click()
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
driver.delete_all_cookies()
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
login_btn = driver.find_element(By.NAME, "login")
login_btn.click()
# Нажмите на вкладку "Shop"
shop_menu_btn = driver.find_element(By.ID, "menu-item-40")
shop_menu_btn.click()
#Откройте категорию "HTML"
html_category_btn = driver.find_element(By.CSS_SELECTOR, ".cat-item-19>a")
html_category_btn.click()
# Добавьте тест, что отображается три товара
products = driver.find_elements(By.CSS_SELECTOR, ".masonry-done li")
assert len(products) == 3
###
driver.delete_all_cookies()
#Сортировка товаров

# Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Залогиньтесь
my_account_btn = driver.find_element(By.ID, "menu-item-50")
my_account_btn.click()
login_email_field = driver.find_element(By.ID, "username")
login_email_field.send_keys("oxample_test@gmail.com")
login_password_field = driver.find_element(By.ID, "password")
login_password_field.send_keys("_6Words_!")
login_btn = driver.find_element(By.NAME, "login")
login_btn.click()
# 3. Нажмите на вкладку "Shop"
shop_menu_btn = driver.find_element(By.ID, "menu-item-40")
shop_menu_btn.click()
# 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
option_default = driver.find_element(By.CSS_SELECTOR, ".woocommerce-ordering>select option:nth-child(1)")
option_default_value = option_default.get_attribute("selected")
assert option_default_value is not None
# Отсортируйте товары по цене от большей к меньшей
selector_element = driver.find_element(By.CSS_SELECTOR, ".woocommerce-ordering>select")
Select(selector_element).select_by_value("price-desc")
# 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
price_desc_option = driver.find_element(By.CSS_SELECTOR, ".woocommerce-ordering>select option:nth-child(6)")
price_desc_option_value = price_desc_option.get_attribute("selected")
assert price_desc_option_value is not None

###
driver.delete_all_cookies()
# Отображение, скидка товара

# Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Залогиньтесь
my_account_btn = driver.find_element(By.ID, "menu-item-50")
my_account_btn.click()
login_email_field = driver.find_element(By.ID, "username")
login_email_field.send_keys("oxample_test@gmail.com")
login_password_field = driver.find_element(By.ID, "password")
login_password_field.send_keys("_6Words_!")
login_btn = driver.find_element(By.NAME, "login")
login_btn.click()
# Нажмите на вкладку "Shop"
shop_menu_btn = driver.find_element(By.ID, "menu-item-40")
shop_menu_btn.click()
# Откройте книгу "Android Quick Start Guide"
android_book = driver.find_element(By.CSS_SELECTOR, ".post-169>a")
android_book.click()
# Добавьте тест, что содержимое старой цены = "₹600.00"
old_price = driver.find_element(By.CSS_SELECTOR, "del>span")
old_price_text = old_price.text
print(old_price_text)
if '₹' in old_price_text:
    old_price_text = old_price_text[1:]
assert  old_price_text== "600.00"
# Добавьте тест, что содержимое новой цены = "₹450.00"
new_price = driver.find_element(By.CSS_SELECTOR, "ins>span")
new_price_text = new_price.text
print(new_price_text)
if '₹' in new_price_text:
    new_price_text = new_price_text[1:]
assert new_price_text == "450.00"
#  Добавьте явное ожидание и нажмите на обложку книги
book_cover = driver.find_element(By.CSS_SELECTOR, ".images>a")
book_cover.click()
# Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
preview_img_check = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "pp_close"))
)
driver.find_element(By.CLASS_NAME, "pp_close").click()

###
driver.delete_all_cookies()








