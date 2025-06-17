from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        """Finds and returns an element after waiting for it to be visible."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator, timeout=10):
        """Clicks an element after waiting for it to be clickable."""
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text, timeout=10):
        """Enters text into a text field."""
        self.find_element(locator, timeout).send_keys(text)

    def get_url(self):
        """Returns the current page URL."""
        return self.driver.current_url
