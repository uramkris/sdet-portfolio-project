from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        """Performs a full login action."""
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """Returns the login error message, if any."""
        return self.find_element(self.ERROR_MESSAGE).text
