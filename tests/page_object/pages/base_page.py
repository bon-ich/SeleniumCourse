from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.baseurl = "http://158.101.173.161/"

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")
    
    def goto(self, url):
        self.driver.get(url)