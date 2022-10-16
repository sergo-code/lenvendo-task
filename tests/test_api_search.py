import allure

from utils.model_lenvendo import JsTestTask
from utils.check_json_response import check_json


@allure.epic('API тесты')
@allure.feature("JsTestTask")
@allure.story("Фильтрация и сортировка по параметру")
@allure.description("Проверка работы API, получение ответа по заданным параметрам:\n"
                    "1. Все поля name в ответе на запрос содержат значение Alcatel.\n"
                    "2. Все элементы в ответе отсортированы по полю name по алфавиту от А до Я.\n")
def test_search(lenvendo_api, api, params):
    with allure.step(f"Отправка запроса GET {api}"):
        response = lenvendo_api.get(params)
    with allure.step(f"Статус код успешный (200)"):
        assert response.status_code == 200
    with allure.step(f"Ответ содержит всю информацию по шаблону, "
                     f"также содержит слово {params.get('search')} в поле {params.get('sort_field')}"):
        check_json(response.json(), params['search'])
        phones = list(map(lambda obj: JsTestTask(**obj), response.json()['products']))

    name_src = list(map(lambda phone: phone.name.lower(), phones))

    if params.get('sort_field', None) is not None:
        name_new = sorted(name_src)
        with allure.step(f"Ответ отсортирован по алфавиту"):
            assert name_src == name_new
