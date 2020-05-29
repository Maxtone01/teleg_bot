import telebot
from telebot import types
from Buttons import testkboard, testkboard2, testkboard3, testkboard4, testkboard5, \
    testkboard6, keyboard1, keyboard2, keyboard3, keyboard4

bot = telebot.TeleBot('1210210101:AAGW40l8xdvQ0yu_or9SAa0XiNK58W-ixqw')

@bot.message_handler(commands=['test'])
def start_message(message):
    img = open('Test' + '/' + 'test1.png', 'rb')
    bot.send_photo(message.chat.id, img, reply_markup=testkboard())

@bot.message_handler(commands=['docs'])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Сайт с документацией", url="https://docs.python.org/3/")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "По нажатию кнопки вы перейдете на сайт с официальной документацией.",
                     reply_markup=keyboard)

@bot.message_handler(commands=['lections'])
def start_message(message):
    keyboard = types.InlineKeyboardMarkup()
    forward = types.InlineKeyboardButton(text="Еще", callback_data="Еще")
    keyboard.add(forward)
    bot.send_message(message.chat.id, text="Какую хотите выбрать лекцию?", reply_markup=keyboard1())

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот который создан для того чтобы помочь тебе в обучении языка Python.'
                                      '\n Напиши /help чтобы получить полную информацию по функционалу.')

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, '/docs - Предложит перейти вам на сайт с официальной документацией по языку '
                                      '\n /lections - Лекции по пайтону. \n /test - Пройти тест. '
                                      '\n  Так же чтобы повысить ваши навыки программирования, '
                                      'я предлагаю вам читать исхожные коды других программистов. '
                                      'Чтобы перейти на сайт гитхаба, выберите команду /hub')


@bot.message_handler(commands=['hub'])
def start_message(message):
    kb = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Сайт Github", url="https://github.com/search?q=games+python")
    kb.add(url_button)
    bot.send_message(message.chat.id, "По нажатию кнопки вы перейдете на сайт. Рекомендую вам зарегестрироваться, "
                                      "если вы этого еще не сделали, "
                                      "чтобы загружать туда свои работы "
                                      "для наполнения вашего будущего резюме", reply_markup=kb)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Здравствуй')
    elif message.text == 'Что такое ООП':
        bot.send_message(message.chat.id, 'Объектно-ориентированное программирование '
                                          '(ООП) — методология программирования, '
                                          'основанная на представлении программы в виде совокупности объектов, '
                                          'каждый из которых является экземпляром определённого класса, '
                                          'а классы образуют иерархию наследовния')
    elif message.text == ".img":
        bot.send_message(message.chat.id, 'К сожалению, я не понимаю картинок')

