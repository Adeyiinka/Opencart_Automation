import os.path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from datetime import datetime


# Fixture for setting up the WebDriver
@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        print("Launching Edge browser")

    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        print("Launching Firefox browser")

    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Launching Chrome browser")
    return driver


# Fixture for getting browser configuration from command line. This will get the value from CLI/hooks
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


# Fixture to provide the browser configuration to other fixtures. This will return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#  pytest HTML Report configuration for adding Environment info to HTML Report
def pytest_configure(config):
    config._metdata['Project Name'] = 'OpenCart'
    config._metdata['Module Name'] = 'CustomerRegistration'
    config._metdata['Tester Name'] = 'Ibrahim Adekunle'


# It is hook for delete/modify Environment info to HTML Report
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)


# Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(
        os.path.join(os.curdir, "reports", datetime.now().strftime("%d-%m-%y %H-%M-%S") + ".html"))
