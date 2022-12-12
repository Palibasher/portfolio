import requests
import json
from config import key, coins, suf_coins

class ConversionExeptions(Exception):
    pass

class Converter:
    @staticmethod
    def get_ammount(values):
        if len(values) != 3:
            return "Неверные параметры, взгляни еще раз на правила написания запроса: /help"
        what_we_have, what_we_need, ammount = values
        print(what_we_have, what_we_need, coins.keys())
        if what_we_have.lower() in coins.keys() and what_we_need.lower() in coins.keys():
            what_we_need = coins[what_we_need.lower()]
            what_we_have = coins[what_we_have.lower()]
        elif what_we_have.lower() in coins.keys() and what_we_need.lower() not in coins.keys():
            return f"{what_we_need} не является доступной валютой из списка, проверь <b>/values</b> - список доступных валют"
        elif what_we_have.lower() not in coins.keys() and what_we_need.lower() in coins.keys():
            return f"{what_we_have} не является доступной валютой из списка, проверь <b>/values</b> - список доступных валют"
        else:
            return f"{what_we_have} и {what_we_need} не являются доступными валютами из списка, проверь <b>/values</b> - список доступных валют"
        if what_we_have == what_we_need:
            return f"Нельзя конвертировать {what_we_need} в {what_we_need}, это не имеет смысла"
        what_we_need_suf = suf_coins[what_we_need]
        what_we_have_suf = suf_coins[what_we_have]
        try:
            ammount = int(ammount)
            print(what_we_have, what_we_need, ammount)
            url = f"https://api.apilayer.com/exchangerates_data/convert?to={what_we_need}&from={what_we_have}&amount={ammount}"
            payload = {}
            headers = {"apikey": key}
            response = requests.request("GET", url, headers=headers, data=payload)
            status_code = response.status_code
            result = response.text
            result_py = json.loads(response.content)
            print(status_code, result_py)
            if result_py['success'] == True:
                return f"Конвертация {ammount} {what_we_have_suf}....\nРезультат: <b>{result_py['result']}</b> {what_we_need_suf}."
            else:
                return "Ошибка сервера"
        except ValueError:
            return "Кажется, ты неправильно вводишь цифры. Взгляни еще раз на правила написания запроса: /help"
