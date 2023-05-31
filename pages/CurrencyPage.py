from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import pytest


class CurrencyPage(BasePage):
    CURRENCYDDM = (By.CSS_SELECTOR, '#form-currency')
    SELECTEUR = (By.CSS_SELECTOR, 'button[name="EUR"]')
    SELECTUSD = (By.CSS_SELECTOR, 'button[name="USD"]')
    SELECTGBP = (By.CSS_SELECTOR, 'button[name="GBP"]')
    TAXPRICE = (By.XPATH, "//span[text()='Ex Tax: 392.30€']")


    def click_currency_btn(self):
        self.click(self.element(self.CURRENCYDDM))


    def select_eur_currency(self):
        self.click(self.element(self.SELECTEUR))

    def check_currency_changed(self):
        self.driver.execute_script("window.scrollTo(0, 880)")
        elem_text = self.element(self.TAXPRICE)
        text = elem_text.text
        assert '€' in text, 'EUR should be in price '
