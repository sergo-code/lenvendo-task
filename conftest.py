import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from endpoints.lenvendo import LenvendoAPI


def pytest_addoption(parser):
    parser.addoption("--chrome", action="store", default=os.getenv("CHROME"))
    parser.addoption("--url", action="store", default=os.getenv("URL"))
    parser.addoption("--api", action="store", default=os.getenv("API"))


@pytest.fixture(scope="session")
def chrome(request):
    return request.config.option.chrome


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.option.url


@pytest.fixture(scope="session")
def browser(chrome):
    driver = webdriver.Chrome(service=Service(chrome))
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def api(request):
    return request.config.option.api


@pytest.fixture(scope="session")
def lenvendo_api(api):
    return LenvendoAPI(api)
