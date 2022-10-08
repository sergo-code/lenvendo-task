import allure

from page_objects.DigiftPage import Digift


@allure.epic('UI тесты')
@allure.feature("Номинал карты")
@allure.story("Выбор номинала подарочной карты")
@allure.description('Проверка работы выбора подарочной карты:\n'
                    '1. Кнопки активируются.\n'
                    '2. В поле ввода "Введите" отображается выбранный номинал.')
def test_gift_cards(browser, base_url):
    digift_page = Digift(browser, base_url)
    with allure.step(f"Открыть страницу"):
        digift_page.go_to_site()
    with allure.step("Пролистать страницу до 'Номинал карты'"):
        digift_page.scroll_to_par()
    with allure.step("Найти все кнопки с номиналом карт"):
        cards = digift_page.find_gift_cards()
    for card in cards:
        with allure.step(f"Кнопка {card.text}"):
            digift_page.click_on_card(card)
