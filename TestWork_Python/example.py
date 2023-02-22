import sqlite3
import requests
import time
print("""
Скрипт принимает на вход APP_ID приложения, по нему находит название приложения через API ITunes, 
разбивает название на отдельные слова, которые вновь ищет через API и фиксирует позицию искомого приложения
в поисковой выдаче через запрос по отдельным словам. Затем заносит полученную информацию в базу данных itunes.db
""")
results = []                                     #создаем список, для сохранения результата
base_url = "https://itunes.apple.com/lookup?id="
example_id = input("Input APP ID: ")             #ввод id
data = requests.get(base_url+example_id)
if data.json().get("results"):                   #проверяем что ответ не пустой
    data = data.json()["results"][0]
    for i in data.keys():
        if i == "trackName":                     #вытаскиваем имя приложения
            app_name_str = data[i]
    app_name_spl = app_name_str.split(" ")       #разбиваем имя по пробелам на слова
    for j in app_name_spl:
        if len(j) > 2:                           #нет смысла искать слова короче трех символов
            limit = "limit=50"                   #задаем лимит
            is_it_inresults = None               #переменная принимает №-позиции, по умолчанию None
            base_url_1 = f"https://itunes.apple.com/search?term={j}&{limit}&entity=software"
            data = requests.get(base_url_1)
            if data.json()["results"]:           #ищем совпадение по id в выдаче
                for i in range(len(data.json()["results"])):
                    if data.json()["results"][i].get("trackId") == int(example_id):
                        is_it_inresults = i + 1  #совпадение есть, сохраняем позицию
            print(j)
            results.append((example_id, j, is_it_inresults,  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
else:
    results.append((example_id, None, None, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                                                 # None,None - неверный ID, пустой ответ API
conn = sqlite3.connect("itunes.db")
c = conn.cursor()
try:                                             # Проверяем, на случай если база уже создана
    c.execute("""CREATE TABLE itunes(
                                id integer,
                                word text,
                                pos integer,
                                date text)""")
except sqlite3.OperationalError:
    print("Table itunes already exists!")        # База уже существует, работаем с ней
for i in results:                                # В данном цикле подставляем данные из нашего списка в SQL-запрос
    if i[1] == None and i[2] != None:            # Проверяем и заменяем None на Null
        c.execute(f"INSERT INTO itunes VALUES ({i[0]},Null,{i[2]},'{i[3]}')")
    elif i[2] == None and i[1] != None:
        c.execute(f"INSERT INTO itunes VALUES ({i[0]},'{i[1]}',Null,'{i[3]}')")
    elif i[1] == None and i[2] == None:
        c.execute(f"INSERT INTO itunes VALUES ({i[0]},Null,Null,'{i[3]}')")
    else:
        c.execute(f"INSERT INTO itunes VALUES ({i[0]},'{i[1]}',{i[2]},'{i[3]}')")

conn.commit()
c.execute(f"SELECT * FROM itunes WHERE id = {example_id}")
[print(i) for i in c.fetchall()]                  # Распечатываем все записи по искомому ID в консоль
conn.close()