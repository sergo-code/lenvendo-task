import os
import pytest
from selenium import webdriver

from endpoints.lenvendo import LenvendoAPI


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default=os.getenv("URL"))
    parser.addoption("--api", action="store", default=os.getenv("API"))
    parser.addoption("--search", action="store", default=os.getenv("SEARCH"))
    parser.addoption("--sort_field", action="store", default=os.getenv("SORT_FIELD"))


@pytest.fixture()
def base_url(request):
    return request.config.option.url


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "106.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": False,
        "screenResolution": "1280x1024x24"
    })

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4444/wd/hub",
        options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def api(request):
    return request.config.option.api


@pytest.fixture()
def params(request):
    return dict(search=request.config.option.search, sort_field=request.config.option.sort_field)


@pytest.fixture()
def lenvendo_api(api):
    return LenvendoAPI(api)
