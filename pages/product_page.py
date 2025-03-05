from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    def find_price_and_name(self):
        self.price = self.browser.find_element(*ProductPageLocators.PRICE_LINK).text
        self.book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_LINK).text
    
    def add_product_to_basket(self):
        cart_link = self.browser.find_element(*ProductPageLocators.CART_LINK)
        cart_link.click()
    
    def check_price(self):
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE_LINK).text
        assert self.price in cart_price, "Стоимость корзины не совпадает с ценой товара!"    
        
    def check_name(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_LINK).text
        assert self.book_name == message , "Книга не добавлена!"