"""
Модель данных пользователя с использованием dataclass
"""
from dataclasses import dataclass
from datetime import date
from enum import Enum


class Gender(Enum):
    """Пол студента"""
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class Hobby(Enum):
    """Хобби студента"""
    SPORTS = 'Sports'
    READING = 'Reading'
    MUSIC = 'Music'


@dataclass
class User:
    """Модель данных студента"""
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile: str
    birth_date: date = None
    subjects: list = None
    hobbies: list = None
    address: str = None

    @property
    def full_name(self) -> str:
        """Полное имя студента"""
        return f'{self.first_name} {self.last_name}'