@bot.callback_query_handler(func=lambda call: True)
def longname(call):
    if call.data == "IDE PyCharm":
        uis_pdf = open('Lections' + '/' + 'IDE PyCharm.pdf', 'rb')
        bot.send_document(call.message.chat.id, uis_pdf)
        uis_pdf.close()
    elif call.data == "Введение в Python":
        uis_pdf = open('Lections' + '/' + 'Введение в Python.pdf', 'rb')
        bot.send_document(call.message.chat.id, uis_pdf)
        uis_pdf.close()
    elif call.data == "Модель данных в Python":
        uis_pdf = open('Lections' + '/' + 'Модель данных в Python.pdf', 'rb')
        bot.send_document(call.message.chat.id, uis_pdf)
        uis_pdf.close()
    elif call.data == "Числа в Python":
        uis_pdf = open('Lections' + '/' + 'Числа в Python.pdf', 'rb')
        bot.send_document(call.message.chat.id, uis_pdf)
        uis_pdf.close()
    elif call.data == "Действия над данными":
        uis_pdf = open('Lections' + '/' + 'Действия над данными.pdf', 'rb')
        bot.send_document(call.message.chat.id, uis_pdf)
        uis_pdf.close()
    elif call.data == "Строковые выражения":
        uis_pdf = open('Lections' + '/' + 'Строковые выражения.pdf', 'rb')
        bot.send_document(call.message.chat.id, uis_pdf)
        uis_pdf.close()
    elif call.data == "Списочный тип данных":
        uis_pdf = open('Lections' + '/' + 'Списочный тип данных.pdf', 'rb')
        bot.send_document(call.message.chat.id, uis_pdf)
        uis_pdf.close()
    elif call.data == "Многомерные массивы":
        uis_pdf = open('Lections' + '/' + 'Многомерные массивы.pdf', 'rb')
        bot.send_document(call.message.chat.id, uis_pdf)
        uis_pdf.close()
    elif call.data == "Поиск данных, 2 части":
        uis_pdf = open('Lections' + '/' + 'Поиск данных.pdf', 'rb')
        bot.send_document(call.message.chat.id, uis_pdf)
        uis_pdf.close()
    elif call.data == "Поиск данных, 2 части":
        uis_pdf = open('Lections' + '/' + 'Поиск данных, 2 часть.pdf', 'rb')
        bot.send_document(call.message.chat.id, uis_pdf)
        uis_pdf.close()
    elif call.data == "Функции":
        uis_pdf = open('Lections' + '/' + 'Функции.pdf', 'rb')
        bot.send_document(call.message.chat.id, uis_pdf)
        uis_pdf.close()
    elif call.data == "Сортировка данных":
        uis_pdf = open('Lections' + '/' + 'Сортировка данных.pdf', 'rb')
        bot.send_document(call.message.chat.id, uis_pdf)
        uis_pdf.close()
    elif call.data == "Рекурсия":
        uis_pdf = open('Lections' + '/' + 'Рекурсия.pdf', 'rb')
        bot.send_document(call.message.chat.id, uis_pdf)
        uis_pdf.close()
    elif call.data == "Файловый тип данных":
        uis_pdf = open('Lections' + '/' + 'Файловый тип данных.pdf', 'rb')
        bot.send_document(call.message.chat.id, uis_pdf)
        uis_pdf.close()
# Tests.
    if call.data == "A":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Верно")
        img = open('Test' + '/' + 'Test2.png', 'rb')
        bot.edit_message_media(media=types.InputMedia(type='photo', media=img),
                               chat_id=call.message.chat.id,
                               message_id=call.message.message_id,
                               reply_markup=testkboard2())
    elif call.data == "B":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Не верно")
    elif call.data == "D":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Верно")
        img = open('Test' + '/' + 'Test3.png', 'rb')
        bot.edit_message_media(media=types.InputMedia(type='photo', media=img),
                               chat_id=call.message.chat.id,
                               message_id=call.message.message_id,
                               reply_markup=testkboard3())
    elif call.data == "C":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Не верно")
    elif call.data == "E":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Верно")
        img = open('Test' + '/' + 'Test4.png', 'rb')
        bot.edit_message_media(media=types.InputMedia(type='photo', media=img),
                               chat_id=call.message.chat.id,
                               message_id=call.message.message_id,
                               reply_markup=testkboard4())
    elif call.data == "F":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Не верно")
    elif call.data == "G":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Верно")
        img = open('Test' + '/' + 'Test5.png', 'rb')
        bot.edit_message_media(media=types.InputMedia(type='photo', media=img),
                               chat_id=call.message.chat.id,
                               message_id=call.message.message_id,
                               reply_markup=testkboard5())
    elif call.data == "H":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Не верно")
    elif call.data == "I":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Верно")
        img = open('Test' + '/' + 'Test6.png', 'rb')
        bot.edit_message_media(media=types.InputMedia(type='photo', media=img),
                               chat_id=call.message.chat.id,
                               message_id=call.message.message_id,
                               reply_markup=testkboard6())
    elif call.data == "J":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Не верно")
    elif call.data == "K":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Не верно")
    elif call.data == "M":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Верно")
        bot.send_message(call.message.chat.id, text="Тест закончен")
    elif call.data == "L":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Не верно")


    if call.data == "Еще":
        bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id, reply_markup=keyboard2())
    if call.data == "Дальше":
        bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id, reply_markup=keyboard3())
    if call.data == "Следующая":
        bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id, reply_markup=keyboard4())
    if call.data == "В начало":
        bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id, reply_markup=keyboard1())

if __name__ == "__main__":
    bot.polling(none_stop=True)
