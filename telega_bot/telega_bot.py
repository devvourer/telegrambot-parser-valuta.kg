# import telebot
# from telebot import types
# from decouple import config
#
#
# bot = telebot.TeleBot(config('TOKEN'))
#
#+
#
#
#
# keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
# btn1 = types.KeyboardButton('Van')
# btn2 = types.KeyboardButton('Владиslave')
# btn3 = types.KeyboardButton('Darkhole')
# keyboard.add(btn1, btn2, btn3)
#
# @bot.message_handler(commands=['start', 'help', 'qwe'])
# def start_message(message):
#
#
#
#     chat_id = message.chat.id
#     bot.send_message(chat_id, 'hi  boss', reply_markup=keyboard)
#     bot.send_sticker(chat_id, 'CAACAgIAAxkBAANSX_1fAnM-XeEy3q-v0zanxL4e5lAAAgYAA_HzcxMSZYmL9UOABx4E' )
#
#
#
# @bot.message_handler(content_types = ['text'])
# def send_text(message):
#     print(message.text)
#     chat_id = message.chat.id
#
#     if message.text == 'slave' :
#         bot.send_message(chat_id, f'апееееей бля {message.chat.first_name}')
#         bot.send_sticker(chat_id, 'CAACAgIAAxkBAANiX_1g56FSjDiHUb5mAe9fmbSsvKsAAhsAA_HzcxOM053faIXUfx4E')
#
#     elif message.text.lower() == 'bye':
#         bot.send_message(chat_id, f'bye bye {message.chat.first_name}')
#     elif message.text.title() == 'Van':
#         bot.send_sticker(chat_id, 'CAACAgIAAxkBAANvX_1iHOcZC8fTamG_8L0Pl-5fjVQAAhsAA_HzcxOM053faIXUfx4E')
#         # bot.register_next_step_handler(msg, inline_kb)
#     elif message.text.title() == 'Владиslave':
#         bot.send_sticker(chat_id, 'CAACAgIAAxkBAANxX_1ibfuXf-mVd9ysDQ7DOIzTNRwAAiEAA_HzcxNdaXei_a0fTx4E')
#
#     elif message.text.title() == 'Darkhole':
#         keyboard = types.InlineKeyboardMarkup(row_width=1)
#         btn1 = types.InlineKeyboardButton('Maker\s ev vol 9', callback_data='1')
#         btn2 = types.InlineKeyboardButton('Maker\s vol9', callback_data='2')
#         btn3 = types.InlineKeyboardButton('Back', callback_data='3')
#         keyboard.add(btn1, btn2, btn3)
#
#         bot.send_message(chat_id, 'ok', reply_markup=keyboard)
#
#
#
# @bot.callback_query_handler(func=lambda c:True)
# def inline_kb(c):
#     chat_id = c.message.chat.id
#     if c.data == '1':
#         bot.send_message(chat_id, 'hello python ev vol 9')
#     if c.data == '2':
#         no_kb = types.InlineKeyboardMarkup(row_width=2)
#         b1 = types.InlineKeyboardButton('1', callback_data='1')
#         b2 = types.InlineKeyboardButton('2', callback_data='2')
#         b3 = types.InlineKeyboardButton('3', callback_data='3')
#         b4 = types.InlineKeyboardButton('4', callback_data='4')
#         no_kb.add(b1, b2, b3, b4)
#         bot.edit_message_text(chat_id=chat_id, message_id=c.message.message_id,text='whats up!', reply_markup=no_kb)
#     if c.data == '3':
#         bot.edit_message_text(chat_id=chat_id,message_id=c.message.message_id, text='Main menu', reply_markup=keyboard)
#         bot.send_message(chat_id=chat_id, text='ok', reply_markup=keyboard)
#
#
#
#
#
# @bot.message_handler(content_types=['sticker'])
# def send_sticker(message):
#     chat_id = message.chat.id
#     bot.send_sticker(chat_id, f'{message.sticker.file_id}')
#     print(message)
#
#
#
# bot.polling()