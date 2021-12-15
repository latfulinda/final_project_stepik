#from .pages.main_page import MainPage
#from .pages.login_page import LoginPage
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage

import time
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
@pytest.mark.skip
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
def test_guest_can_add_product_to_basket (browser, link):
    page = ProductPage(browser, link)   	# инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
    page.open()                         	# открываем страницу
    page.should_be_add_to_basket_button()	# провер€ем наличие кнопки
    product_name = page.save_product_name ()				# сохран€ем им€ товара
    product_value = page.save_product_value()				# сохран€ем цену товара
    page.add_to_basket ()					# нажимаем добавить в корзину
    page.solve_quiz_and_get_code()			# решаем задачку
    print(product_name)
    print (product_value)
    page.should_be_product_in_basket_message(product_name) # провер€ем что присутствует сообщение о том что
    # нужный товар добавлен в корзину
    page.should_be_basket_value(product_value)	 # провер€ем стоимость товаров в корзине
    time.sleep (1)

@pytest.mark.xfail    
def test_guest_cant_see_success_message_after_adding_product_to_basket (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket ()
    page.should_be_add_to_basket_button()  
    page.should_not_be_success_message()

@pytest.mark.skip    
def test_guest_cant_see_success_message (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail    
def test_message_disappeared_after_adding_product_to_basket (browser):
    ink = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket ()
    page.should_be_add_to_basket_button() 
    page.should_be_disappear_message()

@pytest.mark.skip     
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket() # переход по кнопке в корзину
    basket_page = BasketPage (browser, browser.current_url)
    basket_page.should_not_be_products_in_basket () #ќжидаем что в корзине нет товаров
    basket_page.should_basket_empty_text_present () #ќжидаем что есть текст о том что корзина пуста


class TestUserAddToBasketFromProductPage ():
    @pytest.fixture(scope="function", autouse=True)
    def test_test(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, "Qw123456789")
        base_page = BasePage(browser, browser.current_url)
        base_page.should_be_authorized_user()
        
    def test_user_cant_see_success_message (self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket (self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   	# инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
        page.open()                         	# открываем страницу
        #page.should_be_add_to_basket_button()	# провер€ем наличие кнопки
        product_name = page.save_product_name ()				# сохран€ем им€ товара
        product_value = page.save_product_value()				# сохран€ем цену товара
        page.add_to_basket ()					# нажимаем добавить в корзину
        #page.solve_quiz_and_get_code()			# решаем задачку
        page.should_be_product_in_basket_message(product_name) # провер€ем что присутствует сообщение о том что
        # нужный товар добавлен в корзину
        page.should_be_basket_value(product_value)	 # провер€ем стоимость товаров в корзине
        time.sleep (1)    