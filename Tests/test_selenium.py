import pytest

from selenium import webdriver

@pytest.fixture()
def setup(request):
    print("initializing chrome driver")
    driver = webdriver.Chrome()
    request.instance.driver = driver
    driver.get("http://seleniumeasy.com/test")
    driver.maximize_window()
    
    yield driver
    driver.close()
    
@pytest.mark.usefixtures("setup")
class TestExample:
    def test_title(self):
        print("verify title")
        assert "Selenium Easy" in self.driver.title
        
    def test_content_test(self):
        print("verify content of the page")
        center_text = self.driver.find_element_by_css_selector(".tab-content .text-center").text
        assert "WELCOME TO SELENIUM EASY DEMO" == center_text