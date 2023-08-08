from selenium.webdriver.common.by import By

class MainPageLocators():

	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():

	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

	BASKET_LINK = (By.XPATH, "//span/a")

	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class ProductPageLocators():

	SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner ")

	BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '[value="Add to basket"]')

	TEXT_AFTER_ADDING_TO_CART = (By.XPATH, '//*[@class="alertinner "]/strong')

	NAME_OF_PRODUCT = (By.XPATH, '//*[@class="col-sm-6 product_main"]/h1')

	PRICE_OF_PRODUCT = (By.XPATH, "//p[@class='price_color']")

	PRICE_AFTER_ADDING_TO_CART = (By.XPATH, '//*[@class="alertinner "]/p/strong')

class BasketPageLocators():

	BASKET_IS_NOT_EMPTY = (By.CLASS_NAME, "basket-items")

class LoginPageLocators():

	LOGIN_FORM = (By.ID, "login_form")

	EMAIL_LOGIN_INPUT = (By.CSS_SELECTOR, '[name="login-username"]')

	PASSWORD_LOGIN_INPUT = (By.CSS_SELECTOR, '[name="login-password"]')

	REGISTER_FORM = (By.ID, "register_form")

	EMAIL_REGISTER_INPUT = (By.CSS_SELECTOR, '[name="registration-email"]')

	PASSWORD_REGISTER_INPUT = (By.CSS_SELECTOR, '[name="registration-password1"]')

	PASSWORD_REGISTER_INPUT_AGAIN = (By.CSS_SELECTOR, '[name="registration-password2"]')

	EMAIL = (By.ID, "id_registration-email")

	PASSWORD = (By.ID, "id_registration-password1") 

	PASSWORD_CONFIRM = (By.ID, "id_registration-password2")

	REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')



