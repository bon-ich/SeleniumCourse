import pytest
import random

from selenium.webdriver.common.by import By      
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  


@pytest.mark.usefixtures("setup")
class TestCart:
    
    url = "http://158.101.173.161/"
    
    def add_random_duck_to_cart(self):
        popular_products_selector = (By.CSS_SELECTOR, "section#box-popular-products div.listing article")
        add_cart_button_selector = (By.NAME, "add_cart_product")
        
        popular_products = self.driver.find_elements(*popular_products_selector)
        
        # get random duck and open
        random_index = random.randint(0, len(popular_products) - 1)
        random_duck = popular_products[random_index]
        random_duck.click()
        
        self.driver.find_element(*add_cart_button_selector).click()
    
    def test_empty_cart(self):        
        self.driver.get(self.url)

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "section#box-popular-products div.listing")))     
        
        self.add_random_duck_to_cart()
        
        print()