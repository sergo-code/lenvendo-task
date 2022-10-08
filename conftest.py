import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from endpoints.lenvendo import LenvendoAPI


def pytest_addoption(parser):
    parser.addoption("--chrome", action="store", default=os.getenv("CHROME"))
    parser.addoption("--url", action="store", default=os.getenv("URL"))
    parser.addoption("--api", action="store", default=os.getenv("API"))
    parser.addoption("--search", action="store", default=os.getenv("SEARCH"))
    parser.addoption("--sort_field", action="store", default=os.getenv("SORT_FIELD"))


@pytest.fixture()
def chrome(request):
    return request.config.option.chrome


@pytest.fixture()
def base_url(request):
    return request.config.option.url


@pytest.fixture()
def browser(chrome):
    driver = webdriver.Chrome(service=Service(chrome))
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
