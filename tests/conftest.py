import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # No UI needed
    chrome_options.add_argument("--no-sandbox")  # Helps with root in container
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevents shared memory issues
    chrome_options.add_argument("--window-size=1920,1080")  # Emulate a screen size

    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    
    yield driver

    driver.quit()
