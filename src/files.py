import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy
import os


class VacancyStorage(ABC):
    @abstractmethod
    def save_vacancies(self, vacancies):
        pass

    @abstractmethod
    def load_vacancies(self):
        pass


class JSONVacancyStorage(VacancyStorage):
    '''Класс для сохранения в JSON'''
    def __init__(self, filename='vacancies.json'):
        self.directory = 'data'
        self.filename = os.path.join(self.directory, filename)


    def save_vacancies(self, vacancies):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([vacancy.__dict__ for vacancy in vacancies], f, ensure_ascii=False)

    def load_vacancies(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return [Vacancy(**data) for data in json.load(f)]
        except FileNotFoundError:
            return []