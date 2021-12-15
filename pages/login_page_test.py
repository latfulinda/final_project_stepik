from .base_page import BasePage
#from .locators import MainPageLocators
from .locators import BasePageLocators
from .locators import LoginPageLocators
class LoginPage(BasePage):
     
    def test_register_new_user(self, email, password):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_REGISTER_LINK)
        login_link.click()
        input_email = self.browser.find_element(*LoginPageLocators.INPUT_FIELD_EMAIL)
        input_email.send_keys(email)
        input_password1 = self.browser.find_element(*LoginPageLocators.INPUT_FIELD_PASSWORD1)
        input_password1.send_keys(password)
        input_password2 = self.browser.find_element(*LoginPageLocators.INPUT_FIELD_PASSWORD2)
        input_password2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION_SUBMIT)
        register_button.click()