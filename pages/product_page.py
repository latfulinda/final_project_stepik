from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math

class ProductPage(BasePage):
    def should_be_add_to_basket_button (self):
	    assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button add to basket not presented" #проверка надичия кнопкм  
    def add_to_basket(self): #нажать добавить в корзину
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket_button.click()
    def save_product_name(self):
        return self.get_text_from_element(*ProductPageLocators.PRODUCT_NAME_H1)
    def save_product_value(self):
        return self.get_text_from_element(*ProductPageLocators.MAIN_PRODUCT_PRICE)
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def should_be_product_in_basket_message(self, product_name):
        added_product_name = self.get_text_from_element(*ProductPageLocators.ALERT_SUCCESS)
        expected_string = "{} has been added to your basket." .format (product_name)
        assert expected_string == added_product_name, \
            f"Expected product alert got '{expected_string}' but got '{added_product_name}' "
    def should_be_basket_value(self, product_value):
        basket_value = self.get_text_from_element(*ProductPageLocators.BASKET)
        expected_string = "Basket total: " + product_value + "\nView basket"
        assert expected_string == basket_value, \
            f"Expected basket value got '{expected_string}' but got '{basket_value}' "
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS), \
           "Success message is presented, but should not be"
		   
    def should_be_disappear_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS), \
           "Success message is presented, but should not be"		   