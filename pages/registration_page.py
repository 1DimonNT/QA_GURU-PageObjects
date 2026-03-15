from selene import browser, have
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

    def fill_first_name(self, value):
        self._first_name.type(value)
        return self

    def fill_last_name(self, value):
        self._last_name.type(value)
        return self

    def fill_email(self, value):
        self._email.type(value)
        return self

    def select_gender(self, value):
        self._gender.element_by(have.value(value)).click()
        return self

    def fill_mobile(self, value):
        self._mobile.type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        self._date_of_birth.click()
        browser.element('.react-datepicker__year-select').select(str(year))
        browser.element('.react-datepicker__month-select').select(month)
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def add_subjects(self, *subjects):
        for subject in subjects:
            self._subjects.type(subject).press_enter()
        return self

    def select_hobbies(self, *hobbies):
        for hobby in hobbies:
            self._hobbies.element_by(have.value(hobby)).click()
        return self

    def upload_picture(self, file_path):
        self._picture.set_value(file_path)
        return self

    def fill_address(self, value):
        self._address.type(value)
        return self

    def select_state(self, value):
        self._state.click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(value)).click()
        return self

    def select_city(self, value):
        self._city.click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(value)).click()
        return self

    def submit(self):
        browser.execute_script('arguments[0].scrollIntoView(true);', self._submit())
        time.sleep(0.5)
        self._submit.click()
        return self

    def should_have_registered(self, **expected):
        for key, value in expected.items():
            self._results.should(have.text(value))
        return self