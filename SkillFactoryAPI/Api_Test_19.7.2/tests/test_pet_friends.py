import sys
sys.path.append(r"C:\\Users\\brick\\PycharmProjects\\pytest_first_test\\venv\\pract\\Api_Test_19.7.2")
from settings import valid_email, valid_password, valid_email_2
from api import PetFriends
from random import randint

wrong_email, wrong_password = "wrong_email" + str(randint(0, 100000000)), "wrong_pass" + str(randint(0, 100000000)) + r"@mail.ru"
pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""
    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(email=valid_email, password=valid_password):
    """Тест проверяет, что возвращаемый статус == 200, лист питомцев не пустой и соотвествует ожидаемому типу"""
    status, result = pf.get_api_key(email, password)
    auth_key = result["key"]
    status, list_of_all_pets = pf.get_list_of_pets(auth_key)
    assert status == 200
    assert type(list_of_all_pets) == dict
    assert len(list_of_all_pets["pets"]) > 0


def test_add_new_pet_with_valid_data(email=valid_email, password=valid_password):
    """Тест, через метод класса, добавляет питомца на сервер, сверяя ответ сервера с отправляемым запросом"""
    status, result = pf.get_api_key(email, password)
    auth_key = result["key"]
    name, animal_type, age = "Вадим Вадимыч", "Птица", "1"
    status_add, result_add = pf.add_new_pet(auth_key, name, animal_type, age, "tests/images/217.jpg")
    assert status_add == 200
    assert type(result_add) == dict
    assert result_add["name"] == name
    assert result_add["age"] == age
    assert result_add["animal_type"] == animal_type

def test_add_new_pet_with_valid_data_wo_photo(email=valid_email, password=valid_password):
    """Тест, добавляет питомца без фото на сервер, сверяя ответ сервера с отправляемым запросом"""
    status, result = pf.get_api_key(email, password)
    auth_key = result["key"]
    name, animal_type, age = "Стесняш", "Кот", "1"
    status_add, result_add = pf.add_new_pet_wo_photo(auth_key, name, animal_type, age)
    assert status_add == 200
    assert type(result_add) == dict
    assert result_add["name"] == name
    assert result_add["age"] == age
    assert result_add["animal_type"] == animal_type

def test_get_my_pets_with_valid_key(email=valid_email, password=valid_password):
    """Тест проверяет, что возвращаемый статус == 200, лист питомцев не пустой и соотвествует ожидаемому типу"""
    status, result = pf.get_api_key(email, password)
    auth_key = result["key"]
    params = {"filter": "my_pets"}
    status, list_of_all_pets = pf.get_list_of_pets(auth_key, params=params)
    assert status == 200
    assert type(list_of_all_pets) == dict
    assert len(list_of_all_pets["pets"]) > 0

def test_get_id_of_firts_pet_with_valid_key(email=valid_email, password=valid_password):
    """Тест проверяет, что сервер возвращает id первого питомца из спискa"""
    status, result = pf.get_api_key(email, password)
    auth_key = result["key"]
    params = {"filter": "my_pets"}
    first_pet_id = pf.get_id_of_first_pet_on_the_list(auth_key, params=params)
    assert first_pet_id

def test_add_new_photo_by_pet_id(email=valid_email, password=valid_password):
    """Тест проверяет, что возвращаемый статус == 200, после добавления/изменения фото питомца"""
    status, result = pf.get_api_key(email, password)
    auth_key = result["key"]
    params = {"filter": "my_pets"}
    first_pet_id = pf.get_id_of_first_pet_on_the_list(auth_key, params=params)
    ph_add_status = pf.add_photo_of_pet_with_valid_id(auth_key, first_pet_id, "tests/images/111.jpg")
    assert ph_add_status == 200

