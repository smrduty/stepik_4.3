from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

	def add_product_to_cart(self):
		button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
		button_add_to_basket.click()
	
	def name_of_product_matches_after_add_to_cart(self):
		name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
		name_after_adding = self.browser.find_element(*ProductPageLocators.TEXT_AFTER_ADDING_TO_CART)
		assert name_after_adding.text == name_of_product.text,\
		 		"NAME OF PRODUCT DOES NOT MATCH NAME AFTER ADDING"

	def prices_match(self):
		price_of_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT)
		print(price_of_product.text)
		price_after_adding = self.browser.find_element(*ProductPageLocators.PRICE_AFTER_ADDING_TO_CART)
		print(price_after_adding.text)
		assert price_of_product.text == price_after_adding.text, "PRICES DONT MATCH"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
			"Success message is presented, but should not be"

