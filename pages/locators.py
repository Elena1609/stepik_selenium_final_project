from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    
class ProductPageLocators():
    CART_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_LINK = (By.CSS_SELECTOR, ".price_color")
    CART_PRICE_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    BOOK_NAME_LINK = (By.CSS_SELECTOR, "h1")
    MESSAGE_LINK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    
class BasketPageLocators():
    BASKET_MESSAGE_LINK = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")   

    