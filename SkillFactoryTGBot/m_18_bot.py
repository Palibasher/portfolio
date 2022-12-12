import  telebot
from extensions import Converter
from config import BOT_token
from telebot import types

bot = telebot.TeleBot(BOT_token)


@bot.message_handler(commands=["start", "help"])
def handle_start_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/start")
    btn2 = types.KeyboardButton("/values")
    markup.add(btn1, btn2)
    bot.reply_to(message, f"Доброго дня, {message.chat.username}. Чтобы начать работу, введите команду в следующем формате (через пробел):\n"
                          f"<Название валюты> <В какую валюту перевести> <Кол-во переводимой валюты>\n\n"
                          f"Для того, чтобы увидеть список доступных валют, введите /values", reply_markup=markup)


@bot.message_handler(commands=["values"])
def handle_list(message):
    bot.reply_to(message, f"В данный момент доступны следующие валюты:\n"
                          f"1) Рубль\n"
                          f"2) Доллар США\n"
                          f"3) Евро\n"
                          f"4) Йена\n"
                          f"5) Юань\n"
                          f"6) Биткоин\n")


@bot.message_handler(content_types=["text"]) #берем текст
def testfunc(message: telebot.types.Message):
    values = message.text.split(" ")
    bot.reply_to(message, Converter.get_ammount(values), parse_mode="html")





bot.polling(none_stop=True)













