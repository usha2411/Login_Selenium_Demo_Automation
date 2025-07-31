#pytest fixture for browser setup
import pytest
from allure_commons import fixture
from selenium import webdriver

@pytest.fixture()
def browser():
    driver=webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()