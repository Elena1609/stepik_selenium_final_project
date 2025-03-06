from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):    
    
    def add_product_to_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_LINK).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_LINK).text
        cart_link = self.browser.find_element(*ProductPageLocators.CART_LINK)
        cart_link.click()
        self.solve_quiz_and_get_code()
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE_LINK).text
        assert price in cart_price, "Стоимость корзины не совпадает с ценой товара!"
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_LINK).text
        assert book_name == message , "Книга не добавлена!"        