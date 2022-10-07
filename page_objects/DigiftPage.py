from utils.BaseApp import BasePage

from selenium.webdriver.common.by import By
import allure


class DigiftLocators:
    LOCATOR_GIFT_FIELD = (By.XPATH, "//div[@class='par']")
    LOCATOR_GIFT_BUTTON = (By.XPATH, "//button[contains(@class, 'par-options__button')]")
    LOCATOR_GIFT_BUTTON_ACTIVE = (By.XPATH, "//button[contains(@class, 'par-options__button--active')]")
    LOCATOR_GIFT_INPUT = (By.XPATH, "//input[contains(@class, 'js-par-input')]")


class Digift(BasePage):
    def scroll_to_par(self):
        self.scroll_to_element(self.find_element(DigiftLocators.LOCATOR_GIFT_FIELD))

    def check_gift_card(self):
        cards = self.find_elements(DigiftLocators.LOCATOR_GIFT_BUTTON)
        for card in cards:
            with allure.step(f"Кнопка {card.text}"):
                card.click()
                assert self.find_element(DigiftLocators.LOCATOR_GIFT_BUTTON_ACTIVE).text == card.text, card.text
                assert self.find_element(DigiftLocators.LOCATOR_GIFT_INPUT).get_attribute('value') == card.text, card.text
