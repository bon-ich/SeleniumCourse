import random
import time

from .base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  

class CartPageLocators:
    ITEMS_LOCATOR = (By.CSS_SELECTOR, "ul.items")
    REMOVE_ITEM_BTN_SELECTOR = (By.NAME, "remove_cart_item")

class CartPage(BasePage):
    def remove_all_items_from_cart(self):
        # wait until item are displayed
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(CartPageLocators.ITEMS_LOCATOR))

        items_ul = self.find_element(CartPageLocators.ITEMS_LOCATOR)
        items = items_ul.find_elements(By.CSS_SELECTOR, "li")

        print("start removing items from cart")
        while len(items) > 0:
            print(f"\titems left: {len(items)}")
            
            WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(CartPageLocators.REMOVE_ITEM_BTN_SELECTOR))

            # remove item from the cart
            items[0].find_element(*CartPageLocators.REMOVE_ITEM_BTN_SELECTOR).click()
            del items[0]

            WebDriverWait(self.driver, 10).until(expected_conditions.staleness_of(items_ul))

            # if there is at least one item left refresh items
            if len(items) >= 1:
                items_ul = self.find_element(CartPageLocators.ITEMS_LOCATOR)
                items = items_ul.find_elements(By.CSS_SELECTOR, "li")

        print("all items are removed")
        
    def is_items_list_displayed(self):
        # return len(self.find_elements((By.CSS_SELECTOR, "ul.items"))) != 0
        try: 
            self.find_element((By.CSS_SELECTOR, "ul.items"))
            return True
        except: 
            return False