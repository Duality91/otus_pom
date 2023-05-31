from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from test_data import users
from faker import Faker

fake = Faker()
fake_ru = Faker('ru_RU')


class RegLogin(BasePage):
    MYACCOUNTBTN = (By.CSS_SELECTOR, "#top a[title='My Account']")
    REGISTRATEBTN = (By.XPATH, "//a[text()='Register']")
    LOGINBTN = (By.XPATH, "//a[text()='Login']")
    INPUTFIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUTLASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    INPUTEMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUTTELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    INPUTPASS = (By.CSS_SELECTOR, "#input-password")
    INPUTPASSCONF = (By.CSS_SELECTOR, "#input-confirm")
    CHECKBOXPOLICY = (By.CSS_SELECTOR, "input[type='checkbox']")
    CONTINUEBTN = (By.CSS_SELECTOR, "input[value='Continue']")
    CONGRATMSG = (By.CSS_SELECTOR, "#content h1")
    LOGENTERBTN = (By.CSS_SELECTOR, "input[value='Login']")
    CHECKMYACCOUNT = (By.XPATH, "//h2[text()='My Account']")
    LOGOUTBTN = (By.XPATH, "//a[text()='Logout']")
    LOGGEDOUT = (By.XPATH, "//h1[text()='Account Logout']")

    def click_myaccount_btn(self):  #Переход на страницу реги с главной
        self.click(self.element(self.MYACCOUNTBTN))

    def go_to_reg_page(self): #Переход на страницу реги
        self.click(self.element(self.REGISTRATEBTN))
        self.driver.execute_script("window.scrollTo(0, 600)")

    def go_to_login_page(self): #Переход на страницу авторизации
        self.click(self.element(self.LOGINBTN))

    def fill_reg_form(self):  #Заполнение формы реги
        self._input(self.element(self.INPUTFIRSTNAME), fake_ru.first_name())
        self._input(self.element(self.INPUTLASTNAME), fake_ru.last_name())
        mail = users.get_email()
        self._input(self.element(self.INPUTEMAIL), mail)
        self.driver.execute_script("window.scrollTo(0, 600)")
        self._input(self.element(self.INPUTTELEPHONE), fake_ru.phone_number())
        passw = users.get_pass()
        self._input(self.element(self.INPUTPASS), passw)
        self._input(self.element(self.INPUTPASSCONF), passw)
        self.driver.execute_script("window.scrollTo(0, 600)")
        users.save_users_data(mail, passw)  #Не получается вынести за функцию сохранение в файл данных, не понимаю как реализовать красивое сохранение

    # def write_mail_pass_to_file(self, fill_): #Сохранение мэйла и пароля в файл
    #     users.save_users_data(mail, passw)

    def select_checkbox_policy(self): #Чекбокс согласия с политикой конфидецииальности
        self.click(self.element(self.CHECKBOXPOLICY))

    def confirm_sending_form(self): #Подтверждение ввода данных кнопка "Продолжить"
        self.click(self.element(self.CONTINUEBTN))

    def check_congrat_message(self): #Проверка наличия сообщения, подтверждающего успешную регистрацию
        elem_text = self.element(self.CONGRATMSG)
        text = elem_text.text
        assert 'Created' in text

    def fill_login_form_data_from_file(self): #Заполнение формы авторизации
        self._input(self.element(self.INPUTEMAIL), users.get_mail_pass_from_file()[0])
        self._input(self.element(self.INPUTPASS), users.get_mail_pass_from_file()[1])
        self.driver.execute_script("window.scrollTo(0, 200)")

    def click_login_btn(self): #Нажатие кнопки авторизации
        self.click(self.element(self.LOGENTERBTN))

    def check_user_logged_in(self): #Проверка на успешную авторизации
        elem_text = self.element(self.CHECKMYACCOUNT)
        text = elem_text.text
        assert 'My Account' in text

    def log_out(self): #Выход из учетки
        self.click(self.element(self.LOGOUTBTN))

    def check_if_account_is_logged_out(self): #Проверка сообщения, свидетельствующего о выходе
        elem_text = self.element(self.LOGGEDOUT)
        text = elem_text.text
        assert 'Logout' in text



