from pages.registration_page import RegistrationPage
from data.user import User, Gender, Hobby
import os


def test_student_registration_high_level():
    # Полный путь к файлу для загрузки
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    file_path = os.path.join(project_dir, 'tests/photo.jpg')

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
        picture=file_path,
        address='Some Address 123',
        state='NCR',
        city='Delhi'
    )

    (RegistrationPage()
     .open()
     .register(student)
     .should_have_registered(student))