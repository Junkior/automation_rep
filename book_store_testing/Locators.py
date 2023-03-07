from selenium.webdriver.common.by import By

class Locator(object):
    """Home test locators"""
    read_more_btn = ".product_tag-ruby a:nth-child(2)"
    review_tab_btn = "reviews_tab"
    five_stars_button = "star-5"
    review_field = "comment"
    name_field = "author"
    email_field = "email"
    submit_btn = "submit"

    """Login registration locators"""
    my_account_btn = "menu-item-50"
    email_field_registration = "reg_email"
    password_field_registration = "reg_password"
    registration_btn = "register"
    login_email_field = "username"
    login_password_field = "password"
    login_btn = "login"
    element_presence_check = ".woocommerce-MyAccount-navigation>ul li:nth-child(6)>a"
    shop_btn = (By.ID, "menu-item-40")

    """Shop page locators"""

    html5_book_btn = (By.CSS_SELECTOR, ".masonry-done li:nth-child(3)>a>img")
    html_category_btn = (By.CSS_SELECTOR, ".cat-item-19>a")
    products_list_locator = (By.CSS_SELECTOR, ".masonry-done li")
    shop_page_default_option_filter_locator = (By.CSS_SELECTOR, ".woocommerce-ordering>select option:nth-child(1)")
    shop_page_filter_selector = (By.CSS_SELECTOR, ".woocommerce-ordering>select option:nth-child(6)")
    android_quick_guide_book_locator = (By.CSS_SELECTOR, ".post-169>a")
    js_book_locator = (By.CSS_SELECTOR, ".masonry-done li:nth-child(6)>a:nth-child(2)")
    price_desc_option = (By.CSS_SELECTOR, ".woocommerce-ordering>select option:nth-child(6)")



