"""
Page Object для формы регистрации на demoqa.com
Реализует обе части задания: mid-level и high-level step objects
"""
from selene import browser, have
from data.user import User
import time


class RegistrationPage:
    def __init__(self):
        # Инициализация элементов формы
        self._first_name = browser.element('#firstName')
        self._last_name = browser.element('#lastName')
        self._email = browser.element('#userEmail')
        self._gender_male = browser.element('[name=gender][value=Male]')
        self._gender_female = browser.element('[name=gender][value=Female]')
        self._gender_other = browser.element('[name=gender][value=Other]')
        self._mobile = browser.element('#userNumber')
        self._submit_button = browser.element('#submit')

        # Таблица с результатами
        self._results_table = browser.element('.table')

    def open(self):
        """Открытие страницы регистрации"""
        browser.open('/automation-practice-form')

        # Удаляем мешающие элементы
        browser.execute_script('''
            const footer = document.querySelector('footer');
            if (footer) footer.remove();
            const fixedban = document.getElementById('fixedban');
            if (fixedban) fixedban.remove();
        ''')
        return self

    # === ЧАСТЬ I: Mid-level шаги (Fluent interface) ===
    def fill_first_name(self, value: str):
        self._first_name.type(value)
        return self

    def fill_last_name(self, value: str):
        self._last_name.type(value)
        return self

    def fill_email(self, value: str):
        self._email.type(value)
        return self

    def fill_gender(self):
        self._gender_male.click()
        return self

    def fill_mobile(self, value: str):
        self._mobile.type(value)
        return self

    def submit(self):
        browser.execute_script('arguments[0].scrollIntoView(true);', self._submit_button())
        time.sleep(0.5)
        self._submit_button.click()
        return self

    # === ЧАСТЬ II: High-level шаг (работа с моделью User) ===
    def register(self, user: User):
        self._first_name.type(user.first_name)
        self._last_name.type(user.last_name)
        self._email.type(user.email)

        if user.gender.value == 'Male':
            self._gender_male.click()
        elif user.gender.value == 'Female':
            self._gender_female.click()
        else:
            self._gender_other.click()

        self._mobile.type(user.mobile)

        browser.execute_script('arguments[0].scrollIntoView(true);', self._submit_button())
        time.sleep(0.5)
        self._submit_button.click()
        return self

    # === Проверки (универсальные) ===
    def should_have_registered(self, *args):
        time.sleep(1)  # Ждем появления таблицы

        if len(args) == 1 and isinstance(args[0], User):
            user = args[0]
            self._results_table.should(have.text(user.full_name))
            self._results_table.should(have.text(user.email))
            self._results_table.should(have.text(user.gender.value))
            self._results_table.should(have.text(user.mobile))
        else:
            for label, value in args:
                self._results_table.should(have.text(value))
        return self