from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_text(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE_LINK).text, "Basket must be empty." 
        
    def should_be_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There are items in the basket, but should not be"    


  
       