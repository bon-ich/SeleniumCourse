import allure

from .base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from allure_commons.types import AttachmentType

class ProductPageLocators:    
    ADD_CART_BUTTON_LOCATOR = (By.NAME, "add_cart_product")
    CART_QUANTITY_BADGE_LOCATOR = (By.CSS_SELECTOR, "div.badge.quantity")

class ProductPage(BasePage):
    @allure.step("Add item to cart")
    def add_item_to_cart(self, expected_count):    
        add_button = self.find_element(ProductPageLocators.ADD_CART_BUTTON_LOCATOR)
        # scroll to get button at the top of the page 
        # button can be hovered by cookies message
        add_button.location_once_scrolled_into_view
        # add item to cart
        add_button.click()        
        # wait until cart counter updates
        WebDriverWait(self.driver, 5).until(expected_conditions.text_to_be_present_in_element(ProductPageLocators.CART_QUANTITY_BADGE_LOCATOR, expected_count))  