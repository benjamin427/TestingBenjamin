from selenium import webdriver
from utilities.configurationReader import read_configuration
import pytest

@pytest.fixture
def setup_and_teardown(request):
    browser = read_configuration("basic info", "browser")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        return "Choose the browser to execute app"
    request.cls.driver = driver
    app_url_login_page = read_configuration("basic info", "url_login_page")
    driver.get(app_url_login_page)

