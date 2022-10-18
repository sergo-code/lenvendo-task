from .base_page import BasePage
from ui.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def scroll_to_par(self):
        self.scroll_to_element(self.find_element(MainPageLocators.LOCATOR_GIFT_FIELD))

    def find_gift_cards(self):
        return self.find_elements(MainPageLocators.LOCATOR_GIFT_BUTTON)

    def click_on_card(self, card):
        card.click()
        assert self.find_element(MainPageLocators.LOCATOR_GIFT_BUTTON_ACTIVE).text == card.text, card.text
        assert self.find_element(MainPageLocators.LOCATOR_GIFT_INPUT).get_attribute('value') == card.text, card.text
