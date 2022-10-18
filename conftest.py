import pytest

from ui.driver import BrowserInterface
from endpoints.lenvendo import LenvendoAPI
from fixtures.api import *


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://HR:test@qa.digift.ru/")
    parser.addoption("--api", action="store", default="/api/js-test-task")
    parser.addoption("--search", action="store", default="Alcatel")
    parser.addoption("--sort_field", action="store", default="name")
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--browser_version", action="store", default="106.0")
    parser.addoption("--hub", action="store", default="192.168.0.102")
    parser.addoption("--hub_port", action="store", default="4444")
    parser.addoption("--enable_vnc", action="store", default="false")


@pytest.fixture()
def browser(request):
    driver = BrowserInterface(request.config)
    yield driver.driver
    driver.quit()


@pytest.fixture()
def lenvendo_api(api):
    return LenvendoAPI(api)
