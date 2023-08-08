from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()

	def should_be_login_url(self):        
		assert "login" in self.browser.current_url, "Login url does not match"

	def should_be_login_form(self):
		assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no LOGIN form"

	def should_be_register_form(self):
		assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "There is no REGISTER form"


	def register_new_user(self, email, password):
		email_field = self.browser.find_element(*LoginPageLocators.EMAIL)
		password_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
		password_confirm_field = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
		email_field.send_keys(email)
		password_field.send_keys(password)
		password_confirm_field.send_keys(password)
		registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
		registration_button.click()



