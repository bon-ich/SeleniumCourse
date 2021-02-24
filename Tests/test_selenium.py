from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_one():
    chrome_driver = webdriver.Chrome("Tests/drivers/chromedriver.exe")
    chrome_driver.get("https://www.google.com/")
    assert "Google" in chrome_driver.title
    search_field = chrome_driver.find_element_by_name("q")
    search_field.clear()
    search_field.send_keys("python")
    search_field.send_keys(Keys.RETURN)
    assert "python" in chrome_driver.title
    chrome_driver.quit()
