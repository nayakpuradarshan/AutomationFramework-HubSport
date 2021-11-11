from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class Homepage(object):
    pass


class LoginPage(BasePage):

    """By Locators - Object Repository"""
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "LoginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign Up")

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """page actions for login page"""

    """This is used to page title"""
    def login_page_title(self, title):
        self.get_title(title)

    """This is used to check sign up link"""
    def is_signup_link_exist(self):
        self.is_visible(self.SIGNUP_LINK)

    """This is used to login to app"""
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return Homepage(self.driver)