from class_abstract import BaseVacancy

class Vacancy(BaseVacancy):
    def cast_to_object_list(self):
        pass
 # def get_vacancies(self,
 #                      text: str,
 #                      salary: int,
 #                      per_page: int = 5,
 #                      area: int = 1,
 #                      accept_temporary: bool = False) -> list[dict]:
 #        if not self.__response_check():
 #            raise ConnectionError("API недоступно. Невозможно получить вакансии.")
 #
 #        headers = {'User-Agent': USER_AGENT}
 #        params = {
 #            'text': text,
 #            'salary': salary,
 #            'per_page': per_page,
 #            'area': area,
 #            'accept_temporary': accept_temporary
 #        }
 #        try:
 #            response = requests.get(self.url, headers=headers, params=params)
 #            response.raise_for_status()  # Если код будет 200
 #            return response.json().get('items', [])  # получение items если найдет( или [] )
 #        except requests.exceptions.RequestException as e:  # отлов только сетевых ошибок
 #            raise ValueError(f"Ошибка при выполнении запроса: {e}") from e  # Сохранить историю ошибки from e