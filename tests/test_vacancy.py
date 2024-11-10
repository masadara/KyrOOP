import pytest
from src.vacancy import Vacancy

def test_vacancy_creation():
    vacancy = Vacancy("Программист", "http://example.com", salary=100000, description="Разработка приложений")
    assert vacancy.title == "Программист"
    assert vacancy.url == "http://example.com"
    assert vacancy.salary == 100000

def test_vacancy_salary_default():
    vacancy = Vacancy("Программист", "http://example.com")
    assert vacancy.salary == 'Зарплата не указана'

def test_vacancy_comparison():
    v1 = Vacancy("Junior Developer", "http://example.com", salary=50000)
    v2 = Vacancy("Senior Developer", "http://example.com", salary=100000)
    assert v1 < v2