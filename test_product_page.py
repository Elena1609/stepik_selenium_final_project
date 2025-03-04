from .pages.product_page import ProductPage
#from .pages.locators import ProductPageLocators
import pytest

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.find_price_and_name()
    #price = page.browser.find_element(*ProductPageLocators.PRICE_LINK).text
    #book_name = page.browser.find_element(*ProductPageLocators.BOOK_NAME_LINK).text
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    #cart_price = page.browser.find_element(*ProductPageLocators.CART_PRICE_LINK).text
    #message = page.browser.find_element(*ProductPageLocators.MESSAGE_LINK).text
    #assert price in cart_price, "Стоимость корзины не совпадает с ценой товара!"
    #assert book_name == message , "Книга не добавлена!"
    page.check_price()
    page.check_name()
  

    
