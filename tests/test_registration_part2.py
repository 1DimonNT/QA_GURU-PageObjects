from pages import RegistrationPage
from data import users
from data.user import User, Gender

def test_student_registration_with_model():
    student = users.student
    (RegistrationPage()
     .open()
     .register(student)
     .should_have_registered(student))

def test_student_registration_with_custom_user():
    custom_student = User(
        first_name='John',
        last_name='Doe',
        email='john.doe@example.com',
        gender=Gender.MALE,
        mobile='5551234567'
    )
    (RegistrationPage()
     .open()
     .register(custom_student)
     .should_have_registered(custom_student))