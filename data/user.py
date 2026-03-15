from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class Hobby(Enum):
    SPORTS = 'Sports'
    READING = 'Reading'
    MUSIC = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile: str
    birth_year: int = 1990
    birth_month: str = 'January'
    birth_day: int = 1
    subjects: list = None
    hobbies: list = None
    picture: str = None
    address: str = None
    state: str = None
    city: str = None

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'