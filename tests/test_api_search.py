import allure
import pytest

from utils.model_lenvendo import JsTestTask


@allure.epic('API тесты')
@allure.feature("JsTestTask")
@allure.story("Фильтрация и сортировка по параметру")
@allure.description("Проверка работы API, получение ответа по заданным параметрам:\n"
                    "1. Все поля name в ответе на запрос содержат значение Alcatel.\n"
                    "2. Все элементы в ответе отсортированы по полю name по алфавиту от А до Я.\n")
@pytest.mark.parametrize('search, sort_field', [('Alcatel', 'name')])
def test_search(lenvendo_api, api, search, sort_field):
    params = {'search': search, 'sort_field': sort_field}
    with allure.step(f"Отправка запроса GET {api}"):
        response = lenvendo_api.get(params)
    with allure.step(f"Статус код успешный (200)"):
        assert response.status_code == 200
    with allure.step(f"Ответ не пустой"):
        assert response.json() != '' or None
    with allure.step(f"Каждый json-объект имеет ключи name, image, price"):
        phones = list(map(lambda obj: JsTestTask(**obj), response.json()['products']))
    with allure.step(f"Каждый json-объект в поле {sort_field} содержит слово {search}"):
        name_src = list()
        for phone in phones:
            assert params['search'] in phone.name
            name_src.append(phone.name.lower())

    name_new = sorted(name_src)
    with allure.step(f"Ответ отсортирован по алфавиту"):
        assert name_src == name_new
