import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--url", "-U", default="http://192.168.65.1:8081/", help="Specify url!")

@pytest.fixture
def browser(request):
    """ Фикстура инициализации браузера """
    url = request.config.getoption("--url")

    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome()

    request.addfinalizer(driver.quit)

    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)

    return driver
