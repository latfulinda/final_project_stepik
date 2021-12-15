import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполн€ем метод страницы Ч переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
	
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
   
@pytest.mark.login_guest
class TestLoginFromMainPage():   
    def test_guest_cant_see_product_in_basket_opened_from_main_page (browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket() # переход по кнопке в корзину
        basket_page = BasketPage (browser, browser.current_url)
        basket_page.should_not_be_products_in_basket () #ќжидаем что в корзине нет товаров
        basket_page.should_basket_empty_text_present () #ќжидаем что есть текст о том что корзина пуста