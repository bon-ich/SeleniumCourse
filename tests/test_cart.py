# homework 2

import pytest
import random
import time

from selenium.webdriver.common.by import By      
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.usefixtures("setup")
class TestCart:
    
    url = "http://158.101.173.161/"
    
    def add_random_duck_to_cart(self, expected_count):
        popular_products_selector = (By.CSS_SELECTOR, "section#box-popular-products div.listing article")
        add_cart_button_selector = (By.NAME, "add_cart_product")
        cart_quantity_badge_selector = (By.CSS_SELECTOR, "div.badge.quantity")
        
        popular_products = self.driver.find_elements(*popular_products_selector)
        
        # get random duck and open
        random_duck = popular_products[random.randint(0, len(popular_products) - 1)]
        random_duck.click()
        
        # add duck to cart
        self.driver.find_element(*add_cart_button_selector).click()
        
        # wait until cart counter updates
        WebDriverWait(self.driver, 5).until(expected_conditions.text_to_be_present_in_element(cart_quantity_badge_selector, expected_count))      

    def is_element_presented(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def test_empty_cart(self):        
        cart_link_selector = (By.CSS_SELECTOR, "div#cart a")

        self.driver.get(self.url)

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "section#box-popular-products div.listing")))  

        # add 3 ducks in the cart
        for i in range(1, 4):                    
            self.add_random_duck_to_cart(str(i))
            self.driver.get(self.url)       

        if(self.is_element_presented(cart_link_selector)):
            pass

        print()