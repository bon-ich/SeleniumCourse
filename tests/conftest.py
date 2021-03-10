import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver

    yield driver
    driver.quit()
    
@pytest.fixture
def login():
    username = ""
    password = ""
    
    # do steps to login