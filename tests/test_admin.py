import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException


@pytest.mark.usefixtures("setup")
class TestAdmin:
    admin_url = "http://158.101.173.161/admin/"
    admin_username = "testadmin"
    admin_password = "R8MRDAYT_test"
    
    def login(self):
        # fill username field
        self.driver.find_element(By.NAME, "username").send_keys(self.admin_username)
        # fill password field
        self.driver.find_element(By.NAME, "password").send_keys(self.admin_password)
        # click login button
        self.driver.find_element(By.CSS_SELECTOR, "button[name=login]").click()
        
    def get_submenus(self, menu_item):
        """ Get submenu items """
        ul = menu_item.find_element(By.CSS_SELECTOR, ".docs") 
        li = ul.find_elements(By.CSS_SELECTOR, "li.doc")
        return li        
    
    def is_element_present(self, element_locator):
        try:
            self.driver.find_element(*element_locator)
            return True
        except NoSuchElementException:
            return False
         
    def test_page_header(self):
        self.driver.implicitly_wait(5)
        self.driver.get(self.admin_url)
        
        self.login()
        
        # wait until the sidebar is displayed
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "sidebar")))        

        menu_items = self.driver.find_elements(By.CSS_SELECTOR, "ul#box-apps-menu li.app")
        
        # wait to be sure that submenus are ready
        time.sleep(1)
        
        for i in range(len(menu_items)):
            menu_items[i].click()
                        
            # update list to not to get stale element exception
            menu_items = self.driver.find_elements(By.CSS_SELECTOR, "ul#box-apps-menu li.app")

            if(self.is_element_present((By.CSS_SELECTOR, "ul.docs"))):
                submenus = self.get_submenus(menu_items[i])
                for j in range(len(submenus)):
                    submenus[j].click()
                                        
                    assert self.is_element_present((By.CSS_SELECTOR, "div.panel-heading")) == True
                    
                    # update lists to not to get stale element exception
                    menu_items = self.driver.find_elements(By.CSS_SELECTOR, "ul#box-apps-menu li.app")
                    submenus = self.get_submenus(menu_items[i])
            
            # check that page header is displayed
            assert self.is_element_present((By.CSS_SELECTOR, "div.panel-heading")) == True
