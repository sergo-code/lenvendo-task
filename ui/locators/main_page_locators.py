from selenium.webdriver.common.by import By


class MainPageLocators:
    LOCATOR_GIFT_FIELD = (By.XPATH, "//div[@class='par']")
    LOCATOR_GIFT_BUTTON = (By.XPATH, "//button[contains(@class, 'par-options__button')]")
    LOCATOR_GIFT_BUTTON_ACTIVE = (By.XPATH, "//button[contains(@class, 'par-options__button--active')]")
    LOCATOR_GIFT_INPUT = (By.XPATH, "//input[contains(@class, 'js-par-input')]")
