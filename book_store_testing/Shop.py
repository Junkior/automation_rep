import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

##Отображение страницы товара

# # Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Залогиниться
my_account_btn = driver.find_element(By.ID, "menu-item-50")
my_account_btn.click()
login_email_field = driver.find_element(By.ID, "username")
login_email_field.send_keys("oxample_test@gmail.com")
login_password_field = driver.find_element(By.ID, "password")
login_password_field.send_keys("_6Words_!")
login_btn = driver.find_element(By.NAME, "login")
login_btn.click()
# Нажать на вкладку "Shop"
shop_menu_btn = driver.find_element(By.ID, "menu-item-40")
shop_menu_btn.click()
# Открыть книгу "HTML 5 Forms"
html5_book_btn = driver.find_element(By.CSS_SELECTOR, ".masonry-done li:nth-child(3)>a>img")
html5_book_btn.click()
# Добавить тест, что заголовок книги назвается: "HTML5 Forms"
book_header = driver.find_element(By.TAG_NAME, "h1")
book_header_txt = book_header.text
assert book_header_txt == "HTML5 Forms"

###
driver.delete_all_cookies()
### Количество товаров в категории

# Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Залогиниться
my_account_btn = driver.find_element(By.ID, "menu-item-50")
my_account_btn.click()
login_email_field = driver.find_element(By.ID, "username")
login_email_field.send_keys("oxample_test@gmail.com")
login_password_field = driver.find_element(By.ID, "password")
login_password_field.send_keys("_6Words_!")
login_btn = driver.find_element(By.NAME, "login")
login_btn.click()
# Нажать на вкладку "Shop"
shop_menu_btn = driver.find_element(By.ID, "menu-item-40")
shop_menu_btn.click()
# Открыть категорию "HTML"
html_category_btn = driver.find_element(By.CSS_SELECTOR, ".cat-item-19>a")
html_category_btn.click()
# Добавить тест, что отображается три товара
products = driver.find_elements(By.CSS_SELECTOR, ".masonry-done li")
assert len(products) == 3
###
driver.delete_all_cookies()
#Сортировка товаров

# Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Залогиниться
my_account_btn = driver.find_element(By.ID, "menu-item-50")
my_account_btn.click()
login_email_field = driver.find_element(By.ID, "username")
login_email_field.send_keys("oxample_test@gmail.com")
login_password_field = driver.find_element(By.ID, "password")
login_password_field.send_keys("_6Words_!")
login_btn = driver.find_element(By.NAME, "login")
login_btn.click()
# Нажать на вкладку "Shop"
shop_menu_btn = driver.find_element(By.ID, "menu-item-40")
shop_menu_btn.click()
#  Добавить тест, что в селекторе выбран вариант сортировки по умолчанию
option_default = driver.find_element(By.CSS_SELECTOR, ".woocommerce-ordering>select option:nth-child(1)")
option_default_value = option_default.get_attribute("selected")
assert option_default_value is not None
# Отсортировать товары по цене от большей к меньшей
selector_element = driver.find_element(By.CSS_SELECTOR, ".woocommerce-ordering>select")
Select(selector_element).select_by_value("price-desc")
# Добавить тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
price_desc_option = driver.find_element(By.CSS_SELECTOR, ".woocommerce-ordering>select option:nth-child(6)")
price_desc_option_value = price_desc_option.get_attribute("selected")
assert price_desc_option_value is not None

###
driver.delete_all_cookies()
### Отображение, скидка товара

# Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Залогиниться
my_account_btn = driver.find_element(By.ID, "menu-item-50")
my_account_btn.click()
login_email_field = driver.find_element(By.ID, "username")
login_email_field.send_keys("oxample_test@gmail.com")
login_password_field = driver.find_element(By.ID, "password")
login_password_field.send_keys("_6Words_!")
login_btn = driver.find_element(By.NAME, "login")
login_btn.click()
# Нажать на вкладку "Shop"
shop_menu_btn = driver.find_element(By.ID, "menu-item-40")
shop_menu_btn.click()
# Открыть книгу "Android Quick Start Guide"
android_book = driver.find_element(By.CSS_SELECTOR, ".post-169>a")
android_book.click()
# Добавить тест, что содержимое старой цены = "₹600.00"
old_price = driver.find_element(By.CSS_SELECTOR, "del>span")
old_price_text = old_price.text
if '₹' in old_price_text:
    old_price_text = old_price_text[1:]
assert  old_price_text== "600.00"
# Добавить тест, что содержимое новой цены = "₹450.00"
new_price = driver.find_element(By.CSS_SELECTOR, "ins>span")
new_price_text = new_price.text
if '₹' in new_price_text:
    new_price_text = new_price_text[1:]
assert new_price_text == "450.00"
# Нажать на обложку книги
book_cover = driver.find_element(By.CSS_SELECTOR, ".images>a")
book_cover.click()
# Закрыть предпросмотр
preview_img_check = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "pp_close"))
)
driver.find_element(By.CLASS_NAME, "pp_close").click()

###
driver.delete_all_cookies()

###Проверка цены в корзине

# Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Нажать на вкладку "Shop"
shop_menu_btn = driver.find_element(By.ID, "menu-item-40")
shop_menu_btn.click()
# Добавить книгу которая есть в наличии
js_book_add_to_basket = driver.find_element(By.CSS_SELECTOR, ".masonry-done li:nth-child(6)>a:nth-child(2)")
js_book_add_to_basket.click()
driver.refresh()
time.sleep(2)
# Проверить что количество товаров в корзине = 1
items_basket = driver.find_element(By.CLASS_NAME, "cartcontents")
items_basket_text = items_basket.text
assert items_basket_text == "1 Item"
# Проверить что сумма товаров в корзине равна 350.00
basket_price = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents span:nth-child(3)")
basket_price_text = basket_price.text
if '₹' in basket_price_text:
    basket_price_text = basket_price_text[1:]
assert basket_price_text == "350.00"
# Открыть корзину
cart_btn = driver.find_element(By.ID, "wpmenucartli")
cart_btn.click()
# Проверить наличие цены в subtotal
subtotal_price_check = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal span"), "₹350.00")
)
# Проверить наличие цены в total
subtotal_price_check = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "strong>span"), "₹357.00")
)
###
driver.delete_all_cookies()
### Работа в корзине

# Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Нажать на вкладку "Shop"
shop_menu_btn = driver.find_element(By.ID, "menu-item-40")
shop_menu_btn.click()
# Добавить книгу которая есть в наличии
js_book_add_to_basket = driver.find_element(By.CSS_SELECTOR, ".masonry-done li:nth-child(6)>a:nth-child(2)")
js_book_add_to_basket.click()
time.sleep(3)
# Перейти в корзину
cart_btn = driver.find_element(By.ID, "wpmenucartli")
cart_btn.click()
# Удалить книгу из корзины
remove_book_btn = driver.find_element(By.CSS_SELECTOR, ".product-remove>a")
remove_book_btn.click()
# Дождаться появления кнопки undo
undo_btn_check = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".woocommerce-message>a"))
)
# Нажать на undo
undo_btn = driver.find_element(By.CSS_SELECTOR, ".woocommerce-message>a")
undo_btn.click()
# Очистить количество товаров
quantity_field = driver.find_element(By.CLASS_NAME, "qty")
quantity_field.clear()
# Добавить три товара
quantity_field.send_keys(3)
# Обновить корзину
update_basket_btn = driver.find_element(By.NAME, "update_cart")
update_basket_btn.click()
# Проверить что количество элемнтов = 3
quantity_field_value = driver.find_element(By.CLASS_NAME, "qty").get_attribute("value")
assert quantity_field_value == "3"
time.sleep(3)
# Нажать apply coupon
apply_coupon_btn = driver.find_element(By.NAME, "apply_coupon")
apply_coupon_btn.click()
# Проверить наличие ошибки добавления купона
coupon_msg_error = driver.find_element(By.CLASS_NAME, "woocommerce-error")
coupon_msg_error_text = coupon_msg_error.text
assert coupon_msg_error_text == "Please enter a coupon code."
###
driver.delete_all_cookies()
### Покупка товара

# Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Нажать на вкладку "Shop" и проскроллить на 300 пикселей вниз
shop_menu_btn = driver.find_element(By.ID, "menu-item-40")
shop_menu_btn.click()
driver.execute_script("window.scrollBy(0,330);")
# Добавить в корзину книгу в наличии
js_book_add_to_basket = driver.find_element(By.CSS_SELECTOR, ".masonry-done li:nth-child(6)>a:nth-child(2)")
js_book_add_to_basket.click()
time.sleep(3)
# Перейти в корзину
cart_btn = driver.find_element(By.ID, "wpmenucartli")
cart_btn.click()
# Нажать "PROCEED TO CHECKOUT"
checkout_btn = driver.find_element(By.CLASS_NAME, "checkout-button")
checkout_btn_wait = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "checkout-button"))
)
checkout_btn.click()
# Заполнить все обязательные поля
first_name_field_waitng = wait.until(
    EC.presence_of_element_located((By.ID, "billing_first_name"))
)
driver.find_element(By.ID, "billing_first_name").send_keys("Mike") ## first name
driver.find_element(By.ID, "billing_last_name").send_keys("Portnoy") ## last name
driver.find_element(By.ID, "billing_email").send_keys("oxample@gmail.com") ## email
driver.find_element(By.ID, "billing_phone").send_keys("9006665531") ## phone
country_selector = driver.find_element(By.ID, "s2id_billing_country") ## country
country_selector.click()
selector_country = driver.find_element(By.ID, "s2id_autogen1_search")
selector_country.send_keys("Armenia")
selector_country.send_keys(Keys.ENTER)
driver.find_element(By.ID, "billing_address_1").send_keys("Fake adress") ##adress
driver.find_element(By.ID, "billing_city").send_keys("Lars") ## city
driver.find_element(By.ID, "billing_state").send_keys("Fake state") ## state
driver.find_element(By.ID, "billing_postcode").send_keys("123456") ## zip code
# Выбрать способ оплаты "Check Payments"
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
check_payments_radio = driver.find_element(By.ID, "payment_method_cheque")
check_payments_radio.click()
# 8. Нажать PLACE ORDER
place_order_btn = driver.find_element(By.ID, "place_order")
place_order_btn.click()
#  Проверить что отображается надпись "Thank you. Your order has been received."
post_order_text_check = wait.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received.")
)
# Проверить что в Payment Method отображается текст "Check Payments"
payment_method_check = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot tr:nth-child(3)>td"), "Check Payments")
)
###
driver.quit()





