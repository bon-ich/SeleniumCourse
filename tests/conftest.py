import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome()
    request.cls.driver = driver

    yield driver
    driver.close()
    
@pytest.fixture
def login():
    username = ""
    password = ""
    
    # do steps to login