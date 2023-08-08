from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

	def basket_is_empty(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_NOT_EMPTY),\
			"There are products in basket"