def test_update_pet_information_by_pet_id(email=valid_email, password=valid_password):
    """Тест проверяет, что возвращаемый статус == 200, после изменения информации о питомце,
    так же сверяет имя в запросе и ответе"""
    status, result = pf.get_api_key(email, password)
    auth_key = result["key"]
    params = {"filter": "my_pets"}
    first_pet_id = pf.get_id_of_first_pet_on_the_list(auth_key, params=params)
    name, animal_type, age = "Рома", "Тест_Пут", "66"
    status, result = pf.update_pet_information_with_valid_id(auth_key, first_pet_id, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_delete_pet_by_pet_id(email=valid_email, password=valid_password):
    """Тест проверяет статус, после удаления питомца и наличие id удаленного питомца в списке питомцев"""
    status, result = pf.get_api_key(email, password)
    auth_key = result["key"]
    params = {"filter": "my_pets"}
    first_pet_id = pf.get_id_of_first_pet_on_the_list(auth_key, params=params)
    status_of_del = pf.delete_pet_with_valid_id(auth_key, first_pet_id)
    status, list_of_my_pets = pf.get_list_of_pets(auth_key, params=params)
    assert status_of_del == 200
    assert first_pet_id not in list_of_my_pets

def test_negative_try_to_get_authkey_with_invalid_user(email = wrong_email, password = wrong_password):
    """Тест пытается получиться API ключ, с неверными данными"""
    status = pf.negative_get_api_key(email, password)
    assert status == 403

def test_negative_add_new_pet_with_invalid_authkey(email=valid_email, password=valid_password):
    """Тест проверяет возможность добавить питомца с неверным ключом авторизации"""
    auth_key = "qwertyqwertyqwertyqwertyqwertyqwerty"
    name, animal_type, age = "Вовка", "Верблюд", "12"
    status_add, result_add = pf.add_new_pet(auth_key, name, animal_type, age, "tests/images/217.jpg")
    assert status_add == 403

def test_negative_try_add_new_pet_with_incomplite_data(email = valid_email, password = valid_password):
    """Тест пытается создать питомца с непоными данными"""
    status, result = pf.get_api_key(email, password)
    auth_key = result["key"]
    name, animal_type = "Конь", "Як"
    status_add = pf.negative_try_add_new_pet_with_incomplite_data(auth_key, name, animal_type)
    assert status_add == 400

def test_negative_try_add_pet_with_negative_age(email=valid_email, password=valid_password):
    """Тест, пытается добавить на сервер питомца с отрицательным возрастом"""
    status, result = pf.get_api_key(email, password)
    auth_key = result["key"]
    name, animal_type, age = "Я еще не родился", "Кто-то", "-1"
    status_add, result_add = pf.add_new_pet(auth_key, name, animal_type, age, "tests/images/9.jpg")
    assert status_add != 200

def test_negative_add_new_pet_with_name_that_too_long(email=valid_email, password=valid_password):
    """Тест, проверяет, что ограничени на длину имени питомца работает"""
    status, result = pf.get_api_key(email, password)
    auth_key = result["key"]
    name = "".join([chr(randint(65,90)) for i in range(100000)])
    animal_type, age =  "Ошибка", "1"
    status_add, result_add = pf.add_new_pet(auth_key, name, animal_type, age, "tests/images/long.jpg")
    assert status_add != 200

def test_negative_delete_pet_by_pet_id_by_other_user(email=valid_email, password=valid_password, email2 = valid_email_2):
    """Тест проверяет невозможность удалить питомца чужого пользователя"""
    status, result = pf.get_api_key(email, password) ##Берем ключ главного пользователя
    auth_key = result["key"]
    status, result = pf.get_api_key(email2, password) ## Берем ключ побочного пользователя
    auth_key2 = result["key"]
    ## добавляем питомца побочного пользователя
    name, animal_type, age = "Saul Goodman", "Lawyer", "47"
    status_add, result_add = pf.add_new_pet(auth_key2, name, animal_type, age, "tests/images/500.jpg")
    params = {"filter": "my_pets"}
    ## Берем id питомца из списка питомцев побочного пользователя
    first_pet_id = pf.get_id_of_first_pet_on_the_list(auth_key2, params=params)
    ## Пытаемся удалить питомца побочного пользователя из под главного пользователя
    status_of_del = pf.delete_pet_with_valid_id(auth_key, first_pet_id)
    assert status_of_del != 200 ## Не долно получиться, так как нет прав



