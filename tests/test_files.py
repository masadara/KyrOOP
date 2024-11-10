import os
import pytest
from src.files import JSONVacancyStorage
from src.vacancy import Vacancy


@pytest.fixture
def storage():
    storage_instance = JSONVacancyStorage()
    yield storage_instance


def test_save_load_vacancies(storage):
    vacancies = [Vacancy("Программист", "http://example.com", salary=100000)]

    storage.save_vacancies(vacancies)

    loaded_vacancies = storage.load_vacancies()

    assert len(loaded_vacancies) == 1
    assert loaded_vacancies[0].title == "Программист"


def test_load_empty_file(storage):
    if os.path.exists(storage.filename):
        os.remove(storage.filename)

    vacancies = storage.load_vacancies()

    assert vacancies == []