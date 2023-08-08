from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators
import pytest
import time
import math

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
# 	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
# 	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
# 	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
# 	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
# 	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
# 	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
# 	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
# 	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
# 	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.login_guest
class TestLoginFromMainPage():

	def test_guest_can_go_to_login_page(self, browser):
		link = "https://selenium1py.pythonanywhere.com"
		page = MainPage(browser, link)
		page.open()
		page.go_to_login_page()

	def test_guest_should_see_login_link(self, browser):
		link = "https://selenium1py.pythonanywhere.com"
		page = MainPage(browser, link)
		page.open()
		page.should_be_login_link()	

#@pytest.mark.hehe
class TestUserAddToBasketFromProductPage():

	@pytest.fixture(scope="function",autouse=True)
	def setup(self, browser):
		self.link = "http://selenium1py.pythonanywhere.com/accounts/login/"
		self.page = LoginPage(browser, self.link)
		self.page.open()
		email = str(time.time()) + "@fakemail.org"
		self.page.register_new_user(email, "lasiemvasldf")
		self.page.should_be_authorised_user()

	def test_user_cant_see_success_message(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		page = ProductPage(browser, link)
		page.open()
		page.should_not_be_success_message()

	@pytest.mark.need_review
	def test_user_can_add_product_to_cart(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
		page = ProductPage(browser, link)
		page.open()
		page.add_product_to_cart()
		page.solve_quiz_and_get_code()
		time.sleep(2)
		page.name_of_product_matches_after_add_to_cart()
		time.sleep(2)
		page.prices_match()
		time.sleep(2)

@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
	#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	page = ProductPage(browser, link)
	page.open()
	page.add_product_to_cart()
	page.solve_quiz_and_get_code()
	time.sleep(2)
	page.name_of_product_matches_after_add_to_cart()
	time.sleep(2)
	page.prices_match()
	time.sleep(2)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.add_product_to_cart()
	page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message()

def test_message_dissappeared_after_adding_product_to_cart(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.add_product_to_cart()
	page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)

def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = BasketPage(browser, link)
	page.open()
	page.go_to_basket()
	page.basket_is_empty()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "https://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
	page = BasketPage(browser, link)
	page.open()
	page.go_to_basket()
	page.basket_is_empty()





