import pytest
from src.abs_api import HHAPI

@pytest.fixture
def api():
    api_instance = HHAPI()
    api_instance.connect()
    yield api_instance
    api_instance.close_connection()

def test_get_vacancies(api):
    vacancies = api.get_vacancies("Python")
    assert isinstance(vacancies, list)
    assert len(vacancies) >= 0

def test_invalid_query(api):
    vacancies = api.get_vacancies("nonexistent_keyword")
    assert isinstance(vacancies, list)
    assert len(vacancies) == 0