from pages.OrderPage import OrderPage
import time


def test_order_for_new_user(browser):
    OrderPage(browser).click_addtocart_button()
    time.sleep(1)  #По другому часто падает
    OrderPage(browser).go_to_dropdown_cart()
    OrderPage(browser).check_if_inside_shopping_cart()
    OrderPage(browser).checkout_order()
    OrderPage(browser).confirm_reg_new_user()
    OrderPage(browser).fill_main_billing_inputs()
    OrderPage(browser).fill_reg_billing_inputs()
    OrderPage(browser).select_region_ddmenu()
    OrderPage(browser).agree_private_polit()
    OrderPage(browser).continue_reg_click_button()
    OrderPage(browser).check_user_get_warning_alert()

def test_order_regged_user(browser):
    OrderPage(browser).click_addtocart_button()
    time.sleep(1)  #По другому часто падает
    OrderPage(browser).go_to_dropdown_cart()
    OrderPage(browser).check_if_inside_shopping_cart()
    OrderPage(browser).checkout_order()
    OrderPage(browser).fill_login_form_checkout()
    OrderPage(browser).fill_main_billing_inputs()
    OrderPage(browser).select_region_ddmenu()
    OrderPage(browser).continue_checkout_click_button()
    OrderPage(browser).check_user_get_warning_alert()
