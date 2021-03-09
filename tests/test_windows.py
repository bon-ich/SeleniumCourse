# homework 3

import pytest
import random
import time

from selenium.webdriver.common.by import By      
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.usefixtures("setup")
class TestWindows:
    url = "http://158.101.173.161/admin/?app=countries&doc=countries"

    admin_username = "testadmin"
    admin_password = "R8MRDAYT_test"

    def login(self):
        # fill username field
        self.driver.find_element(By.NAME, "username").send_keys(self.admin_username)
        # fill password field
        self.driver.find_element(By.NAME, "password").send_keys(self.admin_password)
        # click login button
        self.driver.find_element(By.CSS_SELECTOR, "button[name=login]").click()

    def is_element_present(self, locator):
        """Check if element is present on the page"""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def test_links_in_separate_windows(self):
        external_link_selector = (By.CSS_SELECTOR, "i.fa.fa-external-link")

        self.driver.get(self.url)

        # if countries page is not displayed login
        if not self.is_element_present((By.CLASS_NAME, "panel-heading")):
            self.login()
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "panel-heading")))

        # click new country button
        self.driver.find_element(By.XPATH, "//a[text()=' Add New Country']").click()

        external_links = self.driver.find_elements(*external_link_selector)
        print(len(external_links))

        for link in external_links:
            link.click()

        time.sleep(2)



        