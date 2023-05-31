from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from test_data import users
from faker import Faker
import time

fake = Faker()
fake_ru = Faker('ru_RU')


class OrderPage(BasePage):
    ADDTOCARTBTN = (By.CSS_SELECTOR, '.button-group button:first-child')
    CARTDROPDOWNBUTTON = (By.CSS_SELECTOR, "#cart button[data-toggle]")
    GOTOSHOPPINGCARTBYALERT = (By.XPATH, "//a[text()='shopping cart']")
    MESSAGEINSEDECART = (By.CSS_SELECTOR, "#content h1")
    CHECKOUT = (By.XPATH, "//a[text()='Checkout']")
    TEXTCHECKOUT = (By.CSS_SELECTOR, "div#content h1")
    CONTINUEBUTTON = (By.CSS_SELECTOR, "input[value='Continue']")
    INPUTNAME = (By.CSS_SELECTOR, "input[name='firstname']")
    INPUTSERNAME = (By.CSS_SELECTOR, "input[name='lastname']")
    INPUTEMAILREG = (By.CSS_SELECTOR, "#input-payment-email")
    INPUTEMAILLOG = (By.CSS_SELECTOR, "#input-email")
    INPUTEPHONE = (By.CSS_SELECTOR, "input[name='telephone']")
    INPUTADRESS = (By.CSS_SELECTOR, "input[name='address_1']")
    INPUTCITY = (By.CSS_SELECTOR, "input[name='city']")
    INPUTPOSTCODE = (By.CSS_SELECTOR, "input[name='postcode']")
    INPUTPASSREG = (By.CSS_SELECTOR, "#input-payment-password")
    INPUTPASSLOG = (By.CSS_SELECTOR, "#input-password")
    INPUTPASSCOMFIRM = (By.CSS_SELECTOR, "input[name='confirm']")
    REGIONDROPDOWN = (By.CSS_SELECTOR, "[name='zone_id']")
    SELECTREGION = (By.CSS_SELECTOR, "option[value='3514']")
    POLICYCHECKBOX = (By.CSS_SELECTOR, "input[name='agree']")
    CONTINUEREGBTN = (By.CSS_SELECTOR, "input#button-register")
    LOGINBTN = (By.CSS_SELECTOR, "input#button-login")
    ALERTWARNING = (By.CSS_SELECTOR, ".alert-warning")
    CONTINUECHECKOUTBTN = (By.CSS_SELECTOR, 'input[value="Continue"]')


    def click_addtocart_button(self): #Добавить в корзину
        self.driver.execute_script("window.scrollTo(0, 800)")
        self.click(self.element(self.ADDTOCARTBTN))

    def go_to_dropdown_cart(self): #Переход в превью корзины нажатием на кнопку дропдаун меню
        self.click(self.element(self.GOTOSHOPPINGCARTBYALERT))

    def check_if_inside_shopping_cart(self): #Пероверка в корзине ли юзер
        elem_text = self.element(self.MESSAGEINSEDECART)
        text = elem_text.text
        assert 'Shopping Cart' in text

    def checkout_order(self): #Переход в корзину через превью корзины, кнопка
        self.click(self.element(self.CHECKOUT))
        elem_text = self.element(self.TEXTCHECKOUT)
        text = elem_text.text
        assert 'Checkout' in text

    def confirm_reg_new_user(self): #Выбор способа оформления заказа - через создание нового пользователя
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.click(self.element(self.CONTINUEBUTTON))

    def fill_login_form_checkout(self): #Заполнение формы авторизации
        self.driver.execute_script("window.scrollTo(0, 300)")
        mail = users.get_mail_pass_from_file()[0]
        self._input(self.element(self.INPUTEMAILLOG), mail)
        passw = users.get_mail_pass_from_file()[1]
        self._input(self.element(self.INPUTPASSLOG), passw)
        self.click(self.element(self.LOGINBTN))

    def fill_reg_billing_inputs(self): #Заполнение формы реги юзера
        mail = users.get_email()
        self._input(self.element(self.INPUTEMAILREG), mail)
        self._input(self.element(self.INPUTEPHONE), fake_ru.phone_number())
        self.driver.execute_script("window.scrollTo(0, 600)")
        passw = users.get_pass()
        self._input(self.element(self.INPUTPASSREG), passw)
        self._input(self.element(self.INPUTPASSCOMFIRM), passw)
        users.save_users_data(mail, passw)  # Не получается вынести за функцию сохранение в файл данных, не понимаю как реализовать красивое сохранение

    def fill_main_billing_inputs(self): #Заполнение формы для рег и для авторизованного юзера
        self._input(self.element(self.INPUTNAME), fake_ru.first_name())
        self._input(self.element(self.INPUTSERNAME), fake_ru.last_name())
        self._input(self.element(self.INPUTADRESS), fake.address())
        self._input(self.element(self.INPUTCITY), fake.city())
        self.driver.execute_script("window.scrollTo(0, 600)")
        self._input(self.element(self.INPUTPOSTCODE), fake.postcode())

    def select_region_ddmenu(self): #Выбор региона в дропдаун меню
        self.click(self.element(self.REGIONDROPDOWN))
        time.sleep(3)
        select = Select(self.element(self.REGIONDROPDOWN))
        select.select_by_visible_text("Aberdeen")

    def agree_private_polit(self): #Чекбокс согласия с политикой конфидец.
        self.click(self.element(self.POLICYCHECKBOX))

    def continue_reg_click_button(self): #Клик на кнопку Continue при реге
        self.click(self.element(self.CONTINUEREGBTN))

    def continue_checkout_click_button(self): #Клик на кнопку Continue авторизованного юзера
        self.click(self.element(self.CONTINUECHECKOUTBTN))

    def check_user_get_warning_alert(self): #Проверка на переход юзера на след шаг
        self.driver.execute_script("window.scrollTo(0, -300)")
        elem_text = self.element(self.ALERTWARNING)
        text = elem_text.text
        assert 'Warning' in text