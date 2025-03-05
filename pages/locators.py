from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    CART_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    #CART_PRICE_LINK = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRICE_LINK = (By.CSS_SELECTOR, ".price_color")
    CART_PRICE_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    BOOK_NAME_LINK = (By.CSS_SELECTOR, "h1")
    MESSAGE_LINK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")

    