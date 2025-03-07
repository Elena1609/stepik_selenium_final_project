from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    CART_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_LINK = (By.CSS_SELECTOR, ".price_color")
    CART_PRICE_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    BOOK_NAME_LINK = (By.CSS_SELECTOR, "h1")
    MESSAGE_LINK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")

    