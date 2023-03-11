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
    remove_book_btn = (By.CSS_SELECTOR, ".product-remove>a")
    undo_btn = (By.CSS_SELECTOR, ".woocommerce-message>a")
    quantity_field = (By.CLASS_NAME, "qty")
    apply_coupon_btn = (By.NAME, "apply_coupon")
    coupon_msg_error = (By.CLASS_NAME, "woocommerce-error")
    checkout_btn = (By.CLASS_NAME, "checkout-button")
    update_basket_btn = (By.NAME, "update_cart")
    checkout_btn = (By.CLASS_NAME, "checkout-button")

    """Order page locators"""
    first_name = (By.ID, "billing_first_name")
    last_name = (By.ID, "billing_last_name")
    order_email_field = (By.ID, "billing_email")
    phone = (By.ID, "billing_phone")
    country_selector = (By.ID, "s2id_billing_country")
    country_selector_search_field = (By.ID, "s2id_autogen1_search")
    address = (By.ID, "billing_address_1")
    city = (By.ID, "billing_city")
    state = (By.ID, "billing_state")
    zip_code = (By.ID, "billing_postcode")
    check_payments_radio = (By.ID, "payment_method_cheque")
    place_order_btn = (By.ID, "place_order")
    success_order_message = (By.CLASS_NAME, "woocommerce-thankyou-order-received")
    payment_method = (By.CSS_SELECTOR, "tfoot tr:nth-child(3)>td")




