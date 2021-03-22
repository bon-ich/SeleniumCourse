import random
import time
import allure

from .base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class HomePageLocators:
    POPULAR_PRODUCRS_LOCATOR = (By.CSS_SELECTOR, "section#box-popular-products div.listing article")
    CART_LINK_LOCATOR = (By.CSS_SELECTOR, "div#cart a")


class HomePage(BasePage):
    @allure.step("Get home page")
    def get_page(self):
        self.goto(self.baseurl)

    @allure.step("Open random product from 'Popular' section")
    def open_random_popular_product(self):
        popular_products = self.find_elements(HomePageLocators.POPULAR_PRODUCRS_LOCATOR)
        
        random_item = popular_products[random.randint(0, len(popular_products) - 1)]
        random_item.click()
        
        time.sleep(0.5)
    
    def open_cart(self):
        self.find_element(HomePageLocators.CART_LINK_LOCATOR).click()