from selene import browser, have
from data.user import User
import time


class RegistrationPage:
    def __init__(self):
        self._first_name = browser.element('#firstName')
        self._last_name = browser.element('#lastName')
        self._email = browser.element('#userEmail')
        self._gender = browser.all('[name=gender]')
        self._mobile = browser.element('#userNumber')
        self._date_of_birth = browser.element('#dateOfBirthInput')
        self._subjects = browser.element('#subjectsInput')
        self._hobbies = browser.all('[type=checkbox]')
        self._picture = browser.element('#uploadPicture')
        self._address = browser.element('#currentAddress')
        self._state = browser.element('#state')
        self._city = browser.element('#city')
        self._submit = browser.element('#submit')
        self._results = browser.element('.table')

    def open(self):
        browser.open('/automation-practice-form')
        browser.execute_script('''
            document.querySelector('footer')?.remove();
            document.getElementById('fixedban')?.remove();
        ''')
        return self

    # ОДИН высокоуровневый шаг вместо многих
    def register(self, user: User):
        # Основные данные
        self._first_name.type(user.first_name)
        self._last_name.type(user.last_name)
        self._email.type(user.email)
        self._gender.element_by(have.value(user.gender.value)).click()
        self._mobile.type(user.mobile)

        # Дата рождения
        self._date_of_birth.click()
        browser.element('.react-datepicker__year-select').select(str(user.birth_year))
        browser.element('.react-datepicker__month-select').select(user.birth_month)
        browser.element(f'.react-datepicker__day--0{user.birth_day}').click()

        # Subjects
        if user.subjects:
            for subject in user.subjects:
                self._subjects.type(subject).press_enter()

        # Hobbies
        if user.hobbies:
            for hobby in user.hobbies:
                self._hobbies.element_by(have.value(hobby.value)).click()

        # Picture
        if user.picture:
            self._picture.set_value(user.picture)

        # Address
        if user.address:
            self._address.type(user.address)

        # State and City
        if user.state:
            self._state.click()
            browser.all('[id^=react-select][id*=option]').element_by(have.text(user.state)).click()
            time.sleep(0.5)

            if user.city:
                self._city.click()
                browser.all('[id^=react-select][id*=option]').element_by(have.text(user.city)).click()

        # Submit
        browser.execute_script('arguments[0].scrollIntoView(true);', self._submit())
        time.sleep(0.5)
        self._submit.click()
        return self

    def should_have_registered(self, user: User):
        self._results.should(have.text(user.full_name))
        self._results.should(have.text(user.email))
        self._results.should(have.text(user.gender.value))
        self._results.should(have.text(user.mobile))
        return self