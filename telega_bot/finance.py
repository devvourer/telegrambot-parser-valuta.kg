# import telebot
# from telebot import types
# from decouple import config
# import csv
#
#
#
# bot = telebot.TeleBot(config('TOKEN'))
#
#
#
# inline_keyboard = types.InlineKeyboardMarkup()
# btn1 = types.InlineKeyboardButton('Доход', callback_data='income')
# btn2 = types.InlineKeyboardButton('Расход', callback_data='expenses')
# inline_keyboard.add(btn1, btn2)
#
#
#
# entry = {}
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     chat_id = message.chat.id
#     bot.send_message(chat_id, 'hello! Choose:', reply_markup=inline_keyboard)
#
#
#
# @bot.callback_query_handler(func=lambda c: True)
# def inline(c):
#     chat_id = c.message.chat.id
#     if c.data == 'income':
#         income_keyboard = types.ReplyKeyboardMarkup()
#         k1 = types.KeyboardButton('Работа')
#         k2 = types.KeyboardButton('Фриланс')
#         k3 = types.KeyboardButton('Леввки')
#         k4 = types.KeyboardButton('Other')
#         income_keyboard.add(k1, k2, k3 ,k4)
#         msg = bot.send_message(chat_id, 'choose one of this:', reply_markup=income_keyboard)
#         bot.register_next_step_handler(msg, get_category)
#     if c.data == 'expenses':
#         income_keyboard2 = types.ReplyKeyboardMarkup()
#         k1 = types.KeyboardButton('Еда')
#         k2 = types.KeyboardButton('Дорога')
#         k3 = types.KeyboardButton('Комуналка')
#         k4 = types.KeyboardButton('Other')
#         income_keyboard2.add(k1, k2, k3, k4)
#         msg = bot.send_message(chat_id, 'choose one of this', reply_markup=income_keyboard2)
#         bot.register_next_step_handler(msg, get_category)
#
# def get_category(message):
#     list_income = ['Работа', 'Фриланс', 'Леввки', 'Other']
#     list_expenses = ['Еда', 'Дорога', 'Комуналка', 'Other']
#     chat_id = message.chat.id
#     entry.update({'category': message.text})
#     if message.text in list_income:
#         msg = bot.send_message(chat_id, 'Укажите сумму заработка')
#         bot.register_next_step_handler(msg, get_amount)
#
# def get_amount(message):
#     chat_id = message.chat.id
#     entry.update({'sum': message.text})
#     print(entry.items())
#
#     with open('income.csv', 'a', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow((entry['category'], entry['sum']))
#
#     bot.send_message(chat_id, 'Ваши данные записаны', reply_markup=inline_keyboard
#
# bot.polling()
i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        continue
    i = i + 1

print(i)