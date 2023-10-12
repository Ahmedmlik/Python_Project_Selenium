import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        print("--------------------- Chrome ---------")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


# Pytest Html report

# Adding Environment info to HTML Report
def pytest_configure(config):
    try:
        config._metadata['Project Name'] = 'nop Commerce'
        config._metadata['Module Name'] = 'Customers'
        config._metadata['Tester'] = 'Ahmed MLIK'
    except Exception as e:
        print("An error occurred in pytest_configure:", e)

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")