from faker import Faker
from test_data import LOG_DATA_PATH

fake = Faker()
fake_ru = Faker('ru_RU')


def get_email():
    return fake.email()

def get_pass():
    return fake.password()

def save_users_data(mail, passw):
    with open(LOG_DATA_PATH, 'a') as file:
        file.write(f'{mail},{passw},')

def get_users_data():
    with open(LOG_DATA_PATH, 'r') as file:
        all_files = file.readlines()
        return all_files

def get_mail_pass_from_file():
    return [element for sublist in (f.split(",") for f in get_users_data()) for element in sublist]

