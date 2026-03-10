"""
Предопределенные пользователи для тестов
"""
from datetime import date
from .user import User, Gender, Hobby


# Тестовый студент
student = User(
    first_name='Yasha',
    last_name='Kramarenko',
    email='yashaka@gmail.com',
    gender=Gender.MALE,
    mobile='1234567890',
    birth_date=date(1990, 1, 1),
    subjects=['Computer Science'],
    hobbies=[Hobby.SPORTS, Hobby.READING],
    address='Some Address 123'
)