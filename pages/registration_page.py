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
        self._hobbies_checkbox_1 = browser.element('[for="hobbies-checkbox-1"]')
        self._hobbies_checkbox_2 = browser.element('[for="hobbies-checkbox-2"]')
        self._hobbies_checkbox_3 = browser.element('[for="hobbies-checkbox-3"]')
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

    def register(self, user: User):
        # Основные данные
        self._first_name.type(user.first_name)
        self._last_name.type(user.last_name)
        self._email.type(user.email)
        self._gender.element_by(have.value(user.gender.value)).click()
        self._mobile.type(user.mobile)

        # Дата рождения
        self._fill_date_of_birth(user.birth_year, user.birth_month, user.birth_day)

        # Subjects
        if user.subjects:
            for subject in user.subjects:
                self._subjects.type(subject).press_enter()

        # Hobbies
        if user.hobbies:
            for hobby in user.hobbies:
                if hobby.value == 'Sports':
                    self._hobbies_checkbox_1.click()
                elif hobby.value == 'Reading':
                    self._hobbies_checkbox_2.click()
                elif hobby.value == 'Music':
                    self._hobbies_checkbox_3.click()

        # Picture
        if user.picture:
            self._picture.set_value(user.picture)

        # Address
        if user.address:
            self._address.type(user.address)

        # State and City
        if user.state:
            self._select_state(user.state)
            time.sleep(0.5)
            if user.city:
                self._select_city(user.city)

        # Submit
        browser.execute_script('arguments[0].scrollIntoView(true);', self._submit())
        time.sleep(0.5)
        self._submit.click()
        return self

    def _fill_date_of_birth(self, year, month, day):
        self._date_of_birth.click()

        month_map = {
            'January': '0', 'February': '1', 'March': '2', 'April': '3',
            'May': '4', 'June': '5', 'July': '6', 'August': '7',
            'September': '8', 'October': '9', 'November': '10', 'December': '11'
        }

        browser.execute_script(
            "document.querySelector('.react-datepicker__year-select').value = arguments[0];",
            str(year)
        )
        browser.execute_script(
            "document.querySelector('.react-datepicker__month-select').value = arguments[0];",
            month_map[month]
        )
        browser.element(f'.react-datepicker__day--0{day:02d}').click()

    def _select_state(self, value):
        browser.execute_script('arguments[0].scrollIntoView(true);', self._state())
        time.sleep(0.5)
        self._state.click()
        time.sleep(0.5)
        browser.all('[id^=react-select][id*=option]').element_by(have.text(value)).click()

    def _select_city(self, value):
        browser.execute_script('arguments[0].scrollIntoView(true);', self._city())
        time.sleep(0.5)
        self._city.click()
        time.sleep(0.5)
        browser.all('[id^=react-select][id*=option]').element_by(have.text(value)).click()

    def should_have_registered(self, user: User):
        self._results.should(have.text(user.full_name))
        self._results.should(have.text(user.email))
        self._results.should(have.text(user.gender.value))
        self._results.should(have.text(user.mobile))
        return self