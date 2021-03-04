import pytest

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
        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys(self.admin_username)

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(self.admin_password)

        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[name=login]")
        login_button.click()
    
    def has_submenus(self, menu_item):
        """ Check if menu item has submenus """
        try:
            menu_item.find_element(By.CSS_SELECTOR, ".docs")    
            return True    
        except NoSuchElementException:
            return False
    
    def get_submenus(self, menu_item):
        """ Get submenu items """
        ul = menu_item.find_element(By.CSS_SELECTOR, ".docs") 
        li = ul.find_elements(By.CSS_SELECTOR, "li.doc")
        return li          
     
    def is_page_header_presented(self):
        """ Check if page header is displayed """
        try:
            self.driver.find_element(By.CSS_SELECTOR, "div.panel-heading")
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
        
        for i in range(len(menu_items)):
            
            menu_items[i].click()
                        
            # update list to not to get stale element exception
            menu_items = self.driver.find_elements(By.CSS_SELECTOR, "ul#box-apps-menu li.app")

            if(self.has_submenus(menu_items[i])):
                submenus = self.get_submenus(menu_items[i])
                for j in range(len(submenus)):
                    submenus[j].click()
                                        
                    # update lists to not to get stale element exception
                    menu_items = self.driver.find_elements(By.CSS_SELECTOR, "ul#box-apps-menu li.app")
                    submenus = self.get_submenus(menu_items[i])
            
            # check that page header is displayed
            assert self.is_page_header_presented() == True
