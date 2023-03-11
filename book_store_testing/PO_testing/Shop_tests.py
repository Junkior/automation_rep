import time

from selenium import webdriver
from book_store_testing.PageObjectPages.OrderPagePO import OrderPage
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
###
driver = DriverSet.browser()

### Работа в корзине
# Открыть http://practice.automationtesting.in/
start_page = StartPage(driver)
# Нажать на вкладку "Shop"
start_page.go_to_shop()
# обавить книгу которая есть в наличии
shop_page = ShopPage(driver)
shop_page.add_js_book_to_cart()
driver.refresh()
# Перейти в корзину
shop_page = ShopPage(driver)
shop_page.go_to_cart()
# Удалить книгу из корзины
cart_page = CartPage(driver)
cart_page.remove_book_from_cart()
# Дождаться появления кнопки undo
cart_page.wait_undo_button_appearance()
# Нажать на undo
cart_page.click_undo_btn()
# Очистить количество товаров и добавить три товара
cart_page = CartPage(driver)
cart_page.set_quantity_field_amount(3)
# Обновить корзину
cart_page.update_cart()
# Проверить что количество элемнтов == 3
cart_page.check_quantity_field_amount("3")
time.sleep(3)
# Нажать apply coupon
cart_page = CartPage(driver)
cart_page.click_apply_coupon()
# Проверить наличие ошибки добавления купона
cart_page.check_coupon_message_error()
#
driver.quit()
#
driver = DriverSet.browser()
### Покупка товара
# Открыть http://practice.automationtesting.in/
start_page = StartPage(driver)
# Нажать на вкладку "Shop"
start_page.go_to_shop()
# обавить книгу которая есть в наличии
shop_page = ShopPage(driver)
shop_page.add_js_book_to_cart()
driver.refresh()
# Перейти в корзину
shop_page = ShopPage(driver)
shop_page.go_to_cart()
# Нажать "PROCEED TO CHECKOUT"
cart_page = CartPage(driver)
cart_page.click_checkout_btn()
# Заполнить все обязательные поля
order_page = OrderPage(driver)
order_page.wait_first_name_presence()
order_page.set_first_name_field()
order_page.set_last_name_field()
order_page.set_email_field()
order_page.set_phone_field()
order_page.set_country()
order_page.set_address()
order_page.set_city()
order_page = OrderPage(driver)
order_page.set_state()
order_page.set_zipcode()
# Выбрать способ оплаты "Check Payments"
order_page.scroll_by()
order_page = OrderPage(driver)
order_page.set_payment_to_check_payments()
# 8. Нажать PLACE ORDER
order_page.click_place_order()
#  Проверить что отображается надпись "Thank you. Your order has been received."
order_page.check_success_order_message()
# Проверить что в Payment Method отображается текст "Check Payments"
order_page.check_payment_methode_check_payments()
###
driver.quit()