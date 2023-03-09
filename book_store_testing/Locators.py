from selenium.webdriver.common.by import By

class Locator(object):
    """Home test locators"""
    read_more_btn = (By.CSS_SELECTOR, ".product_tag-ruby a:nth-child(2)")
    review_tab_btn = (By.CLASS_NAME, "reviews_tab")
    five_stars_button = (By.CLASS_NAME, "star-5")
    review_field = (By.ID, "comment")
    name_field = (By.ID, "author")
    email_field = (By.ID, "email")
    submit_btn = (By.ID, "submit")

    """Login registration locators"""
    my_account_btn = (By.ID, "menu-item-50")
    email_field_registration = (By.ID, "reg_email")
    password_field_registration = (By.ID, "reg_password")
    registration_btn = (By.NAME, "register")
    login_email_field = (By.ID, "username")
    login_password_field = (By.ID, "password")
    login_btn = (By.NAME, "login")
    element_presence_check = (By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation>ul li:nth-child(6)>a")
    shop_btn = (By.ID, "menu-item-40")

    """Shop page locators"""

    html5_book_btn = (By.CSS_SELECTOR, ".masonry-done li:nth-child(3)>a>img")
    html_category_btn = (By.CSS_SELECTOR, ".cat-item-19>a")
    products_list_locator = (By.CSS_SELECTOR, ".masonry-done li")
    shop_page_default_option_filter_locator = (By.CSS_SELECTOR, ".woocommerce-ordering>select option:nth-child(1)")
    shop_page_filter_selector = (By.CSS_SELECTOR, ".woocommerce-ordering>select")
    android_quick_guide_book_locator = (By.CSS_SELECTOR, ".post-169>a")
    price_desc_option = (By.CSS_SELECTOR, ".woocommerce-ordering>select option:nth-child(6)")
    js_book_add_to_cart = (By.CSS_SELECTOR, ".masonry-done li:nth-child(6)>a:nth-child(2)")
    items_cart = (By.CLASS_NAME, "cartcontents")
    cart_price = (By.CSS_SELECTOR, ".wpmenucart-contents span:nth-child(3)")
    cart_btn = (By.ID, "wpmenucartli")

    """Android quick start guide locators"""
    old_price = (By.CSS_SELECTOR, "del>span")
    new_price = (By.CSS_SELECTOR, "ins>span")
    book_cover = (By.CSS_SELECTOR, ".images>a")
    close_btn_locator = (By.CLASS_NAME, "pp_close")

    """Cart page locators"""
    subtotal_price_element = (By.CSS_SELECTOR, ".cart-subtotal span")
    total_price_element = (By.CSS_SELECTOR, "strong>span")



