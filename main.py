from src.vacancy import Vacancy
from src.files import JSONVacancyStorage
from src.abs_api import HHAPI

def user_interface():
    """Функция пользовательского интерфейса"""
    api = HHAPI()
    api.connect()

    storage = JSONVacancyStorage()

    while True:
        print("1. Найти вакансии")
        print("2. Вывести топ N вакансий по зарплате")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            query = input("Введите поисковый запрос: ")
            vacancies_data = api.get_vacancies(query)
            if vacancies_data:
                vacancies = []
                for v in vacancies_data:
                    title = v.get('name')
                    url = v.get('alternate_url')

                    salary_from = None
                    if 'salary' in v and v['salary'] is not None:
                        salary_from = v['salary'].get('from')

                    description = v.get('snippet', {}).get('requirement', '')

                    if title and url:
                        vacancies.append(Vacancy(title, url, salary_from, description))

                storage.save_vacancies(vacancies)
                print(f"Найдено {len(vacancies)} вакансий.")
            else:
                print("Вакансии не найдены.")

        elif choice == '2':
            N = int(input("Сколько вакансий вывести? "))
            vacancies = storage.load_vacancies()
            top_vacancies = sorted(vacancies)[:N]
            for vacancy in top_vacancies:
                print(vacancy)

        elif choice == '3':
            break

    api.close_connection()

if __name__ == "__main__":
    user_interface()