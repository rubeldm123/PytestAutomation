import pytest
from selenium import webdriver
import inspect
from utils import data


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default='chrome',
                     help="specify the host to run tests with. local|stage")


@pytest.fixture(scope="class")
def test_setup(request):
    driver_path = '/Users/mdrubel/Downloads/python_workspace/Jan19Project/drivers/chromedriver'
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=driver_path)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=driver_path)
    elif browser == 'safari':
        driver = webdriver.Safari(executable_path=driver_path)
    else:
        driver = webdriver.Chrome(executable_path=driver_path)

    driver.get(data.URL)
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")
