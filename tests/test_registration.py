from pages.RegLoginPage import RegLogin
import pytest
import time


def test_e2e_registration(browser):
    RegLogin(browser).click_myaccount_btn()
    RegLogin(browser).go_to_reg_page()
    RegLogin(browser).fill_reg_form()
    RegLogin(browser).select_checkbox_policy()
    RegLogin(browser).confirm_sending_form()
    RegLogin(browser).check_congrat_message()
    # RegLogin(browser).write_mail_pass_to_file()
    time.sleep(5)

def test_login_logout(browser):

    RegLogin(browser).click_myaccount_btn()
    RegLogin(browser).go_to_login_page()
    RegLogin(browser).fill_login_form_data_from_file()
    RegLogin(browser).click_login_btn()
    RegLogin(browser).check_user_logged_in()
    RegLogin(browser).click_myaccount_btn()
    RegLogin(browser).log_out()
    RegLogin(browser).check_if_account_is_logged_out()







