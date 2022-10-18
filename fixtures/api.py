import pytest


@pytest.fixture()
def base_url(request):
    return request.config.option.url


@pytest.fixture()
def api(request):
    return request.config.option.api


@pytest.fixture()
def params(request):
    return dict(search=request.config.option.search, sort_field=request.config.option.sort_field)
