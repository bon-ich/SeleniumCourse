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
    
    def add_random_item_to_cart(self, expected_count):
        popular_products_selector = (By.CSS_SELECTOR, "section#box-popular-products div.listing article")
        add_cart_button_selector = (By.NAME, "add_cart_product")
        cart_quantity_badge_selector = (By.CSS_SELECTOR, "div.badge.quantity")        
        popular_products = self.driver.find_elements(*popular_products_selector)
        
        # get random item and open
        random_item = popular_products[random.randint(0, len(popular_products) - 1)]
        random_item.click()

        # added because button isn't clicked randomly without a small wait
        # and WebDriverWait until element_to_be_clickable didn't helped 
        time.sleep(0.5)
        
        # add item to cart
        self.driver.find_element(*add_cart_button_selector).click()
        
        # wait until cart counter updates
        WebDriverWait(self.driver, 5).until(expected_conditions.text_to_be_present_in_element(cart_quantity_badge_selector, expected_count))      

    def is_element_presented(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def remove_all_items_from_cart(self):
        "Removes all items one by one"
        items_selector = (By.CSS_SELECTOR, "ul.items")
        remove_item_btn_selector = (By.NAME, "remove_cart_item")

        # wait until item are displayed
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(items_selector))

        items_ul = self.driver.find_element(*items_selector)
        items = items_ul.find_elements(By.CSS_SELECTOR, "li")

        print("start removing items from cart")
        while len(items) > 0:
            print(f"items left: {len(items)}")

            # remove item from the cart
            items[0].find_element(*remove_item_btn_selector).click()
            del items[0]

            WebDriverWait(self.driver, 10).until(expected_conditions.staleness_of(items_ul))

            # if there is at least one item left refresh items
            if len(items) >= 1:
                items_ul = self.driver.find_element(*items_selector)
                items = items_ul.find_elements(By.CSS_SELECTOR, "li")

        print("all items are removed")


    def test_empty_cart(self):        
        cart_link_selector = (By.CSS_SELECTOR, "div#cart a")

        self.driver.get(self.url)

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "section#box-popular-products div.listing")))  

        # add 3 items in the cart
        for i in range(1, 4):                    
            self.add_random_item_to_cart(str(i))
            # go to the main page
            self.driver.get(self.url)       

        self.driver.find_element(*cart_link_selector).click()
        self.remove_all_items_from_cart()

        # assert if list with items is displayed after all items are removed from the cart
        assert self.is_element_presented((By.CSS_SELECTOR, "ul.items")) == False
