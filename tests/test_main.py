from pages.CurrencyPage import CurrencyPage
import pytest
import time


def test_add_to_wish_list(browser):
    CurrencyPage(browser).click_currency_btn()
    CurrencyPage(browser).select_eur_currency()
    CurrencyPage(browser).check_currency_changed()
    # time.sleep(5)



