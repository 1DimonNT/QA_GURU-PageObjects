from pages.registration_page import RegistrationPage
from data.user import User, Gender, Hobby


def test_student_registration_high_level():
    student = User(
        first_name='Yasha',
        last_name='Kramarenko',
        email='yashaka@gmail.com',
        gender=Gender.MALE,
        mobile='1234567890',
        birth_year=1990,
        birth_month='January',
        birth_day=1,
        subjects=['Computer Science', 'Maths'],
        hobbies=[Hobby.SPORTS, Hobby.READING],
        picture='test.jpg',
        address='Some Address 123',
        state='NCR',
        city='Delhi'
    )

    (RegistrationPage()
     .open()
     .register(student)
     .should_have_registered(student))