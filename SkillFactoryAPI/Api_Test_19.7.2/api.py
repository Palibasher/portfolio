"""Модуль 19"""
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
# from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    """апи библиотека к веб приложению Pet Friends"""

    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email, passwd):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с уникальным ключем пользователя, найденного по указанным email и паролем"""

        headers = {
            'email': email,
            'password': passwd,
        }
        res = requests.get(self.base_url+"api/key", headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, params = ""):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком наденных питомцев, совпадающих с фильтром. На данный момент фильтр может иметь
        либо пустое значение - получить список всех питомцев, либо 'my_pets' - получить список
        собственных питомцев"""
        headers = {
            "auth_key": auth_key,
        }
        res = requests.get(self.base_url+"api/pets", headers = headers, params = params)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet_wo_photo(self, auth_key, name, animal_type, age):
        """Метод делает запрос к API сервера добавляет питомца без фото на сервер, вовращает статус
        полученного ответа и его содержание"""
        data = MultipartEncoder(
            fields={
                "name": name,
                "animal_type": animal_type,
                "age": age,
                })
        headers = {"auth_key": auth_key, "Content-Type": data.content_type}

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key, name, animal_type, age, pet_photo):
        """Метод делает запрос к API сервера добавляет питомца на сервер, вовращает статус
        полученного ответа и его содержание"""
        data = MultipartEncoder(
            fields={
                "name": name,
                "animal_type": animal_type,
                "age": age,
                "pet_photo": (pet_photo, open(pet_photo, "rb"), "image/jpeg")
                })
        headers = {"auth_key": auth_key, "Content-Type": data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_id_of_first_pet_on_the_list(self, auth_key, params = ""):
        """Метод вызывает другой метод, который возвращает список питомцев,
        обрабатывает ответ и возвращает id первого в списке питомца,
        если список пустой, выдает информацию об ошибке в консоль"""
        _, list_of_pets = self.get_list_of_pets(auth_key, params = params)
        if len(list_of_pets["pets"]) > 0:
            return list_of_pets["pets"][0]["id"]
        else:
            return "NO PETS ON THE LIST"



    def add_photo_of_pet_with_valid_id(self, auth_key, pet_id, pet_photo):
        """Метод добавляет фотографию к уже существующему питомцу без фото, либо меняет текущее фото,
        обращаясь к питомцу по id"""
        data = MultipartEncoder(
            fields={
                "pet_photo": (pet_photo, open(pet_photo, "rb"), "image/jpeg")
            })
        headers = {
            "auth_key": auth_key,
            "Content-Type": data.content_type
        }
        res = requests.post(self.base_url + "api/pets/set_photo/" + pet_id, headers = headers, data = data)
        status = res.status_code
        return status

    def update_pet_information_with_valid_id(self, auth_key, pet_id, name, animal_type, age):
        """Метод изменяет информации о питомце по его id"""
        data = MultipartEncoder(
            fields={
                "name": name,
                "animal_type": animal_type,
                "age": age,
            })
        headers = {"auth_key": auth_key, "Content-Type": data.content_type}
        res = requests.put(self.base_url + "api/pets/" + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


    def delete_pet_with_valid_id(self, auth_key, pet_id):
        headers = {
            "auth_key": auth_key,
        }
        res = requests.delete(self.base_url + "api/pets/" + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status

    def negative_get_api_key(self, wrong_email, wrong_password):
        """Метод делает запрос к API сервера и возвращает ошибку, т.к. мы задаем
        неверные данные пользователя"""

        headers = {
            'email': wrong_email,
            'password': wrong_password,
        }
        res = requests.get(self.base_url+"api/key", headers=headers)
        status = res.status_code
        return status

    def negative_try_add_new_pet_with_incomplite_data(self, auth_key, name, animal_type):
        """Метод делает запрос к API сервера, пытается добавить питомца с неполными данными и возвращает статус"""
        data = MultipartEncoder(
            fields={
                "name": name,
                "animal_type": animal_type,
            })
        headers = {"auth_key": auth_key, "Content-Type": data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        return status
