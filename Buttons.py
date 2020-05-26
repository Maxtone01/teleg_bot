import telebot
from telebot import types

def testkboard():
    keyboard = types.InlineKeyboardMarkup()
    answer = types.InlineKeyboardButton(text="A", callback_data="A")
    answer2 = types.InlineKeyboardButton(text="Б", callback_data="Б")
    keyboard.add(answer, answer2)
    return keyboard

def keyboard1():
    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton(text="IDE PyCharm", callback_data="IDE PyCharm")
    but2 = types.InlineKeyboardButton(text="Введение в Python", callback_data="Введение в Python")
    but3 = types.InlineKeyboardButton(text="Модель данных в Python", callback_data="Модель данных в Python")
    forward = types.InlineKeyboardButton(text="Еще", callback_data="Еще")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(forward)
    return markup
def keyboard2():
    markup = types.InlineKeyboardMarkup()
    but4 = types.InlineKeyboardButton(text="Числа в Python", callback_data="Числа в Python")
    but5 = types.InlineKeyboardButton(text="Действия над данными", callback_data="Действия над данными")
    but6 = types.InlineKeyboardButton(text="Строковые выражения", callback_data="Строковые выражения")
    forward = types.InlineKeyboardButton(text="Дальше", callback_data="Дальше")
    markup.add(but4)
    markup.add(but5)
    markup.add(but6)
    markup.add(forward)
    return markup
def keyboard3():
    markup = types.InlineKeyboardMarkup()
    but7 = types.InlineKeyboardButton(text="Списочный тип данных", callback_data="Списочный тип данных")
    but8 = types.InlineKeyboardButton(text="Многомерные массивы", callback_data="Многомерные массивы")
    but9 = types.InlineKeyboardButton(text="Поиск данных, 2 части", callback_data="Поиск данных, 2 части")
    forward = types.InlineKeyboardButton(text="Следующая", callback_data="Следующая")
    markup.add(but7)
    markup.add(but8)
    markup.add(but9)
    markup.add(forward)
    return markup
def keyboard4():
    markup = types.InlineKeyboardMarkup()
    but10 = types.InlineKeyboardButton(text="Функции", callback_data="Функции")
    but11 = types.InlineKeyboardButton(text="Сортировка данных", callback_data="Сортировка данных")
    but12 = types.InlineKeyboardButton(text="Рекурсия", callback_data="Рекурсия")
    but13 = types.InlineKeyboardButton(text="Файловый тип данных", callback_data="Файловый тип данных")
    forward = types.InlineKeyboardButton(text="В начало", callback_data="В начало")
    markup.add(but10)
    markup.add(but11)
    markup.add(but12)
    markup.add(but13)
    markup.add(forward)
    return markup