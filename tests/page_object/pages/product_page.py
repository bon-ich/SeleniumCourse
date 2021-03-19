import random
import time

from .base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class ProductPageLocators:    
    ADD_CART_BUTTON_LOCATOR = (By.NAME, "add_cart_product")
    CART_QUANTITY_BADGE_LOCATOR = (By.CSS_SELECTOR, "div.badge.quantity")

class ProductPage(BasePage):
    def add_item_to_cart(self, expected_count):
        # add item to cart
        self.find_element(ProductPageLocators.ADD_CART_BUTTON_LOCATOR).click()        
        # wait until cart counter updates
        WebDriverWait(self.driver, 5).until(expected_conditions.text_to_be_present_in_element(ProductPageLocators.CART_QUANTITY_BADGE_LOCATOR, expected_count))    