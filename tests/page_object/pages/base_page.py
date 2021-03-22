import allure
import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from allure_commons.types import AttachmentType

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.baseurl = "http://158.101.173.161/"

    def find_element(self, locator, time=5):
        try:
            return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name=f"find_element_error_{locator}", attachment_type=AttachmentType.PNG)
            pytest.fail(f"{e}")

    def find_elements(self, locator, time=5):
        try:
            return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name=f"find_elements_error_{locator}", attachment_type=AttachmentType.PNG)
            pytest.fail(f"{e}")
    
    def goto(self, url):
        self.driver.get(url)